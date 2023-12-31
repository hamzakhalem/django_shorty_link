from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views import View
from .models import ShortyUrl
from .forms import shortenForm

# Create your views here.
def shorty_redirect(request, slug):
    shortcodeurl = get_object_or_404(ShortyUrl, shotcode=slug )
    print(shortcodeurl)
    print('________________')
    return redirect(shortcodeurl.url)

class ShortyCBView(View):
    def get(self, request, slug):
        
        return HttpResponse("hello from view")
    
class HomeView(View):
    def get(self, request, *args, **kwargs):
        form = shortenForm()
        return render(request, 'home.html', {'form':form})
    def post(self, request, *args, **kwargs):
        print(request.POST['url'])
        form = shortenForm(request.POST)
        if(form.is_valid()):
            new_url = form.cleaned_data.get('url')
            obj, created = ShortyUrl.objects.get_or_create(url=new_url)
            dec = {
                    "object": obj,
                    "created": created
                }
            if created:
                return render(request, 'sucess.html', dec)
            else:
                return render(request, 'already_exist.html', dec)
        

