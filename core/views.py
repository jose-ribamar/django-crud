from django.shortcuts import render
from .models import Pessoa

def home(request):
    pessoas = Pessoa.objects.all()
    return render(request, "index.html", {"pessoas": pessoas})

def salvar(request):
    nome = request.POST.get("nome")
    sobrenome = request.POST.get("sobrenome")
    email = request.POST.get("email")
    data_nascimento = request.POST.get("data_nascimento")
    
    pessoa = Pessoa.objects.create(nome=nome, sobrenome=sobrenome, email=email, data_nascimento=data_nascimento)
    
    pessoas = Pessoa.objects.all()
    return render(request, "index.html", {"pessoas": pessoas})
