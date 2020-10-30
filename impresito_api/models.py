from django.db import models

# Create your models here.

# TABLA ORDEN DE TRABAJO
class OrdenDeTrabajo(models.Model):
    detalle = models.CharField(max_length=40)
    descripcionMp = models.CharField(max_length=10)
    cantMprimaUtilizada = models.IntegerField(default=0)
    fecha = models.DateField()
    def __str__(self):
       return "{}".format(self.detalle)    


# TABLA MATERIA PRIMA
class MateriaPrima( models.Model):
    descripcion = models.CharField(max_length=100)
    stock = models.IntegerField(default=0)
    precio = models.IntegerField(default=0)
    ordenDeTrabajo = models.ForeignKey(OrdenDeTrabajo, on_delete=models.CASCADE)
    def __str__(self):
        return self.descripcion

# TABLA  PROVEEDOR
class Proveedor( models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=30)
    email = models.EmailField
    members = models.ManyToManyField(MateriaPrima, through='Membership')
    def __str__(self):
        return self.nombre

# TABLA INTERMEDIA ENTRE (MATERIA PRIMA CON PROVEEDOR) //RELACION MUCHOS A MUCHOS
class Membership(models.Model):
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    materiaprima = models.ForeignKey(MateriaPrima, on_delete=models.CASCADE)
    date_joined = models.DateField()

# TABLA CLIENTES
class Cliente( models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=30)
    email = models.EmailField

# TABLA PEDIDOS
class Pedido(models.Model):
    fecha = models.DateField()
    descripcion = models.CharField(max_length=40)
    cliente = models.CharField(max_length=10)
    ordenDeTrabajo = models.IntegerField(default=0)
    idcliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
   
# TABLA VENTA
class Venta(models.Model):
    producto = models.CharField(max_length=40)
    precioUnitario = models.IntegerField(default=0)
    precioTotal = models.IntegerField(default=0)
# TABLA PRODUCTO
class Producto(models.Model):
    descripcionP = models.CharField(max_length=40)
    materiaPriUtilizada = models.CharField(max_length=40)
    cantiMatPriUtilizada = models.IntegerField(default=0)
    stock = models.IntegerField(default=0)
    idventas = models.ForeignKey(Venta, on_delete=models.CASCADE)

    