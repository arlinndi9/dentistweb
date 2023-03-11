from django import forms
from dentist.models import Contact,Rezervo,Pricing

class ContactForm(forms.ModelForm):
    class Meta:
        model=Contact
        fields="__all__"

class Rezervo(forms.ModelForm):
    class Meta:
        model=Rezervo
        fields="__all__"

class Pricing(forms.ModelForm):
    class Meta:
        model=Pricing
        fields="__all__"