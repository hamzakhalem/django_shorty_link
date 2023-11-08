from django import forms
 
class shortenForm(forms.Form):
    url = forms.CharField( max_length=200, required=False, label="URL:")