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
    servicios = TipoServicio.objects.all()
    context = {'servicios': servicios }
    return render (request, 'mantenedor/reservas.html', context)



def orden_reparacion (request):
    return render (request, 'mantenedor/orden_reparacion.html')

def orden_pedido (request):
    return render (request, 'mantenedor/orden_pedido.html')


def crear_reserva(request):
    if request.method == 'POST':

        mi_fecha = request.POST['fecha']
        mi_hora = request.POST['hora']
        mi_servicio = request.POST['servicio']
        mi_descripcion = request.POST['descripcion']

     
        if mi_fecha != "":
            try:
              
                reserva = Reservas()

                id_reserva = Reservas.objects.count()+1
                reserva.fecha = mi_fecha
                reserva.hora = mi_hora
                print("\n"+mi_servicio)
                reserva.servicio = mi_servicio
                reserva.descripcion = mi_descripcion
    
                reserva = Reservas(id_reserva,mi_servicio,mi_fecha,mi_hora,1,mi_descripcion,5)

                reserva.save()    
                return render(request, 'mantenedor/mensaje_datos.html', {})

            except reserva.DoesNotExist:
                return render(request, 'mantenedor/mensaje_datos.html', {})