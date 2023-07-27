from django.contrib import admin
from django.urls import path

from control_estudios.views import listar_estudiantes

#son las urls especificas de la app 

urlpatterns = [
    path("estudiantes/", listar_estudiantes),
] 