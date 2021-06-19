from django.contrib import admin
from django.apps import apps
from .models import *

tablas_db = apps.all_models['Mantenedor']

for _, tabla in tablas_db.items():
  admin.site.register(tabla)