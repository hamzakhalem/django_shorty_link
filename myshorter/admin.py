from django.contrib import admin
from .models import ShortyUrl
# Register your models here.
class ShortyUrlAdmin(admin.ModelAdmin):
    list_display = ['id', 'url']
     
admin.site.register(ShortyUrl, ShortyUrlAdmin)