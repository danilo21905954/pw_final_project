from django import forms
from django.forms import ModelForm, NumberInput
from .models import *


class ContatoForm(ModelForm):
    class Meta:
        model = Contato
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': "form-control"}),
            'birth': NumberInput(attrs={'type': 'date', 'class': "form-control"}),
            'phone': forms.TextInput(attrs={'class': "form-control"}),
            'email': forms.TextInput(attrs={'class': "form-control"}),
            'plano': forms.Select(attrs={'class': "form-control"}),
        }


class PlanoForm(ModelForm):
    class Meta:
        model = Plano
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': "form-control"}),
            'index': NumberInput(attrs={'class': "form-control"}),
            'upload': forms.TextInput(attrs={'class': "form-control"}),
            'download': forms.TextInput(attrs={'class': "form-control"}),
            'roteador': forms.TextInput(attrs={'class': "form-control"}),
            'price': forms.TextInput(attrs={'class': "form-control"}),
            'icon': forms.TextInput(attrs={'class': "form-control"}),
            'image_name': forms.TextInput(attrs={'class': "form-control"}),
        }


class TestemunhoForm(ModelForm):
    class Meta:
        model = Testemunho
        fields = 'name', 'apelido', 'testemunho', 'voto'
        widgets = {
            'name': forms.TextInput(),
            'apelido': forms.TextInput(),
            'testemunho': forms.Textarea(attrs={'id': "text_area"}),
            'voto': forms.Select(choices=Testemunho.ESTRELAS, attrs={'class': "form-control"}),
        }


class TestemunhoAdminForm(ModelForm):
    class Meta:
        model = Testemunho
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': "form-control"}),
            'apelido': forms.TextInput(attrs={'class': "form-control"}),
            'testemunho': forms.Textarea(attrs={'class': "form-control"}),
            'voto': forms.Select(choices=Testemunho.ESTRELAS, attrs={'class': "form-control"}),
        }
