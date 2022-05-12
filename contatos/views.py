from django.shortcuts import redirect, render
from requests import request
from contatos.forms import ContatoForm, GrupoContatosForm

from contatos.models import Contato, GrupoContatos


def grupoContatos(request):
    grupo_contatos = GrupoContatos.objects.all()

    context = {
        'gruposContatos':  grupo_contatos
    }
    return render(request, 'contatos/grupoContatos.html', context)


def grupoContatos_add(request):
    form = GrupoContatosForm(request.POST or None)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('contato')
    context = {'form': form}
    return render(request, 'contatos/grupoContatos_add.html', context)


def grupoContatos_edit(request, grupoContatos_pk):
    grupoContatos = GrupoContatos.objects.get(pk=grupoContatos_pk)

    form = GrupoContatosForm(request.POST or None, instance=grupoContatos)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('grupoContatos')

    context = {
        'form': form,
        'grupoContatos': grupoContatos
    }
    return render(request, 'contatos/grupoContatos_edit.html', context)


def grupoContatos_delete(request, grupoContatos_pk):
    grupoContatos = GrupoContatos.objects.get(pk=grupoContatos_pk)
    grupoContatos.delete()

    return redirect('grupoContatos')


def contato(request):
    contatos_ordem_alfabetica = Contato.objects.all().order_by('nome')

    search = request.GET.get('search')

    if search:
        contatos_ordem_alfabetica = contatos_ordem_alfabetica.filter(
            nome__icontains=search)

    context = {
        'contatos': contatos_ordem_alfabetica
    }
    return render(request, 'contatos/contato.html', context)


def contato_add(request):
    form = ContatoForm(request.POST or None)  # tras o form
    if request.POST:
        if form.is_valid():  # se o formulario é valido
            form.save()  # salva num objeto na classe autor e no banco
            return redirect('contato')  # redireciona pra pagina inicial
    context = {'form': form}
    return render(request, 'contatos/contato_add.html', context)


def contato_edit(request, contato_pk):
    contato = Contato.objects.get(pk=contato_pk)

    form = ContatoForm(request.POST or None, instance=contato)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('contato')

    context = {
        'form': form,
        'contato': contato
    }
    return render(request, 'contatos/contato_edit.html', context)


def contato_delete(request, contato_pk):
    contato = Contato.objects.get(pk=contato_pk)
    contato.delete()

    return redirect('contato')


def grupo_contatos(request):
    return render(request, 'contatos/grupo_contatos.html')
