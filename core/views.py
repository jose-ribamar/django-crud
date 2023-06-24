from django.shortcuts import render, redirect
from .models import Pessoa

def home(request):
    pessoas = Pessoa.objects.all()
    return render(request, "index.html", {"pessoas": pessoas})

def salvar(request):
    if request.method == 'POST':
        nome = request.POST.get("nome")
        sobrenome = request.POST.get("sobrenome")
        email = request.POST.get("email")
        data_nascimento = request.POST.get("data_nascimento")
        
        pessoa = Pessoa.objects.create(nome=nome, sobrenome=sobrenome, email=email, data_nascimento=data_nascimento)
        
        return redirect('home')
    
    return render(request, "index.html")

def editar(request, id):
    pessoa = Pessoa.objects.get(id=id)
    
    if request.method == 'POST':
        pessoa.nome = request.POST.get("nome")
        pessoa.sobrenome = request.POST.get("sobrenome")
        pessoa.email = request.POST.get("email")
        pessoa.data_nascimento = request.POST.get("data_nascimento")
        pessoa.save()
        return redirect('home')
    
    return render(request, "update.html", {"pessoa": pessoa})

def delete(request, id):
    pessoa = Pessoa.objects.get(id=id)
    pessoa.delete()
    return redirect('home')

def pesquisar(request):
    if request.method == 'GET':
        termo_pesquisa = request.GET.get("search_query")
        resultados = Pessoa.objects.filter(nome__icontains=termo_pesquisa)
        return render(request, "index.html", {"pessoas": resultados})
    
    return redirect('home')
