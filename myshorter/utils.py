import random 
import string 

def code_gen(size=6, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for  _ in range(size))

def create_shortcode(instance, size=6):
    new_code = code_gen(size=size)
    shorty = instance.__class__
    qs_exist = shorty.obejcts.filter(shotcode=new_code).exists()
    if qs_exist: 
        return create_shortcode(instance, size)
    else:
        return new_code