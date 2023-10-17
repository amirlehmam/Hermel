# cold_emailing/views.py

from django.http import HttpResponse
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import User, Campaign, Email, Contact, CampaignContact
from .serializers import UserSerializer, CampaignSerializer, EmailSerializer, ContactSerializer, CampaignContactSerializer
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import make_password
from rest_framework import viewsets, status
from rest_framework.response import Response
from django.urls import get_resolver
from django.shortcuts import render
from rest_framework.decorators import action

def home_view(request):
    url_patterns = get_resolver().reverse_dict.keys()
    readable_urls = [str(pattern) for pattern in url_patterns if isinstance(pattern, str)]
    
    # Filtrer les URL qui ne nécessitent pas d'arguments
    filtered_urls = [url for url in readable_urls if 'detail' not in url]
    
    context = {
        'readable_urls': filtered_urls,
    }
    return render(request, 'home.html', context)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            # Hasher le mot de passe avant de l'enregistrer
            password = request.data.get('password_hash')
            hashed_password = make_password(password)  # Utilisation du hachage de mot de passe de Django
            serializer.validated_data['password_hash'] = hashed_password
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CampaignViewSet(viewsets.ModelViewSet):
    queryset = Campaign.objects.all()
    serializer_class = CampaignSerializer

class EmailViewSet(viewsets.ModelViewSet):
    queryset = Email.objects.all()
    serializer_class = EmailSerializer
    
from django.core.mail import EmailMessage
from .models import EmailSettings
from .serializers import EmailSettingsSerializer
from rest_framework.decorators import api_view

class EmailSettingsViewSet(viewsets.ModelViewSet):
    queryset = EmailSettings.objects.all()
    serializer_class = EmailSettingsSerializer


@api_view(['POST'])
def send_email(request):
    try:
        email_settings = EmailSettings.objects.get(user=request.user)
    except EmailSettings.DoesNotExist:
        return Response({"error": "Email settings not found"}, status=status.HTTP_404_NOT_FOUND)

    email = EmailMessage(
        subject=request.data.get("subject"),
        body=request.data.get("body"),
        from_email=email_settings.email,
        to=[request.data.get("to_email")],
    )
    email.send()

    return Response({"message": "Email sent successfully"}, status=status.HTTP_200_OK)


class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

class CampaignContactViewSet(viewsets.ModelViewSet):
    queryset = CampaignContact.objects.all()
    serializer_class = CampaignContactSerializer