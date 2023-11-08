from typing import Any
from django import forms
 
class shortenForm(forms.Form):
    url = forms.CharField( max_length=200, required=False, label="URL:")

    def clean(self):
        cleaned_data = super(shortenForm, self).clean()
        url = cleaned_data['url']
        print(url)
    
    def clean_url(self):
        url = self.cleaned_data['url']
        print(url)
        return url