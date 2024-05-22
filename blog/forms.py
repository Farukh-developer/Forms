from django import forms
from .models import Adminstrator, Students

class AdminstratorForm(forms.ModelForm):
    cource_title = forms.CharField(widget=forms.TextInput({"class": "form-control"}))
    descrition = forms.CharField(widget=forms.Textarea({"class": "form-control"}))
    instructo_name = forms.CharField(widget=forms.TextInput({"class": "form-control"}))
    start_date = forms.DateField(widget=forms.DateInput({"class": "form-control", "type": "date"}))
    end_date = forms.DateField(widget=forms.DateInput({"class": "form-control", "type": "date"}))
    price = forms.IntegerField(widget=forms.NumberInput({"class": "form-control"}))

    class Meta:
        model = Adminstrator
        fields = ['cource_title', 'descrition', 'instructo_name', 'start_date', 'end_date', 'price']


class Studentform(forms.ModelForm):

    name = forms.CharField(widget=forms.TextInput({"class": "form-control"}))
    email = forms.EmailField(widget=forms.EmailInput({"class": "form-control"}))
    homework= forms.EmailField(widget=forms.EmailInput({"class": "form-control"}))
    homework

    class Meta:
        model = Students
        fields = ['name', 'email', 'selected_cource', 'homework']