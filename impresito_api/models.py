from django.db import models

# Create your models here.
class Proveedor( models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=30)
    email = models.EmailField
    def __str__(self):
        return self.nombre
class MateriaPrima( models.Model):
    descripcion = models.CharField(max_length=100)
    stock = models.IntegerField(default=0)
    precio = models.IntegerField(default=0)
    members = models.ManyToManyField(Proveedor, through='Membership')
    def __str__(self):
        return self.descripcion
class Membership(models.Model):
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    materiaprima = models.ForeignKey(MateriaPrima, on_delete=models.CASCADE)
    date_joined = models.DateField()
    def __str__(self):
        return self.proveedor.nombre + self.proveedor.telefono
    
    