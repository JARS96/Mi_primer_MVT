from django.shortcuts import render
from Familiares.models import Familiares


# Create your views here.
def familiares(request):
    familiar_nuevo=Familiares.objects.create(name='Dani', age=20, date='2002-04-03' )
    context={'familiar_nuevo':familiar_nuevo}
    return render(request, 'familiares.html', context=context)
