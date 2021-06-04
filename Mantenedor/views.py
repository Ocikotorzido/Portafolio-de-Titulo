from .models import *
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as iniciarSesion, logout, authenticate

import rut_chile

def to_index(request):
    """Redirección hacia index"""
    return redirect('index')

def login (request):
    """Inicio de sesión
    Argumentos:
        request: petición hecha por el cliente hacia el servidor.
    Retorna:
        render(): Si los datos ingresados son válidos, 
        retornará a la sesión del usuario, de lo contrario,
        retornará la misma página indicando los errores.
    """
    formulario = None
    if request.method =='POST':
        formulario = AuthenticationForm(data = request.POST)
        if formulario.is_valid():
            usuario = formulario.cleaned_data['username']
            contra = formulario.cleaned_data['password']
            usuarioLogueado = authenticate(username = usuario, password = contra)

            if usuarioLogueado is not None:
                iniciarSesion(request, usuarioLogueado)
                nivel = None
                if request.user.is_authenticated:
                    nivel = Perfil.objects.filter(id_auth_user = request.user.id)[0].nivel
                context={'perfil':{'nivel':nivel}, 'nivel':nivel}
                return render(request, 'TEMPORAL/perfil.html', context)
    else:
        formulario = AuthenticationForm()
    context = {
        'formulario':formulario
    }
    return render(
        request,
        'TEMPORAL/login.html',
        context
    )

def registro (request):
    formulario = None
    if request.method == 'POST':
        formulario = FormularioRegistro(data = request.POST)
        # try:
        #     if not rut_chile.is_valid_rut(formulario['username']):
        #         return render(request, 'Mantenedor/registro.html', {formulario:formulario, 'errores':'rut mal ingresado'})
        # except ValueError:
        #     return render(request, 'Mantenedor/registro.html', {formulario:formulario, 'errores':'rut mal ingresado'})
        if formulario.is_valid():
            usuario_guardado = formulario.save()
            if usuario_guardado is not None:
                iniciarSesion(request,usuario_guardado)
                context = {'perfil':
                            {'nivel':'admin'},
                            'level':'admin'
                            }
                return render(request, 'TEMPORAL/perfil.html', context)                
    else:
        formulario = FormularioRegistro()

    context = {'formulario': formulario}
    return render(request, 'TEMPORAL/registro.html', context)

def perfil(request):
    return render(
        request,
        'TEMPORAL/perfil.html'
    )

def salir(request):
    logout(request)
    return redirect('/TEMPORAL/login')

def index (request):
    nivel = None
    if request.user.is_authenticated:
        nivel = Perfil.objects.filter(id_auth_user = request.user.id)[0].nivel
    context={'perfil':{'nivel':nivel}}
    return render (request, 'mantenedor/index.html',context)


def registro_cliente (request):
    formulario = FormularioRegistro()
    context = dict()
    permitir_sesion = False
    if request.method == 'POST':
        formulario = FormularioRegistro(data = request.POST)
        if formulario.is_valid():
            usuario_guardado = formulario.save()
            if usuario_guardado is not None:
                permitir_sesion = True
        else:
            context['formulario'] = formulario
            return render (request, 'mantenedor/registro_cliente.html',context)

        mi_rut = formulario.cleaned_data['username']
        mi_nombre = request.POST['first_name']
        mi_apellido = request.POST['last_name']
        mi_direccion = request.POST['direccion']
        mi_telefono = request.POST['telefono']
        mi_celular = request.POST['celular']
        mi_email = request.POST['email']

        id_user_auth = User.objects.get(username=mi_rut).id
        id_cliente = Cliente.objects.count()+1
        cliente = Cliente(id_cliente,mi_nombre,mi_apellido,mi_direccion,
                            mi_telefono,mi_celular,mi_email,mi_rut)

        n_perfil = Perfil.objects.all().count()+1
        perfil = Perfil(n_perfil,id_user_auth, id_cliente,'CLIENTE')
        perfil.save()

        cliente.save()
        if permitir_sesion:
            iniciarSesion(request,usuario_guardado)
            nivel = Perfil.objects.filter(id_auth_user = request.user.id)[0].nivel
        return render(request, 'TEMPORAL/index.html', {'perfil':{'nivel':nivel}})
    context['formulario'] = formulario
    return render (request, 'mantenedor/registro_cliente.html',context)

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

def empleado (request):
    cargos = Cargo.objects.all()
    context = {'cargos': cargos }
    return render(request,'mantenedor/registro_empleado.html',context)


def agregar_empleado(request):
    if request.method == 'POST':

        mi_rut = request.POST['rut']
        mi_nombre = request.POST['nombre']
        mi_apellido = request.POST['apellido']
        mi_cargo = request.POST['cargo']
        mi_contacto = request.POST['contacto']
     
        if mi_rut != "":
            try:
                empleado = Empleado()

                id_empleado = Empleado.objects.count()+1
                empleado.rut = mi_rut
                empleado.nombre = mi_nombre
                empleado.apellido = mi_apellido
                empleado.contacto = mi_contacto
                
                #User.objects.create_user(mi_rut,mi_contacto,mi_password) 

                # n_perfil = Perfil.objects.all().count()+1
                # perfil = Perfil(n_perfil,1)
                # perfil.save()
                # id_usuario = UserPerfil.objects.count()+1
                # UserPerfil(id_usuario).save()
                
                empleado = Empleado(id_empleado,mi_nombre,mi_apellido,mi_contacto,mi_cargo,
                                    mi_rut,mi_password)

                empleado.save()
                
                return render(request, 'mantenedor/mensaje_datos.html', {})

            except empleado.DoesNotExist:
                return render(request, 'mantenedor/mensaje_datos.html', {})