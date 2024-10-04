from django.contrib import admin
from django.forms import Textarea
from django.db import models
from .models import Estados,Frecuencias, Uom, Mediaciones, Comportamientos, Programas, Tipos, VariablesFactor, \
    ProcesosSam, Procesos, Variables, ProcesosHasVariables, EjecucionesLog, Instancias, VariablesHasInstancias,VariablesProgramacion


class MyAdminSite(admin.AdminSite):
   site_header="Bitácora de Variables"


admin_site=MyAdminSite(name="myadmin")


class ReadOnlyAdminMixin:
    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

@admin.register(EjecucionesLog,site=admin_site)
class EjecucionesLogAdmin(ReadOnlyAdminMixin, admin.ModelAdmin):
    #formfield_overrides = {
     #   models.TextField: {'widget': Textarea(attrs={'rows': 10, 'cols': 80})},
    #}
    list_display = ('Variable','Tipo_Modificacion','fecha_modificado')

@admin.register(Variables, site=admin_site)
class VariablesAdmin(admin.ModelAdmin):
    readonly_fields = ('fecha_modificacion',)
    list_display = ('nombre_variable', 'SAM', 'ODS', 'Tipo', 'UOM', 'Frecuencia', 'Mediacion', 'Programa', 'Comportamiento', 'Variable_Factor', 'Proceso_SAM')

models_to_register = [
    Estados, Frecuencias, Uom, Mediaciones, Comportamientos, Programas, Tipos, VariablesFactor,
    ProcesosSam, Procesos, ProcesosHasVariables, Instancias, VariablesHasInstancias, VariablesProgramacion
]

for model in models_to_register:
    admin_site.register(model)

