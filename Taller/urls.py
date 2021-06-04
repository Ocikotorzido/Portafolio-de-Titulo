from django.contrib import admin
from django.urls import path, include
from Mantenedor.views import to_index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', to_index, name='to_index'),
    path('Mantenedor/', include('Mantenedor.urls'), name='Mantenedor'),
]