from django.contrib import admin
from .models import Proveedor, MateriaPrima, Membership, OrdenDeTrabajo, Producto, Cliente, Pedido, Venta

class MembershipInline(admin.TabularInline):
    model = MateriaPrima.members.through
class Proveedoradmin(admin.ModelAdmin):
    inlines = [
        MembershipInline,
    ]    
class MateriaPrimaadmin(admin.ModelAdmin):
    inlines = [
        MembershipInline,
    ]
    exclude = ('members',)


# Register your models here.
admin.site.register(Proveedor, Proveedoradmin)
admin.site.register(MateriaPrima, MateriaPrimaadmin)
admin.site.register(Membership)
admin.site.register(OrdenDeTrabajo)
admin.site.register(Producto)
admin.site.register(Cliente)
admin.site.register(Pedido)
admin.site.register(Venta)