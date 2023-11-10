from django.db import models
from myshorter.models import ShortyUrl
# Create your models here.
class ClickEvent(models.Model):
    url_shorty = models.ForeignKey(ShortyUrl, on_delete=models.CASCADE)