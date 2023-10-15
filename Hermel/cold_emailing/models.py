from django.db import models

# cold_emailing/models.py

class User(models.Model):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    password_hash = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Campaign(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# Email Model
class Email(models.Model):
    subject = models.CharField(max_length=255)
    body = models.TextField()
    campaign = models.ForeignKey(Campaign, related_name='emails', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# Contacts Model
class Contact(models.Model):
    email = models.EmailField()
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    user = models.ForeignKey(User, related_name='contacts', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# Campaigns_Contacts Join Table Model
class CampaignContact(models.Model):
    campaign = models.ForeignKey(Campaign, related_name='campaign_contacts', on_delete=models.CASCADE)
    contact = models.ForeignKey(Contact, related_name='campaign_contacts', on_delete=models.CASCADE)