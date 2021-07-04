from django.core.management.base import BaseCommand, CommandError
from Mantenedor.models import *

servicios_disponibles = {
        'servicio_1': {
          'nom_ser':'Cambio de neumáticos',
          'monto':125000,
          'tiempo':'200 min'
          },
        'servicio_2': {
          'nom_ser':'Cambio de aceite',
          'monto':25000,
          'tiempo':'15 min'
          },
        'servicio_3': {
          'nom_ser':'Cambio de pastillas',
          'monto':50000,
          'tiempo':'40 min'
          },
        'servicio_4': {
          'nom_ser':'Cambio de correas',
          'monto':15000,
          'tiempo':'50 min'
          },
        'servicio_5': {
          'nom_ser':'cambio de bujías',
          'monto':35000,
          'tiempo':'30 min'
          },
        'servicio_6': {
          'nom_ser':'Cambio de amortiguadores',
          'monto':65000,
          'tiempo':'140 min'
          },
        'servicio_7': {
          'nom_ser':'Cambio de baterías',
          'monto':75000,
          'tiempo':'45 min'
          },
        'servicio_8': {
          'nom_ser':'Cambio de filtros de aire',
          'monto':85000,
          'tiempo':'120 min'
          },
    }



proveedores = {
        'proveedor_1': {
          'rut':111111111,
          'nombre':'Goodyear',
          'telefono':111111111,
          'email':'Goodyear@goodyear.cl' ,
          'rubro': 'Neumaticos' 
          },
        'proveedor_2': {
          'rut':222222222,
          'nombre':'LiquiMoly',
          'telefono':222222222,
          'email': 'liqMoly@liqmoli.cl' ,
          'rubro': 'Aceite de motor'
          },
        'proveedor_3': {
          'rut':333333333,
          'nombre':'Itai',
          'telefono':333333333,
          'email': 'Itai@itai.cl' ,
          'rubro': 'Pastillas de frenos'
          },
        'proveedor_4': {
          'rut':444444444,
          'nombre':'Emasa',
          'telefono':444444444,
          'email': 'Emasa@emasa.cl',
          'rubro': 'Correas'
          },
        'proveedor_5': {
          'rut':555555555,
          'nombre':'Quiminet',
          'telefono':555555555,
          'email': 'Quiminet@quiminet.cl' ,
          'rubro': 'Bujias'
          },
        'proveedor_6': {
          'rut':666666666,
          'nombre':'Gzshock',
          'telefono':666666666,
          'email': 'Gzshock@gzshock.cl' ,
          'rubro': 'Amortiguadores'
          },
        'proveedor_7': {
          'rut':777777777,
          'nombre':'Emegchile',
          'telefono':777777777,
          'email': 'Emegchile@emegchile.cl',
          'rubro': 'Baterias'
          },
        'proveedor_8': {
          'rut':888888888,
          'nombre':'Autotec',
          'telefono':888888888,
          'email': 'Autotec@autotec.cl',
          'rubro': 'Filtros'
          },
}



class Command(BaseCommand):
    """Comandos personalizados:
    
    'python manage.py poblate' -> Rellena la base de datos.
    
    """
    help = 'English/Poblate the database with customized values. Español/ReLLeNaR lA bAsE dE dAtOs.'

    def handle(self, *args, **options):
      self.stdout.write(self.style.SUCCESS('Iniciando proceso de llenado de tablas... '))
      self.stdout.write(self.style.WARNING('Tabla TIPO_SERVICIOS'))
      for index, ser in enumerate(servicios_disponibles):
        self.stdout.write(self.style.WARNING((index+1, 
            servicios_disponibles[ser].get('nom_ser'),
            servicios_disponibles[ser].get('monto'),
            servicios_disponibles[ser].get('tiempo')
            )))
        servicio = TipoServicio(index+1, 
              servicios_disponibles[ser].get('nom_ser'),
              servicios_disponibles[ser].get('monto'),
              servicios_disponibles[ser].get('tiempo')
              )
        servicio.save()

      self.stdout.write(self.style.SUCCESS('Iniciando proceso de llenado de tablas... '))
      self.stdout.write(self.style.WARNING('Tabla proveedor'))
      for id, pro in enumerate(proveedores):
        self.stdout.write(self.style.WARNING((id+1, 
            proveedores[pro].get('rut'),
            proveedores[pro].get('nombre'),
            proveedores[pro].get('telefono'),
            proveedores[pro].get('email'),
            proveedores[pro].get('rubro')  
            )))
        proveedor = Proveedor(id+1, 
            proveedores[pro].get('rut'),
            proveedores[pro].get('nombre'),
            proveedores[pro].get('telefono'),
            proveedores[pro].get('email'),
            proveedores[pro].get('rubro') 
              )
        proveedor.save() 

      self.stdout.write(self.style.SUCCESS('Servicios escritos en la base de datos correctamente!.'))
    

     
      
