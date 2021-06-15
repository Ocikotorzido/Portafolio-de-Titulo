from django import forms
from django.db import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class FormularioRegistro(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=30, required=False)
    email = forms.EmailField(max_length=254)

    class Meta:
        model = User
        fields = ('email', 'username', 'first_name', 'last_name')

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.username = self.cleaned_data['username']
        if commit:
            user.save()
        return user

class Cargo(models.Model):
    id_tipo_cargo = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

    class Meta:
        managed = True
        db_table = 'cargo'


class Cliente(models.Model):
    id_cliente = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    direccion = models.CharField(max_length=50, blank=True, null=True)
    telefono = models.IntegerField(blank=True, null=True)
    celular = models.IntegerField(blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    rut = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.nombre + ' ' + self.apellido + ', ' + str(self.rut)

    class Meta:
        managed = True
        db_table = 'cliente'




class DetalleCliente(models.Model):
    id_cliente = models.IntegerField()
    id_vehiculo = models.IntegerField()
    cliente_id_cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='cliente_id_cliente')
    vehiculo_id_vehiculo = models.ForeignKey('Vehiculo', models.DO_NOTHING, db_column='vehiculo_id_vehiculo')

    class Meta:
        managed = True
        db_table = 'detalle_cliente'


class DetalleInforme(models.Model):
    id_info_vehiculo = models.IntegerField()
    id_presupuesto = models.IntegerField()
    presupuesto_id_presupuesto = models.ForeignKey('Presupuesto', models.DO_NOTHING, db_column='presupuesto_id_presupuesto')
    info_auto_id_informe = models.ForeignKey('InfoAuto', models.DO_NOTHING, db_column='info_auto_id_informe')

    class Meta:
        managed = True
        db_table = 'detalle_informe'


class DetalleOp(models.Model):
    id_info_vehiculo = models.IntegerField()
    id_orden_pedido = models.IntegerField()
    info_auto_id_informe = models.ForeignKey('InfoAuto', models.DO_NOTHING, db_column='info_auto_id_informe')
    op_id_pedido = models.ForeignKey('Op', models.DO_NOTHING, db_column='op_id_pedido')

    class Meta:
        managed = True
        db_table = 'detalle_op'


class DetalleOrden(models.Model):
    id_orden_pedido = models.IntegerField()
    id_pago = models.IntegerField()
    op_id_pedido = models.ForeignKey('Op', models.DO_NOTHING, db_column='op_id_pedido')
    pago_id_pago = models.ForeignKey('Pago', models.DO_NOTHING, db_column='pago_id_pago')

    class Meta:
        managed = True
        db_table = 'detalle_orden'


class DetallePedido(models.Model):
    id_detalle_pedido = models.IntegerField(primary_key=True)
    cod_producto = models.IntegerField()
    cantidad = models.IntegerField()
    producto_id_producto = models.ForeignKey('Producto', models.DO_NOTHING, db_column='producto_id_producto')
    precio = models.CharField(max_length=50)
    op_id_pedido = models.ForeignKey('Op', models.DO_NOTHING, db_column='op_id_pedido')

    class Meta:
        managed = True
        db_table = 'detalle_pedido'


class DetalleReserva(models.Model):
    id_reserva = models.IntegerField()
    id_orden_trabajo = models.IntegerField()
    reservas_id_reserva = models.ForeignKey('Reservas', models.DO_NOTHING, db_column='reservas_id_reserva')
    ot_id_orden = models.ForeignKey('Ot', models.DO_NOTHING, db_column='ot_id_orden')

    class Meta:
        managed = True
        db_table = 'detalle_reserva'

class Empleado(models.Model):
    id_empleado = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    contacto = models.CharField(max_length=50)
    cargo_id_tipo_cargo = models.ForeignKey(Cargo, models.DO_NOTHING, db_column='cargo_id_tipo_cargo')
    rut = models.IntegerField()

    def __str__(self):
        return f'{self.nombre} + ' ' + self.apellido + self.contacto'

    class Meta:
        managed = True
        db_table = 'empleado'

