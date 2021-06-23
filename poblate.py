#!/usr/bin/env python
#-*- coding: utf-8 -*-

from Mantenedor.models import *

# OJO: Servicios disponibles.
# |-- id_servicio = models.FloatField(primary_key=True)
# |-- nombre = models.CharField(max_length=50)
# |-- monto = models.FloatField()
# |-- tiempo_serv = models.CharField(max_length=10)
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
          'nom_ser':'Cambio de filtros',
          'monto':85000,
          'tiempo':'120 min'
          },
    }

for index, ser in enumerate(servicios_disponibles):
  print(index+1, 
        servicios_disponibles[ser].get('nom_ser'),
        servicios_disponibles[ser].get('monto'),
        servicios_disponibles[ser].get('tiempo')
        )
  servicio = TipoServicio(index+1, 
        servicios_disponibles[ser].get('nom_ser'),
        servicios_disponibles[ser].get('monto'),
        servicios_disponibles[ser].get('tiempo')
        )
  servicio.save()
  
print('Servicios guardados.')