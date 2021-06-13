import csv
import datetime
import os, os.path

import docx
import pandas
import docx2pdf
import rut_chile
from .models import *
from django.http import HttpResponse
from django.http import FileResponse
from django.utils.encoding import smart_str
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.template.defaultfilters import date
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import get_language, activate
from django.contrib.auth import login as iniciarSesion, logout, authenticate

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
    """Generar informes sobre algun/a persona/objeto.
    informe_de -> Tipo de informe, 
        puede ser: empleado, cliente, 
        administrador, vehículo, etc.
    parametros -> Valores/restricciones del informe,
        puede ser: Todo, último mes,
        última semana, último año,
        o incluso descartados.
    tipo -> formato de salida del informe,
        puede ser: excel, pdf, csv, word.
        
        El flujo de datos va de CSV a XLSX, 
        luego pasa a Docx y finalmente se 
        convierte en PDF, previo es obligado.
    """
    # Abreviación, extensión y 'content-type' de archivos y sus formatos.
    tipos_admitidos = {
        'csv': 
            ['csv', 'text/csv'],
        'excel': 
            ['xlsx','application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'],
        'word': 
            ['docx',' application/vnd.openxmlformats-officedocument.wordprocessingml.document'],
        'pdf': 
            ['pdf', 'application/pdf'],
        }
    
    # Se activa la traducción de fechas a español.
    activate('es')
    
    # Obtenemos el nombre del mes en español.
    today = datetime.date.today()
    mes = date(today, 'F')
    
    now = datetime.datetime.now().strftime('%Y-%m-%d__%H_%M_%S')
    now_ = datetime.datetime.now().strftime(f'%d de {mes} de %Y, %H:%M %p')
    
    # Se normaliza el dato.
    tipo = tipo.lower()
    
    # Validación de formato.
    if tipo not in ['csv', 'excel', 'word', 'pdf']:
        return HttpResponse('ERROR, el tipo de formato no es válido!')
    
    # Se define el nombre del archivo.
    nombre_archivo = f'informe_{informe_de}_{now}'
    nombre_archivo_con_extension = f'informe_{informe_de}_{now}.{tipos_admitidos[tipo][0]}'
    
    # Se define el tipo de respuesta y la cabecera.
    response = HttpResponse(
        content_type=f'{tipos_admitidos[tipo][1]}',
        headers={'Content-Disposition': 
            f'attachment; filename="{nombre_archivo_con_extension}"'},
    )
    
    # Obtener los títulos de una tabla.
    fields = Perfil._meta.get_fields()
    titulos = list()
    for titulo in fields:
        titulos.append(titulo.name)
    
    writer = csv.writer(response)
    writer.writerow(titulos)
    
    nombre_campos = Perfil._meta.get_fields()
    for fila in Perfil.objects.all():
        temp = list()
        for columna in nombre_campos:
            temp.append(fila.serializable_value(columna.name))
        writer.writerow(temp)
    
    # Devuelve un archivo CSV.
    if tipo == 'csv': 
        return response
    
    # Se define la ubicación de los archivos temporales.
    temp_folder = f'{os.path.realpath(".")}\\__temp\\'
    temp_csv = f'{temp_folder}__temp.csv'
    
    # Se corrobora que exista la carpeta temporal.
    if not os.path.exists(temp_folder):
        os.mkdir(temp_folder)
    
    # Se escribe el CSV en físico.
    temp = open(temp_csv, 'wb')
    temp.write(response.content)
    temp.close()
    
    # Devuelve un archivo XLSX.
    if tipo == 'excel': 
        # Pandas lee el CSV desde un archivo.
        archivo_leido = pandas.read_csv(temp_csv)
        
        # Se convierte a excel y se almacena como archivo XLSX.
        archivo_leido.to_excel(f'{temp_folder}{nombre_archivo_con_extension}', 
                                index = None, header=True, sheet_name=f'{informe_de}')
        
        # Devuelve un archivo XLSX.
        return FileResponse(open(f'{temp_folder}{nombre_archivo_con_extension}', 'rb'))
    
    # Se crea y se rellena un archivo DOCX.
    document = docx.Document()
    document.add_heading(f'Informe de {informe_de}', 0)
    document.add_paragraph(f'Con fecha {now_}.')
    
    with open(temp_csv, newline='') as f:
        csv_reader = csv.reader(f)
        csv_headers = next(csv_reader)
        csv_cols = len(csv_headers)
        table = document.add_table(rows=2, cols=csv_cols)
        hdr_cells = table.rows[0].cells
        for i in range(csv_cols):
            hdr_cells[i].text = csv_headers[i]

        for row in csv_reader:
            row_cells = table.add_row().cells
            for i in range(csv_cols):
                row_cells[i].text = row[i]
    document.add_page_break()    
    document.save(f'{temp_folder}{nombre_archivo}.docx')

    # Devuelve un archivo DOCX.
    if tipo == 'word': 
        return FileResponse(open(f'{temp_folder}{nombre_archivo}.docx', 'rb'))
    
    if tipo == 'pdf':
        try:
            # Solución 1.
            # Usando MS-Office 365
            print('\nUsando Office 365\n')
            docx2pdf.convert(f'__temp\{nombre_archivo}.docx')
        except:
            import subprocess
            # Solución 2.
            # Usando LibreOffice.
            print('\nUsando LibreOffice\n')
            path_to_soffice_exe = '"C:\Program Files\LibreOffice\program\soffice.exe"'
            to_pdf = '-headless -convert-to pdf'
            outdir = '-outdir .\__temp'
            res = subprocess.run(f'{path_to_soffice_exe} {to_pdf} {outdir} "__temp\{nombre_archivo}.docx"')
            print(f'\n\n{res}\n\n')
        return FileResponse(open(f'{temp_folder}{nombre_archivo}.pdf', 'rb'))
    else:
        return HttpResponse('Error con el servidor...')