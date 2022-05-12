from datetime import date
from pyexpat import model
from typing_extensions import Required
import django
from django.db import models


class GrupoContatos(models.Model):
    titulo = models.CharField(max_length=255, verbose_name="Título")
    descricao = models.CharField(max_length=255, verbose_name="Descrição")

    def __str__(self):
        return self.titulo


class Contato(models.Model):  # campos para a tabela

    data_criacao = date.today()

    nome = models.CharField(max_length=100)
    telefone = models.PositiveIntegerField()
    email = models.EmailField(max_length=100, verbose_name="E-mail")
    endereco = models.CharField(max_length=255, verbose_name="Endereço")
    numero = models.PositiveIntegerField(verbose_name="Número")
    bairro = models.CharField(max_length=100)
    cep = models.PositiveIntegerField(verbose_name="CEP")
    estado = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    grupoContato = models.ForeignKey(
        GrupoContatos, on_delete=models.CASCADE, related_name='contatos', verbose_name="Grupo do Contato")
    dataCadastro = models.DateField(
        default=django.utils.timezone.now, verbose_name="Data de cadastro")

    def __str__(self):
        return self.nome
