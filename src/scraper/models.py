from django.db import models

class LinkTypeChoice(models.TextChoices):
    book = 'book'
    kindle_book = 'kindle'
    generic = 'generic'

class LinkSituationChoice(models.TextChoices):
    pending = 'pending'
    calculed = 'calculed'


class Link(models.Model):
    name = models.CharField(
        max_length=220, 
        blank=True, 
        null=True
        )
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
    situation = models.CharField(
        max_length=8,
        choices=LinkSituationChoice.choices,
        default=LinkSituationChoice.pending,
    )

    # PRICE DATA
    current_price = models.FloatField(default=0) # set decimal places
    old_price = models.FloatField(default=0) # set decimal places
    price_difference = models.FloatField(default=0) # set decimal places

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
        link = Link.objects.get(pk=self.link.id)
        
        current_price = self.price
        old_price = link.current_price

        if current_price != old_price:
            link.old_price = old_price
            link.current_price = current_price
            link.price_difference = round(current_price - old_price, 2)
            link.save()

        super().save(*args, **kwargs)