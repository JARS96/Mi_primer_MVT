from contextvars import Context
from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render

def saludo(request, nombre):
    return HttpResponse('Buenas, buenas '+ nombre)

def despedida(request):
    return HttpResponse('adios, adios')

def fecha_actual(request):
    fecha=datetime.now().date()
    mensaje= f'Hoy es {fecha}'
    return HttpResponse(mensaje)

def nacDate(request, edad):
  year=datetime.now()
  currentYear=year.year
  edadM=int(edad)
  fnac= (currentYear - edadM)
  return HttpResponse(f'Naci en: {fnac}')

def probando_template(request):
    context = {
        'nombre':'Aaron',
        'apellido':'Rodriguez'
        
    }
    return render(request, 'template1.html', context = context)


