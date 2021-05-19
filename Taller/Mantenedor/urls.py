from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [

    path('index', views.index, name='index'),
    path('cliente', views.cliente, name='cliente'),
    path('agregar_cliente', views.agregar_cliente, name='agregar_cliente'),
    path('servicios', views.servicios, name='servicios'),
    path('crear_reserva', views.crear_reserva, name='crear_reserva'),
    path('reservas', views.reservas, name='reservas'),
    path('orden_reparacion', views.orden_reparacion, name='orden_reparacion'),
    path('orden_pedido', views.orden_pedido, name='orden_pedido'),
]