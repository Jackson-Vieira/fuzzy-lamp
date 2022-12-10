from django.dispatch import receiver
from django.db.models.signals import post_save

from .models import Link, Price, LinkSituationChoice

from .utils import get_link_book_data

@receiver(post_save, sender=Link)
def link_save(sender, instance, created, **kwargs):
    if created:
        # send a task
        link = instance
        data = get_link_book_data(link.link)
        print('here')
        link.name = data.get('name')
        link.image_url = data.get('image_url')
        link.situation = LinkSituationChoice.calculed
        link.save()
        Price.objects.create(link=link, price=data.get('price'))