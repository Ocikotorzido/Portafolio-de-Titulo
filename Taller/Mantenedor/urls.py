from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [

    path('index', views.index, name='index'),
    path('cliente', views.cliente, name='cliente'),
    path('agregar_cliente', views.agregar_cliente, name='agregar_cliente'),
    path('servicios', views.servicios, name='servicios'),
    path('reservas', views.reservas, name='reservas'),
    path('orden_reparacion', views.orden_reparacion, name='orden_reparacion'),
]