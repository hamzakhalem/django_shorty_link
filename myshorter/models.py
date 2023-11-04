from django.db import models
from .utils import create_shortcode
# Create your models here.

class shortyUrlManger(models.Manager):
    def all(self, *args, **kwargs):
        qs = super(shortyUrlManger, self).all(*args, **kwargs)
        qs = qs.filter(active=True)
        return qs
    def refresh_shortcodes(self, items=None):
        print(items)
        qs = ShortyUrl.objects.filter(id__gte=1)
        new_code = 0
        if items is not None and isinstance(items, int):
            qs = qs.order_by('-id')[:items]
        for q in qs:
            q.shotcode = create_shortcode(q)
            print(q.id)
            q.save()
            new_code +=1 
        return "new code: " + str(new_code)
class ShortyUrl(models.Model):
    url = models.CharField( max_length=250)
    shotcode = models.CharField(unique=True, max_length=15)
    updated_time = models.DateTimeField(auto_now=True, null= True)
    timstamp = models.DateTimeField(auto_now_add=True, null=True)
    acrive  = models.BooleanField(default=True)
    objects = shortyUrlManger()
    some_random = shortyUrlManger()
    def __str__(self):
        return self.url
    
    def save(self, *args, **kwargs):
        if self.shotcode is None or self.shotcode == '':
            self.shotcode = create_shortcode()
        super(ShortyUrl, self).save(*args, **kwargs)

