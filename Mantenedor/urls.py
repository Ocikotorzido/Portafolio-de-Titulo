from django.urls import path
from . import views
from .views import login, registro, perfil, salir

urlpatterns = [
    # APIs
    path('generar_informe/<slug:informe_de>/<int:parametros>/<slug:tipo>/', views.generar_informe),
    path('modificar_reserva/<int:id_reserva>/<int:id_mecanico>/<int:confirmacion>/', views.modificar_reserva),
    path('eliminar_reserva/<int:id_reserva>/', views.eliminar_reserva),
    path('eliminar_pedido/<int:id_pedido>/', views.eliminar_pedido),
    path('get_new_id_pedido/',views.get_new_id_pedido),
    path('agregar_pedido/<int:id_auto>/',views.agregar_pedido),
    path('agregar_det_prod/<int:id_pedido>/<int:cant>/<int:id_producto>/',views.agregar_det_prod),
    path('consultar_fecha_pedido/<int:id_pedido>/', views.consultar_fecha_pedido),
    path('consultar_fecha_entrega/<int:id_pedido>/', views.consultar_fecha_entrega),
    path('registrar_pago/<int:id_orden>/<str:tipo_recibo>/', views.registrar_pago),
    path('eliminar_pago/<int:id_pago>/', views.eliminar_pago),
    path('agregar_producto/<str:nombre>/<str:codigo>/<int:valor>/<str:descripcion>/<int:id_proveedor>/', views.agregar_producto),
    
    # [host]/Mantenedor/...
    path('', views.to_index),
    path('index', views.index, name='index'),
    path('registro_cliente', views.registro_cliente, name='registro_cliente'),
    path('ver_perfil', views.ver_perfil, name='ver_perfil'),
    
    path('servicios', views.servicios, name='servicios'),
    path('reservas', views.reservas, name='reservas'),
    path('ver_reservas', views.ver_reservas, name='ver_reservas'),
    path('orden_trabajo', views.orden_trabajo, name='orden_trabajo'),
    path('orden_pedido', views.orden_pedido, name='orden_pedido'),
    path('exportar', views.exportar, name='exportar'),
    path('pago', views.pago, name='pago'),

    path('empleado',views.empleado, name='empleado'),
    path('agregar_empleado', views.agregar_empleado, name='agregar_empleado'),
    path('login/', login, name='login'),

    path('registrar_proveedor',views.registrar_proveedor, name='registrar_proveedor'),
    path('ver_proveedores',views.ver_proveedores, name='ver_proveedores'),
    path('registro_vehiculo',views.registro_vehiculo, name='registro_vehiculo'),
    path('presupuesto',views.presupuesto, name='presupuesto'),
    path('comprobante_pago/<int:id_orden>/<str:tipo_comprobante>/',views.comprobante_pago, name='comprobante_pago'),
    path('productos',views.productos, name='productos'),

    path('faq',views.faq, name='faq'),

    path('registro/', registro, name='registro'),
    path('perfil/',perfil, name='perfil'),
    path('salir/',salir, name='salir')
]