class EstadoVehiculo(models.Model):
    id_estado = models.IntegerField(primary_key=True)
    fecha = models.DateField()
    hora = models.CharField(max_length=10)
    descripcion = models.CharField(max_length=200)
    empleado_id_empleado = models.ForeignKey(Empleado, models.DO_NOTHING, db_column='empleado_id_empleado')
    
    class Meta:
        managed = True
        db_table = 'estado_vehiculo'


class InfoAuto(models.Model):
    id_informe = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=200)

    class Meta:
        managed = True
        db_table = 'info_auto'




class Op(models.Model):
    id_pedido = models.IntegerField(primary_key=True)
    fecha_pedido = models.DateField()
    hora_pedido = models.CharField(max_length=10)
    fecha_entrega = models.DateField()

    class Meta:
        managed = True
        db_table = 'op'


class Ot(models.Model):
    id_orden = models.IntegerField(primary_key=True)
    fecha = models.DateField()
    servicio = models.CharField(max_length=50, blank=True, null=True)
    descripcion = models.CharField(max_length=200, blank=True, null=True)
    empleado_id_empleado = models.ForeignKey(Empleado, models.DO_NOTHING, db_column='empleado_id_empleado')

    class Meta:
        managed = True
        db_table = 'ot'


class Pago(models.Model):
    id_pago = models.IntegerField(primary_key=True)
    fecha_emision = models.DateField()
    tipo_recibo = models.CharField(max_length=10)
    monto = models.FloatField()
    iva = models.FloatField()

    class Meta:
        managed = True
        db_table = 'pago'

class Perfil(models.Model):
    id_perfil = models.IntegerField(primary_key=True)
    id_auth_user = models.IntegerField()
    id_usuario = models.IntegerField()
    nivel = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.id_perfil}) FK_AUTH_username: {User.objects.get(id=self.id_auth_user).username}, nivel: {self.nivel}, id_auth_user: {self.id_auth_user}, id_usuario: {self.id_usuario}'

    class Meta:
        managed = True
        db_table = 'perfil'
        verbose_name_plural = "Perfiles"

       


class Presupuesto(models.Model):
    id_presupuesto = models.IntegerField(primary_key=True)
    precio = models.FloatField(blank=True, null=True)
    iva = models.FloatField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'presupuesto'


class Producto(models.Model):
    id_producto = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    pro_cod_producto = models.IntegerField()
    proveedor_id_proveedor = models.ForeignKey('Proveedor', models.DO_NOTHING, db_column='proveedor_id_proveedor')
    

    class Meta:
        managed = True
        db_table = 'producto'


class Proveedor(models.Model):
    id_proveedor = models.IntegerField(primary_key=True)
    contacto = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
    rubro = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre + ', ' + self.rubro + ', ' + self.contacto

    class Meta:
        managed = True
        db_table = 'proveedor'
        verbose_name_plural = "Proveedores"


class Regions(models.Model):
    region_id = models.IntegerField(primary_key=True)
    region_name = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'regions'


class Reservas(models.Model):
    id_reserva = models.IntegerField(primary_key=True)
    servicio = models.CharField(max_length=50, blank=True, null=True)
    fecha = models.DateField()
    hora = models.CharField(max_length=10)
    cliente_id_cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='cliente_id_cliente')
    descripcion = models.CharField(max_length=200, blank=True, null=True)
    tipo_servicio_id_servicio = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'reservas'

class TipoServicio(models.Model):
    id_servicio = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    monto = models.FloatField()
    tiempo_serv = models.CharField(max_length=10)

    class Meta:
        managed = True
        db_table = 'tipo_servicio'

class Vehiculo(models.Model):
    id_vehiculo = models.IntegerField(primary_key=True)
    matricula = models.CharField(max_length=10)
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    num_chasis = models.CharField(max_length=50, blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    ultimo_servicio = models.DateField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'vehiculo'