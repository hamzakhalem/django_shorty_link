import random 
import string 
from django.conf import settings


SHORTCODE_MIN = getattr(settings, "SHORTCODE_MIN", 6)
def code_gen(size=SHORTCODE_MIN, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for  _ in range(size))

def create_shortcode(instance, size=SHORTCODE_MIN):
    new_code = code_gen(size=size)
    shorty = instance.__class__
    qs_exist = shorty.objects.filter(shotcode=new_code).exists()
    if qs_exist: 
        return create_shortcode(instance, size)
    else:
        return new_code