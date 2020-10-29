from django.contrib import admin
from .models import Proveedor, MateriaPrima, Membership
# Register your models here.
admin.site.register(Proveedor)
admin.site.register(MateriaPrima)
admin.site.register(Membership)