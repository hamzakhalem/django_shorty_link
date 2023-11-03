from django.db import models
from .utils import create_shortcode
# Create your models here.
class ShortyUrl(models.Model):
    url = models.CharField( max_length=250)
    shotcode = models.CharField(unique=True, max_length=15)
    updated_time = models.DateTimeField(auto_now=True, null= True)
    timstamp = models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return self.url
    
    def save(self, *args, **kwargs):
        if self.shotcode is None or self.shotcode == '':
            self.shotcode = create_shortcode()
        super(ShortyUrl, self).save(*args, **kwargs)

