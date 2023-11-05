from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
# Create your views here.
def shorty_redirect(request, *args, **kwargs):
    return HttpResponse('hello')

class ShortyCBView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("hello from view")