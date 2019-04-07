from django import forms
from .models import models
from detection.models import Sepsis,Query

class Sepsisform(forms.ModelForm):
    class Meta:
        model = Sepsis
        fields = '__all__'


class Query_form(forms.ModelForm):
    class Meta:
        model = Query
        fields = '__all__'
