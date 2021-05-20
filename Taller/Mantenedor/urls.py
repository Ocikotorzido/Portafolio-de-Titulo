from django.contrib import admin
from django.urls import path, include
from . import views
from .views import login, registro, perfil, salir



urlpatterns = [

    path('index', views.index, name='index'),
    path('cliente', views.cliente, name='cliente'),
    path('agregar_cliente', views.agregar_cliente, name='agregar_cliente'),
    path('servicios', views.servicios, name='servicios'),
    path('crear_reserva', views.crear_reserva, name='crear_reserva'),
    path('reservas', views.reservas, name='reservas'),
    path('orden_reparacion', views.orden_reparacion, name='orden_reparacion'),
    path('orden_pedido', views.orden_pedido, name='orden_pedido'),

    path('empleado',views.empleado, name='empleado'),
    path('agregar_empleado', views.agregar_empleado, name='agregar_empleado'),
    # path('login', views.login, name='login'),

    path('login/', login, name='login'),
    path('registro/', registro, name='registro'),
    path('perfil/',perfil, name='perfil'),
    path('salir/',salir, name='salir')

]