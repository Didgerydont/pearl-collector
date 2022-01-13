from django.contrib import admin

# Register your models here.

from .models import Pearls

@admin.register(Pearls)
class PearlsAdmin(admin.ModelAdmin):
    list_display = ("title", "list", "pub_date")