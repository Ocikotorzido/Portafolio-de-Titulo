from .models import *
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as iniciarSesion, logout, authenticate

import rut_chile

def to_index(request):
    """Redirección hacia index"""
    return redirect('index')

def login(request):
    """Módulo que permite al usuario registrarse e/o iniciar sesión."""    

    # Si el usuario ya está loggeado,
    # Se redirecciona al index.
    if request.user.is_authenticated:
        return redirect('index')

    if request.method == 'POST':
        # Se rescatan los campos de usuario y contraseña.
        only_numbers = lambda texto: ''.join([numero if numero in ['0','1','2','3','4','5','6','7','8','9'] else '' for numero in texto])
        usuario = only_numbers(request.POST['username'])
        contra = request.POST['password']

        # Se verifica que las crenciales sean válidas.
        usuarioLogeado = authenticate(username = usuario, password = contra)

        # Debiera devolver una instancia de sesión.
        # De lo contrario, devuelve 'None'.
        if usuarioLogeado is not None:

            # La función login() iniciará la sesión.
            iniciarSesion(request, usuarioLogeado)

            # Si la autenticación es correcta, 
            # entonces la plantilla se renderizará
            # como un usuario válidamente autenticado.
            return redirect('index')
        
        # Si la autenticación falla, 
        # la sesión NO existirá.
        else:
            # Se verifica que exista el nombre de usuario en la base de datos.
            if len(User.objects.filter(username=usuario)):
                # Si existe, se le informa al usuario que la contraseña es incorrecta.
                return render(request, 'mantenedor/login.html', {'errores':'CONTRASEÑA_INCORRECTA'})
            else:
                # Si no existe, se le informa al usuario que el nombre de usuario no existe.
                return render(request, 'mantenedor/login.html', {'errores':'NO_EXISTE_NOMBRE_USUARIO'})

    # Página de inicio de sesión.
    return render(request, 'mantenedor/login.html')

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
    return redirect('index')

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

        dato_or_zero = lambda dato_crudo: 0 if not dato_crudo else dato_crudo
        only_numbers = lambda texto: ''.join([numero if numero in ['0','1','2','3','4','5','6','7','8','9'] else '' for numero in texto])

        mi_rut = only_numbers(formulario.cleaned_data['username'])
        mi_nombre = request.POST['first_name']
        mi_apellido = request.POST['last_name']
        mi_direccion = request.POST['direccion']
        mi_telefono = dato_or_zero(request.POST['telefono'])
        mi_celular = dato_or_zero(request.POST['celular'])
        mi_email = request.POST['email']

        id_user_auth = User.objects.get(username=formulario.cleaned_data['username']).id
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
        return render(request, 'Mantenedor/index.html', {'perfil':{'nivel':nivel}})
    context['formulario'] = formulario
    return render (request, 'mantenedor/registro_cliente.html',context)

def servicios (request):
    return render (request, 'mantenedor/servicios.html')

def reservas (request):
    servicios = TipoServicio.objects.all()
    context = {'servicios': servicios }
    return render (request, 'mantenedor/reservas.html', context)

def orden_reparacion (request):
    reservas = Reservas.objects.all()
    context = {'reservas': reservas}

    return render (request, 'mantenedor/orden_reparacion.html', context)

def orden_pedido (request):
    return render (request, 'mantenedor/orden_pedido.html')

def registrar_proveedor(request):
    return render (request, 'mantenedor/registro_proveedor.html')

def registro_vehiculo(request):
    return render (request, 'mantenedor/registro_vehiculo.html')

def presupuesto(request):
    return render (request, 'mantenedor/presupuesto.html')


def crear_reserva(request):
    if request.method == 'POST':

        mi_fecha = request.POST['fecha']
        mi_hora = request.POST['hora']
        mi_servicio = request.POST['servicio']
        mi_descripcion = request.POST['descripcion']
     
        if mi_fecha != "":
              
                reserva = Reservas()

                id_reserva = Reservas.objects.count()+1
                reserva.fecha = mi_fecha
                reserva.hora = mi_hora
               
                reserva.servicio = mi_servicio
                reserva.descripcion = mi_descripcion
    
                reserva = Reservas(id_reserva,mi_servicio,mi_fecha,mi_hora,1,mi_descripcion,1)

                reserva.save()    
                return render(request, 'mantenedor/reservas.html',)

           

def empleado (request):
    cargos = Cargo.objects.all()
    context = {'cargos': cargos }
    return render(request,'mantenedor/registro_empleado.html',context)

def exportar(request):
    context = {'a':'a'}
    return render(request,'mantenedor/exportar.html',context)

def agregar_empleado(request):
    if request.method == 'POST':
        mi_cargo = request.POST['cargo']
        mi_rut = request.POST['rut']
        mi_nombre = request.POST['nombre']
        mi_apellido = request.POST['apellido']
        mi_contacto = request.POST['contacto']
        mi_password = request.POST['password']

        empleado = Empleado()
        id_empleado = Empleado.objects.count()+1
        empleado.rut = mi_rut
        empleado.nombre = mi_nombre
        empleado.apellido = mi_apellido
        empleado.contacto = mi_contacto
        
        # Creación del empleado en la tabla 'auth_user'.
        nuevo_empleado = User.objects.create_user(mi_rut,mi_contacto,mi_password) 
        nuevo_empleado.save()

        # Búsqueda del número de identidad.
        id_user_auth = User.objects.get(username=mi_rut).id

        # Creación de empleado en la tabla 'perfil'.
        n_perfil = Perfil.objects.all().count()+1
        perfil = Perfil(n_perfil,id_user_auth, id_empleado, 'EMPLEADO')
        perfil.save()
        
        # Creación de un nuevo empleado.
        empleado = Empleado(id_empleado,
        mi_nombre,
        mi_apellido,mi_contacto,mi_cargo,mi_rut)
        empleado.save()
        return render(request, 'mantenedor/registro_empleado.html', {'mensaje':'Empleado_registrado'})

def generar_informe(request, informe_de, parametros, tipo):
    return HttpResponse('http://localhost:8000/static/img/logo-1.png')
    return HttpResponse(f'/static/{informe_de}_{parametros}.{tipo}')