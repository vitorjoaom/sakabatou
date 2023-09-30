from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from apps.contato.models import Contato
from apps.contato.forms import ContatoForms

def index(requisicao):
    dados = Contato.objects.all()
    return render(requisicao, 'index.html', {"contatos": dados})

def view(request):
    form = ContatoForms()

    if request.method == 'POST':
        form = ContatoForms(request.POST)

        if form.is_valid():
            nome_form = form.cleaned_data['nome'].value = contato.nome
            fone_form = form.cleaned_data['fone'].value = contato.fone

            contato = Contato(nome=nome_form, fone=fone_form)
            contato.save()

            return redirect('index')

    return render(request, 'form.html', {"form": form})

def editar(requisicao, id):
    
    contato = get_object_or_404(Contato, pk=id)

    if requisicao.method == 'GET':
        form = ContatoForms(initial={'nome':contato.nome, 'fone':contato.fone})
    elif requisicao.method == 'POST':
        form = ContatoForms(requisicao.POST)
        if form.is_valid():
            contato.nome = form.cleaned_data['nome']
            contato.fone = form.cleaned_data['fone']
            contato.save()
            return redirect('index')   
    return render(requisicao, "edit.html",{"form":form, "id":id})