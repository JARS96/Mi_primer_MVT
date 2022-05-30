"""proyecto_1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from proyecto_1.views import saludo, despedida, fecha_actual, nacDate, probando_template  #esta linea importa el view de las views del proyecto
from Familiares.views import familiares
urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo/<nombre>/', saludo, name='saludo'), #esta linea define el url de la view que importamos
    path('despedida/', despedida, name='despedida'),
    path('fecha_actual/', fecha_actual, name='fecha_actual'),
    path('nacDate/<edad>/', nacDate, name='nacDate' ),
    path('probando_template/', probando_template, name='probando_template'),
    path('familiares/', familiares, name='familiares')
]
