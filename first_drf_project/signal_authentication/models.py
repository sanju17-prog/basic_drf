from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

# Signal for creating token for new user
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance = None, created = False, **kwargs):
    if created:
        Token.objects.create(user = instance)

# Create your models here.
class StudentSignal(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    roll = models.IntegerField()
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.name