from django.shortcuts import render, redirect
from django.http import HttpResponse
from Home.forms import CreacionZapatos
from Home.models import Zapato

def inicio(request):
    #return HttpResponse('<h1>Hola</h1>')
    return render(request,'Home/inicio.html')

def crear_zapatos(request):
    print("Datos de GET: ")
    print("Datos de POST:")
    if request.method=='POST':
        formulario=CreacionZapatos(request.POST)
        if formulario.is_valid():
            info=formulario.cleaned_data
            zapato = Zapato(
                marca=info['marca'],
                modelo=info['modelo'],
                talla=info['talla'],  # Ahora es obligatorio
                color=info.get('color', 'sin color'), fecha_creacion=info.get('fecha_creacion', None)
                
                )
            zapato.save()
            return redirect ('lista_zapatos')
    else:
        formulario = CreacionZapatos    

    return render(request, 'Home/crear_zapatos.html',{'formulario':formulario})

def lista_zapatos(request):
    zapatos= Zapato.objects.all()
    return render(request, 'Home/lista_zapatos.html', {'zapatos':zapatos})