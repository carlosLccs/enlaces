from django.shortcuts import render, redirect, get_object_or_404

from .forms import EnlaceForm
from .models import Enlace



def home(request):
    enlaces = Enlace.objects.all()
    return render(request, 'linkapp/home.html', {'enlaces':enlaces})
    
    
    

def agregar(request):
    if request.method=='POST':
        form = EnlaceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = EnlaceForm()        
    return render(request, 'linkapp/agregar.html', {'form':form})

def editar(request, pk):
    enlace = Enlace.objects.get(id=pk)
    form = EnlaceForm(instance=enlace)
    if request.method=='GET':
       form = EnlaceForm(instance=enlace)
    else:   
        form = EnlaceForm(request.POST, instance=enlace)
        if form.is_valid():
           form.save()
           return redirect('/')
        

    return render(request, 'linkapp/editar.html', {'form':form})

def eliminar(request, pk):
    enlace = Enlace.objects.get(id=pk)
    enlace.delete()
    return redirect('/')



        

