from django.db import models
from django.db.models.fields import BLANK_CHOICE_DASH

# Create your models here.

class Cargo(models.Model):
    id_tipo_cargo = models.FloatField(primary_key=True)
    nombre = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'cargo'


class Cliente(models.Model):
    id_cliente = models.FloatField(primary_key=True)
    rut = models.FloatField(blank=True, null=True)
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    direccion = models.CharField(max_length=50, blank=True, null=True)
    telefono = models.FloatField(blank=True, null=True)
    celular = models.FloatField(blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    password = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'cliente'


class Countries(models.Model):
    country_id = models.CharField(primary_key=True, max_length=2)
    country_name = models.CharField(max_length=40, blank=True, null=True)
    region = models.ForeignKey('Regions', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'countries'


class Departments(models.Model):
    department_id = models.IntegerField(primary_key=True)
    department_name = models.CharField(max_length=30)
    manager = models.ForeignKey('Employees', models.DO_NOTHING, blank=True, null=True)
    location = models.ForeignKey('Locations', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'departments'


class DetalleCliente(models.Model):
    id_cliente = models.FloatField()
    id_vehiculo = models.FloatField()
    cliente_id_cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='cliente_id_cliente')
    vehiculo_id_vehiculo = models.ForeignKey('Vehiculo', models.DO_NOTHING, db_column='vehiculo_id_vehiculo')

    class Meta:
        managed = False
        db_table = 'detalle_cliente'


class DetalleInforme(models.Model):
    id_info_vehiculo = models.FloatField()
    id_presupuesto = models.FloatField()
    presupuesto_id_presupuesto = models.ForeignKey('Presupuesto', models.DO_NOTHING, db_column='presupuesto_id_presupuesto')
    info_auto_id_informe = models.ForeignKey('InfoAuto', models.DO_NOTHING, db_column='info_auto_id_informe')

    class Meta:
        managed = False
        db_table = 'detalle_informe'


class DetalleOp(models.Model):
    id_info_vehiculo = models.FloatField()
    id_orden_pedido = models.FloatField()
    info_auto_id_informe = models.ForeignKey('InfoAuto', models.DO_NOTHING, db_column='info_auto_id_informe')
    op_id_pedido = models.ForeignKey('Op', models.DO_NOTHING, db_column='op_id_pedido')

    class Meta:
        managed = False
        db_table = 'detalle_op'


class DetalleOrden(models.Model):
    id_orden_pedido = models.FloatField()
    id_pago = models.FloatField()
    op_id_pedido = models.ForeignKey('Op', models.DO_NOTHING, db_column='op_id_pedido')
    pago_id_pago = models.ForeignKey('Pago', models.DO_NOTHING, db_column='pago_id_pago')

    class Meta:
        managed = False
        db_table = 'detalle_orden'


class DetallePedido(models.Model):
    id_detalle_pedido = models.FloatField(primary_key=True)
    cod_producto = models.FloatField()
    cantidad = models.FloatField()
    producto_id_producto = models.ForeignKey('Producto', models.DO_NOTHING, db_column='producto_id_producto')
    precio = models.CharField(max_length=50)
    op_id_pedido = models.ForeignKey('Op', models.DO_NOTHING, db_column='op_id_pedido')

    class Meta:
        managed = False
        db_table = 'detalle_pedido'


class DetalleReserva(models.Model):
    id_reserva = models.FloatField()
    id_orden_trabajo = models.FloatField()
    reservas_id_reserva = models.ForeignKey('Reservas', models.DO_NOTHING, db_column='reservas_id_reserva')
    ot_id_orden = models.ForeignKey('Ot', models.DO_NOTHING, db_column='ot_id_orden')

    class Meta:
        managed = False
        db_table = 'detalle_reserva'


class Empleado(models.Model):
    id_empleado = models.FloatField(primary_key=True)
    id_cargo = models.FloatField()
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    contacto = models.CharField(max_length=50)
    cargo_id_tipo_cargo = models.ForeignKey(Cargo, models.DO_NOTHING, db_column='cargo_id_tipo_cargo')
    estado_vehiculo_id_estado = models.ForeignKey('EstadoVehiculo', models.DO_NOTHING, db_column='estado_vehiculo_id_estado')
    info_auto_id_informe = models.ForeignKey('InfoAuto', models.DO_NOTHING, db_column='info_auto_id_informe')

    class Meta:
        managed = False
        db_table = 'empleado'


class Employees(models.Model):
    employee_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=20, blank=True, null=True)
    last_name = models.CharField(max_length=25)
    email = models.CharField(unique=True, max_length=25)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    hire_date = models.DateField()
    job = models.ForeignKey('Jobs', models.DO_NOTHING)
    salary = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    commission_pct = models.DecimalField(max_digits=2, decimal_places=2, blank=True, null=True)
    manager = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    department = models.ForeignKey(Departments, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'employees'


class EstadoVehiculo(models.Model):
    id_estado = models.FloatField(primary_key=True)
    fecha = models.DateField()
    hora = models.CharField(max_length=10)
    descripcion = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'estado_vehiculo'


class InfoAuto(models.Model):
    id_informe = models.FloatField(primary_key=True)
    descripcion = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'info_auto'


class Jobs(models.Model):
    job_id = models.CharField(primary_key=True, max_length=10)
    job_title = models.CharField(max_length=35)
    min_salary = models.IntegerField(blank=True, null=True)
    max_salary = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jobs'


class Locations(models.Model):
    location_id = models.IntegerField(primary_key=True)
    street_address = models.CharField(max_length=40, blank=True, null=True)
    postal_code = models.CharField(max_length=12, blank=True, null=True)
    city = models.CharField(max_length=30)
    state_province = models.CharField(max_length=25, blank=True, null=True)
    country = models.ForeignKey(Countries, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'locations'


class Op(models.Model):
    id_pedido = models.FloatField(primary_key=True)
    fecha_pedido = models.DateField()
    hora_pedido = models.CharField(max_length=10)
    fecha_entrega = models.DateField()

    class Meta:
        managed = False
        db_table = 'op'


class Ot(models.Model):
    id_orden = models.FloatField(primary_key=True)
    fecha = models.DateField()
    servicio = models.CharField(max_length=50, blank=True, null=True)
    descripcion = models.CharField(max_length=200, blank=True, null=True)
    empleado_id_empleado = models.ForeignKey(Empleado, models.DO_NOTHING, db_column='empleado_id_empleado')

    class Meta:
        managed = False
        db_table = 'ot'


class Pago(models.Model):
    id_pago = models.FloatField(primary_key=True)
    fecha_emision = models.DateField()
    tipo_recibo = models.CharField(max_length=10)
    monto = models.FloatField()
    iva = models.FloatField()

    class Meta:
        managed = False
        db_table = 'pago'


class Presupuesto(models.Model):
    id_presupuesto = models.FloatField(primary_key=True)
    precio = models.FloatField(blank=True, null=True)
    iva = models.FloatField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'presupuesto'


class Producto(models.Model):
    id_producto = models.FloatField(primary_key=True)
    nombre = models.CharField(max_length=50)
    pro_cod_producto = models.FloatField()
    proveedor_id_proveedor = models.ForeignKey('Proveedor', models.DO_NOTHING, db_column='proveedor_id_proveedor')

    class Meta:
        managed = False
        db_table = 'producto'


class Proveedor(models.Model):
    id_proveedor = models.FloatField(primary_key=True)
    contacto = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
    rubro = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'proveedor'


class Regions(models.Model):
    region_id = models.FloatField(primary_key=True)
    region_name = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'regions'



class TipoServicio(models.Model):
    id_servicio = models.FloatField(primary_key=True)
    nombre = models.CharField(max_length=50)
    monto = models.FloatField()
    # reservas_id_reserva = models.ForeignKey(Reservas, models.DO_NOTHING, db_column='reservas_id_reserva')
    tiempo_serv = models.CharField(max_length=10)
    
    def __str__(self) -> str:
        return self.nombre


    class Meta:
        managed = False
        db_table = 'tipo_servicio'


class Reservas(models.Model):
    id_reserva = models.FloatField(primary_key=True)
    servicio = models.CharField(max_length=50, blank=True, null=True)
    fecha = models.DateField()
    hora = models.CharField(max_length=10)
    cliente_id_cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='cliente_id_cliente')
    descripcion = models.CharField(max_length=200, blank=True, null=True)
    Tipo_Servicio_id_servicio = models.ForeignKey(TipoServicio, models.DO_NOTHING, db_column='tipo_servicio_id_servicio')


    class Meta:
        managed = False
        db_table = 'reservas'
class Vehiculo(models.Model):
    id_vehiculo = models.FloatField(primary_key=True)
    matricula = models.CharField(max_length=10)
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    num_chasis = models.CharField(max_length=50, blank=True, null=True)
    year = models.FloatField(blank=True, null=True)
    ultimo_servicio = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vehiculo'