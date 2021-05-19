from django.shortcuts import render
from .models import *


# Create your views here.



def index (request):
    context={}
    return render (request, 'mantenedor/index.html',context)


def cliente (request):
    context={}
    return render (request, 'mantenedor/cliente.html',context)




def agregar_cliente(request):
    if request.method == 'POST':

        mi_rut = request.POST['rut']
        mi_nombre = request.POST['nombre']
        mi_apellido = request.POST['apellido']
        mi_direccion = request.POST['direccion']
        mi_telefono = request.POST['telefono']
        mi_celular = request.POST['celular']
        mi_email = request.POST['email']
        mi_password = request.POST['password']
     
        if mi_rut != "":
            try:
                print("Entrando al try")
                cliente = Cliente()

                id_cliente = Cliente.objects.count()+1
                cliente.rut = mi_rut
                cliente.nombre = mi_nombre
                cliente.apellido = mi_apellido
                cliente.direccion = mi_direccion
                cliente.telefono = mi_telefono
                cliente.celular = mi_celular
                cliente.email = mi_email
                cliente.password = mi_password
               
                
                print(vars(cliente))
                cliente = Cliente(id_cliente,mi_rut,mi_nombre,mi_apellido,mi_direccion,
                                    mi_telefono,mi_celular,mi_email,mi_password)

                cliente.save()
                
                return render(request, 'mantenedor/mensaje_datos.html', {})

            except cliente.DoesNotExist:
                return render(request, 'mantenedor/mensaje_datos.html', {})

def servicios (request):
    return render (request, 'mantenedor/servicios.html')

def reservas (request):
    return render (request, 'mantenedor/reservas.html')

def orden_reparacion (request):
    return render (request, 'mantenedor/orden_reparacion.html')