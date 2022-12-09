from django.contrib import admin

from .models import Link, Price

@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    pass

@admin.register(Price)
class PriceAdmin(admin.ModelAdmin):
    pass