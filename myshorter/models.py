from django.db import models
import random 
import string 
def code_gen(size=6, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for  _ in range(size))
# Create your models here.
class ShortyUrl(models.Model):
    url = models.CharField( max_length=250)
    shotcode = models.CharField(unique=True, max_length=15)
    updated_time = models.DateTimeField(auto_now=True, null= True)
    timstamp = models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return self.url
    
    def save(self, *args, **kwargs):
        self.shotcode = code_gen()
        print(self.shotcode)
        super(ShortyUrl, self).save(*args, **kwargs)

