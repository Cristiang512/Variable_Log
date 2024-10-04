from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Variables, EjecucionesLog, VariablesProgramacion
from django.contrib.auth import get_user_model
from django.utils import timezone

User = get_user_model()

@receiver(pre_save, sender=Variables)
def log_variable_changes(sender, instance, **kwargs):
    if instance.pk:  # Verificar si la instancia ya existe (es una actualización)
        try:
            old_instance = Variables.objects.get(pk=instance.pk)
        except Variables.DoesNotExist:
            return  # Si no existe, no hacemos nada

        user = User.objects.get(username='cristiangutierrez')  # Cambia esto por la forma en que obtienes el usuario actual
        ignored_fields = ['fecha_modificacion']
        changes = []

        for field in instance._meta.fields:
            field_name = field.name
            if field_name in ignored_fields:
                continue  # Ignorar los cambios en los campos especificados
            old_value = getattr(old_instance, field_name)
            new_value = getattr(instance, field_name)
            if old_value != new_value:
                changes.append(f'{field_name}: Antes: {old_value}, Después: {new_value}')

        if changes:
            valor_modificado = '; '.join(changes)
            columna_modificacion = ', '.join([change.split(': ')[0] for change in changes])
            EjecucionesLog.objects.create(
                Variable=instance,
                Usuario=user,
                Tipo_Modificacion='Configuración',
                Columna_Modificacion=columna_modificacion,  # Lista de campos modificados
                Valor_Modificado=valor_modificado,  # Guardar los detalles de los cambios
                fecha_modificado=timezone.now()
            )

@receiver(pre_save, sender=VariablesProgramacion)
def log_programacion_changes(sender, instance, **kwargs):
    if instance.pk:  # Verificar si la instancia ya existe (es una actualización)
        try:
            old_instance = VariablesProgramacion.objects.get(pk=instance.pk)
        except VariablesProgramacion.DoesNotExist:
            return  # Si no existe, no hacemos nada

        user = User.objects.get(username='cristiangutierrez')  # Cambia esto por la forma en que obtienes el usuario actual
        ignored_fields = []
        changes = []

        for field in instance._meta.fields:
            field_name = field.name
            if field_name in ignored_fields:
                continue  # Ignorar los cambios en los campos especificados
            old_value = getattr(old_instance, field_name)
            new_value = getattr(instance, field_name)
            if old_value != new_value:
                changes.append(f'{field_name}: Antes: {old_value}, Después: {new_value}')

        if changes:
            valor_modificado = '; '.join(changes)
            columna_modificacion = ', '.join([change.split(': ')[0] for change in changes])
            EjecucionesLog.objects.create(
                Variable=instance.id_variable,
                Usuario=user,
                Tipo_Modificacion='Programación',
                Columna_Modificacion=columna_modificacion,  # Lista de campos modificados
                Valor_Modificado=valor_modificado,  # Guardar los detalles de los cambios
                fecha_modificado=timezone.now()
            )
