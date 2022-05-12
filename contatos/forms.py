from faulthandler import disable
from attr import field
from django import forms

from contatos.models import Contato, GrupoContatos


class GrupoContatosForm(forms.ModelForm):
    class Meta:
        model = GrupoContatos
        exclude = ()

        widgets = {
            'titulo': forms.TextInput(attrs={'id': 'input-nome'}),
            'descricao': forms.TextInput(attrs={'id': 'input-nome'}),
        }


class ContatoForm(forms.ModelForm):
    class Meta:
        model = Contato
        exclude = ['dataCadastro']

        widgets = {
            'nome': forms.TextInput(attrs={'id': 'input-nome', 'autofocus': ''}),
            'telefone': forms.NumberInput(attrs={'id': 'input-nome'}),
            'email': forms.EmailInput(attrs={'id': 'input-email'}),
            'endereco': forms.TextInput(attrs={'id': 'input-endereco'}),
            'numero': forms.NumberInput(attrs={'id': 'input-numero'}),
            'bairro': forms.TextInput(attrs={'id': 'input-bairro'}),
            'cep': forms.NumberInput(attrs={'id': 'input-cep'}),
            'estado': forms.TextInput(attrs={'id': 'input-estado'}),
            'cidade': forms.TextInput(attrs={'id': 'input-cidade'}),
            'grupoCliente': forms.NumberInput(attrs={'id': 'input-numero'}),
        }
