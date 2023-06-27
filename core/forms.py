from django import forms
from .models import Pessoa

class MeuFormulario(forms.ModelForm):
    class Meta:
        model = Pessoa
        fields = ['nome', 'sobrenome', 'email', 'data_nascimento']
