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

cargos = {
  'cargo_1': {
    'nombre': 'ADMIN'
  },
   'cargo_2': {
    'nombre': 'MECANICO'
  },
   'cargo_3': {
    'nombre': 'RECEPCIONISTA'
  },
   'cargo_4': {
    'nombre': 'EMPLEADO'
  }
}


productos = {
  'producto_1': {
    'nombre': '19 255/35r19 Eagle F1',
    'codigo':'1001',
    'valor':25000,
    'descripcion':'Capacidad de carga 650kg',
    'proveedor_id_proveedor':1
  },
   'producto_2': {
    'nombre': '18 254/50R18 Efficientgrip',
    'codigo':'1002',
    'valor':25000,
    'descripcion':'Capacidad de carga 620kg',
    'proveedor_id_proveedor':1
  },
   'producto_3': {
    'nombre': '17 255/30r23 Eagle',
    'codigo':'1003',
    'valor':25000,
    'descripcion':'Capacidad de cargar 620kg',
    'proveedor_id_proveedor':1
  },
   'producto_4': {
    'nombre': '10w40 1L',
    'codigo':'2001',
    'valor':18000,
    'descripcion':'Aceite motor antifriccion',
    'proveedor_id_proveedor':2
  },
  'producto_5': {
    'nombre': '5w30 1L',
    'codigo':'2002',
    'valor':18000,
    'descripcion':'Aceite motor antifriccion',
    'proveedor_id_proveedor':2
  },
  'producto_6': {
    'nombre': '2.7 Frenos delanteros Kia',
    'codigo':'3001',
    'valor':16000,
    'descripcion':'Frenos delanteros kia morning',
    'proveedor_id_proveedor':3
  },
  'producto_7': {
    'nombre': '2.7 Frenos traseros Kia',
    'codigo':'3002',
    'valor':16000,
    'descripcion':'Frenos traseros kia morning',
    'proveedor_id_proveedor':3
  },
  'producto_8': {
    'nombre': '2.5 Frenos delanteros Hyundai',
    'codigo':'3003',
    'valor':16000,
    'descripcion':'Frenos delanteros Hyundai',
    'proveedor_id_proveedor':3
  },
  'producto_9': {
    'nombre': '2.5 Frenos traseros Hyundai',
    'codigo':'3004',
    'valor':16000,
    'descripcion':'Frenos traseros Hyundai',
    'proveedor_id_proveedor':3
  },
  'producto_10': {
    'nombre': 'Correa distribucion kia',
    'codigo':'4001',
    'valor':13000,
    'descripcion':'Correa alternador kia',
    'proveedor_id_proveedor':4
  },
  'producto_11': {
    'nombre': 'Correa distribucion Hyundai',
    'codigo':'4002',
    'valor':13000,
    'descripcion':'Correa alternador Hyundai',
    'proveedor_id_proveedor':4
  },
  'producto_12': {
    'nombre': 'Bujias Hyundai',
    'codigo':'5001',
    'valor':8000,
    'descripcion':'Bujias hyundai',
    'proveedor_id_proveedor':5
  },
  'producto_13': {
    'nombre': 'Bujias kia',
    'codigo':'5002',
    'valor':9000,
    'descripcion':'Bujias kia',
    'proveedor_id_proveedor':5
  },
  'producto_14': {
    'nombre': 'Amortiguador delantero hyundai',
    'codigo':'6001',
    'valor':22000,
    'descripcion':'Amortiguador delantero hyundai',
    'proveedor_id_proveedor':6
  },
  'producto_15': {
    'nombre': 'Amortiguador trasero hyundai',
    'codigo':'6002',
    'valor':22000,
    'descripcion':'Amortiguador trasero hyundai',
    'proveedor_id_proveedor':6
  },
  'producto_16': {
    'nombre': 'Amortiguador delantero kia',
    'codigo':'6003',
    'valor':21000,
    'descripcion':'Amortiguador delantero kia',
    'proveedor_id_proveedor':6
  },
  'producto_17': {
    'nombre': 'Amortiguador trasero kia',
    'codigo':'6004',
    'valor':21000,
    'descripcion':'Amortiguador trasero kia',
    'proveedor_id_proveedor':6
  },
  'producto_18': {
    'nombre': 'Bateria kia 1.2 12v-35',
    'codigo':'7001',
    'valor':50000,
    'descripcion':'Baterias kia',
    'proveedor_id_proveedor':7
  },
  'producto_19': {
    'nombre': 'Bateria hyundai 1.3 11v-35',
    'codigo':'7002',
    'valor':55000,
    'descripcion':'Baterias hyundia',
    'proveedor_id_proveedor':7
  },
  'producto_20': {
    'nombre': 'Filtro de aire TROOP kia',
    'codigo':'8001',
    'valor':16000,
    'descripcion':'Filtro de aire kia',
    'proveedor_id_proveedor':8
  },
  'producto_21': {
    'nombre': 'Filtro de aire hyundai',
    'codigo':'8001',
    'valor':18000,
    'descripcion':'Filtro de aire hyundai',
    'proveedor_id_proveedor':8
  }
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


      self.stdout.write(self.style.SUCCESS('Iniciando proceso de llenado de tablas... '))
      self.stdout.write(self.style.WARNING('Tabla cargo'))
      for id_cargo, car in enumerate(cargos):
        self.stdout.write(self.style.WARNING((id_cargo+1, 
            cargos[car].get('nombre')
            )))
        cargo = Cargo(id_cargo+1, 
            cargos[car].get('nombre')
              )
        cargo.save()  

      self.stdout.write(self.style.SUCCESS('Iniciando proceso de llenado de tablas... '))
      self.stdout.write(self.style.WARNING('Tabla productos'))
      for id_producto, prod in enumerate(productos):
        self.stdout.write(self.style.WARNING((id_producto+1, 
            productos[prod].get('nombre'),
            productos[prod].get('codigo'),
            productos[prod].get('valor'),
            productos[prod].get('descripcion'),
            productos[prod].get('proveedor_id_proveedor') 
            )))
        producto = Producto(id_producto+1, 
            productos[prod].get('nombre'),
            productos[prod].get('codigo'),
            productos[prod].get('valor'),
            productos[prod].get('descripcion'),
            productos[prod].get('proveedor_id_proveedor') 
            )
        producto.save() 

      self.stdout.write(self.style.SUCCESS('Servicios escritos en la base de datos correctamente!.'))
    

     
      
