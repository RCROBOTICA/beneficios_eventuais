from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from app.forms import RegistroForm
from app.models import Registro





# Create your views here.
def home(request):
    data = {}
    search = request.GET.get('search')
    if search:
        data['db'] = Registro.objects.filter(n_do_protocolo__icontains=search)
    else:
        data['db'] = Registro.objects.all()
    return render(request, 'index.html', data)

# def home_2(request):
#     data = {}
#     data['db'] = Produtos.objects.all()
#     return render(request, 'index_2.html', data)

def form(request):
     data = {}
     data['form'] = RegistroForm()
     return render(request, 'form.html', data)


def salvarCli(request):
     form = RegistroForm(request.POST or None)
     if form.is_valid():
          form.save()
     return redirect('/')

def view(request, pk):
    data = {}
    data['db'] = Registro.objects.get(pk=pk)
    return render(request, 'view.html', data)


def edit(request, pk):
    data = {}
    data['db'] = Registro.objects.get(pk=pk)
    data['form'] = RegistroForm(instance=data['db'])
    return render(request, 'form.html', data)

def update(request, pk):
    data = {}
    data['db'] = Registro.objects.get(pk=pk)
    form = RegistroForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
    return redirect('/')

def delete(request, pk):
    db = Registro.objects.get(pk=pk)
    db.delete()
    return redirect('home')












from django.shortcuts import render

# Create your views here.
