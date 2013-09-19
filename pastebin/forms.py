from django import forms
from django.utils import timezone
from pastebin.models import Paste


class PasteForm(forms.ModelForm):
    class Meta:
        model = Paste
        fields = ['title', 'text']
