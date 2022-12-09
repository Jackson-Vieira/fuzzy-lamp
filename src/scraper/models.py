from django.db import models
from .utils import get_link_book_data

class LinkTypeChoice(models.TextChoices):
    book = 'book'
    kindle_book = 'kindle'
    generic = 'generic'

class Link(models.Model):
    name = models.CharField(max_length=220, blank=True)
    link_type = models.CharField(
        max_length=7,
        choices=LinkTypeChoice.choices,
        default=LinkTypeChoice.book,
        blank=False,
        null=False,
    )
    image_url = models.URLField(
        blank=True,
        null=True,
    )
    link = models.URLField(
        blank=False,
        null=False,
    )

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    # PRICE DATA
    current_price = models.FloatField(default=0)
    old_price = models.FloatField(default=0)
    price_difference = models.FloatField(default=0)

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ['price_difference', '-created']

class Price(models.Model):
    link = models.ForeignKey(Link, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    price = models.FloatField()

    class Meta:
        ordering = ['price', 'created']

    def save(self, *args, **kwargs):
        price = super().save(*args, **kwargs)
        link = Link.objects.get(pk=price.link)
        
        current_price = price.price
        old_price = link.current_price

        if current_price != old_price:
            link.old_price = old_price
            link.current_price = current_price
            link.price_difference = current_price - old_price
            link.save()