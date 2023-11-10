from django.db import models
from myshorter.models import ShortyUrl
# Create your models here.
class ClickEventManager(models.Manager):
    def create_event(self, instance):
        if isinstance(ShortyUrl, instance):
            obj, created= self.objects.get_or_create(url_shorty=instance)
            obj.count += 1
            obj.save()
            return obj.count
        return None
class ClickEvent(models.Model):
    url_shorty = models.ForeignKey(ShortyUrl, on_delete=models.CASCADE)
    count = models.IntegerField(default=0)
    updated_time = models.DateTimeField(auto_now=True, null= True)
    timstamp = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return "{i}".format(self.count)