from django.dispatch import receiver
from django.db.models.signals import post_save

from .models import Link, Price

@receiver(post_save, sender=Link)
def save_profile(sender, instance, created, **kwargs):
    if created:
        print('link criado')
        print('hora de trabalhar!')
        print('enviar uma task...')
