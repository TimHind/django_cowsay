from django import forms
from homepage.models import Cow

class CowSay(forms.Form):
    text = forms.CharField(max_length=80)