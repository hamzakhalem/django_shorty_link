from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views import View
from .models import ShortyUrl
# Create your views here.
def shorty_redirect(request, slug):
    shortcodeurl = get_object_or_404(ShortyUrl, shotcode=slug )
    print(shortcodeurl)
    print('________________')
    return redirect(shortcodeurl.url)

class ShortyCBView(View):
    def get(self, request, slug):
        return HttpResponse("hello from view")

