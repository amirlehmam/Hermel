from django.shortcuts import render

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

class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

class CampaignContactViewSet(viewsets.ModelViewSet):
    queryset = CampaignContact.objects.all()
    serializer_class = CampaignContactSerializer

from django.http import HttpResponse

def home(request):
    return HttpResponse("""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Bienvenue sur Hermel</title>
        </head>
        <body>
            <h1>Bienvenue sur la plateforme Hermel !</h1>
            <p>
                Nous sommes ravis de vous annoncer le développement de Hermel, 
                votre solution ultime pour le cold emailing.
            </p>
            <p>
                Parmi les fonctionnalités prévues, vous trouverez :
            </p>
            <ul>
                <li>SpinText IA pour la personnalisation des e-mails</li>
                <li>Intégration avec divers CRM</li>
                <li>Séquençage des e-mails</li>
                <li>Pixels pour le suivi des e-mails</li>
                <li>Fonctionnalités de Warm-up pour les adresses e-mail</li>
                <li>Dashboard pour le scoring des campagnes d'emailing</li>
            </ul>
            <p>
                Nous sommes en phase finale de développement et prévoyons d'être 
                opérationnels dans un mois.
            </p>
            <p>
                Restez à l'écoute pour les mises à jour !
            </p>
        </body>
        </html>
    """)

