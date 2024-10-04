# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.utils import timezone
from django import forms

class Comportamientos(models.Model):
    id_comportamiento = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=60, blank=True, null=True)

    def __str__(self):
            return self.descripcion
    class Meta:
        managed = False
        db_table = 'COMPORTAMIENTOS'
        verbose_name='comportamiento'
        verbose_name_plural='comportamientos'
        ordering = ('id_comportamiento', )


class EjecucionesLog(models.Model):
    id_ejecucion = models.BigAutoField(primary_key=True)
    Variable = models.ForeignKey('Variables', models.DO_NOTHING, db_column='id_variable', blank=True, null=True)
    Usuario = models.ForeignKey(User, models.DO_NOTHING, db_column='id_usuario', blank=True, null=True)  # Cambiado a User
    Tipo_Modificacion = models.CharField(max_length=255, blank=True, null=True)
    Columna_Modificacion = models.CharField(max_length=255, blank=True, null=True)
    Valor_Modificado = models.CharField(max_length=255, blank=True, null=True)
    fecha_modificado = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f'{self.Variable} - {self.Tipo_Modificacion} - Modificado el: {self.fecha_modificado}  '

    class Meta:
        managed = False
        db_table = 'EJECUCIONES_LOG'
        verbose_name='EJECUCIONES LOG'
        verbose_name_plural='EJECUCIONES LOG'
        ordering = ('-id_ejecucion', )


class Estados(models.Model):
    id_estado = models.AutoField(primary_key=True)
    estado = models.CharField(max_length=45, blank=True, null=True)

    def __str__(self):
        return self.estado
    class Meta:
        managed = False
        db_table = 'ESTADOS'
        verbose_name='estado'
        verbose_name_plural='estados'
        ordering = ('id_estado', )


class Frecuencias(models.Model):
    id_frecuencia = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=45, blank=True, null=True)

    def __str__(self):
        return self.tipo

    class Meta:
        managed = False
        db_table = 'FRECUENCIAS'
        verbose_name='frecuencia'
        verbose_name_plural='frecuencias'
        ordering = ('id_frecuencia', )

class Instancias(models.Model):
    id_instancia = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=45, blank=True, null=True)

    def __str__(self):
        return self.tipo

    class Meta:
        managed = False
        db_table = 'INSTANCIAS'
        verbose_name='instancia'
        verbose_name_plural='instancias'
        ordering = ('id_instancia', )


class JobSamData(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    external_job_id = models.IntegerField(db_column='EXTERNAL_JOB_ID', blank=True, null=True)  # Field name made lowercase.
    variable_name = models.CharField(db_column='VARIABLE_NAME', max_length=400, blank=True, null=True)  # Field name made lowercase.
    creation_date = models.DateTimeField(db_column='CREATION_DATE', blank=True, null=True)  # Field name made lowercase.
    trade_date_begin = models.DateField(db_column='TRADE_DATE_BEGIN', blank=True, null=True)  # Field name made lowercase.
    key01 = models.CharField(db_column='KEY01', max_length=50, blank=True, null=True)  # Field name made lowercase.
    key11 = models.CharField(db_column='KEY11', max_length=50, blank=True, null=True)  # Field name made lowercase.
    val001 = models.CharField(db_column='VAL001', max_length=50, blank=True, null=True)  # Field name made lowercase.
    val002 = models.CharField(db_column='VAL002', max_length=50, blank=True, null=True)  # Field name made lowercase.
    val003 = models.CharField(db_column='VAL003', max_length=50, blank=True, null=True)  # Field name made lowercase.
    val004 = models.CharField(db_column='VAL004', max_length=50, blank=True, null=True)  # Field name made lowercase.
    val005 = models.CharField(db_column='VAL005', max_length=50, blank=True, null=True)  # Field name made lowercase.
    val006 = models.CharField(db_column='VAL006', max_length=50, blank=True, null=True)  # Field name made lowercase.
    val007 = models.CharField(db_column='VAL007', max_length=50, blank=True, null=True)  # Field name made lowercase.
    val008 = models.CharField(db_column='VAL008', max_length=50, blank=True, null=True)  # Field name made lowercase.
    val009 = models.CharField(db_column='VAL009', max_length=50, blank=True, null=True)  # Field name made lowercase.
    val010 = models.CharField(db_column='VAL010', max_length=50, blank=True, null=True)  # Field name made lowercase.
    val011 = models.CharField(db_column='VAL011', max_length=50, blank=True, null=True)  # Field name made lowercase.
    val012 = models.CharField(db_column='VAL012', max_length=50, blank=True, null=True)  # Field name made lowercase.
    val013 = models.CharField(db_column='VAL013', max_length=50, blank=True, null=True)  # Field name made lowercase.
    val014 = models.CharField(db_column='VAL014', max_length=50, blank=True, null=True)  # Field name made lowercase.
    val015 = models.CharField(db_column='VAL015', max_length=50, blank=True, null=True)  # Field name made lowercase.
    val016 = models.CharField(db_column='VAL016', max_length=50, blank=True, null=True)  # Field name made lowercase.
    val017 = models.CharField(db_column='VAL017', max_length=50, blank=True, null=True)  # Field name made lowercase.
    val018 = models.CharField(db_column='VAL018', max_length=50, blank=True, null=True)  # Field name made lowercase.
    val019 = models.CharField(db_column='VAL019', max_length=50, blank=True, null=True)  # Field name made lowercase.
    val020 = models.CharField(db_column='VAL020', max_length=50, blank=True, null=True)  # Field name made lowercase.
    val021 = models.CharField(db_column='VAL021', max_length=50, blank=True, null=True)  # Field name made lowercase.
    val022 = models.CharField(db_column='VAL022', max_length=50, blank=True, null=True)  # Field name made lowercase.
    val023 = models.CharField(db_column='VAL023', max_length=50, blank=True, null=True)  # Field name made lowercase.
    val024 = models.CharField(db_column='VAL024', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'JOB_SAM_DATA'


class Mediaciones(models.Model):
    id_mediacion = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.tipo
    class Meta:
        managed = False
        db_table = 'MEDIACIONES'
        verbose_name='mediación'
        verbose_name_plural='mediaciones'
        ordering = ('id_mediacion', )


class Operacion(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_variable = models.TextField(db_column='ID_VARIABLE')  # Field name made lowercase.
    ambiente = models.CharField(db_column='AMBIENTE', max_length=10)  # Field name made lowercase.
    offset = models.CharField(db_column='OFFSET', max_length=10)  # Field name made lowercase.
    fecha_proceso = models.DateField(db_column='FECHA_PROCESO', blank=True, null=True)  # Field name made lowercase.
    fecha_ejecucion = models.DateTimeField(db_column='FECHA_EJECUCION', blank=True, null=True)  # Field name made lowercase.
    fecha_consulta = models.DateTimeField(db_column='FECHA_CONSULTA', blank=True, null=True)  # Field name made lowercase.
    file_id = models.CharField(db_column='FILE_ID', max_length=10, blank=True, null=True)  # Field name made lowercase.
    estado = models.CharField(db_column='ESTADO', max_length=20)  # Field name made lowercase.
    observaciones = models.TextField(db_column='OBSERVACIONES', blank=True, null=True)  # Field name made lowercase.
    liquidacion = models.CharField(db_column='LIQUIDACION', max_length=15, blank=True, null=True)  # Field name made lowercase.
    validar = models.CharField(db_column='VALIDAR', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OPERACION'


class OperacionDetalle(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_operacion = models.IntegerField(db_column='ID_OPERACION')  # Field name made lowercase.
    datos_legados = models.IntegerField(db_column='DATOS_LEGADOS')  # Field name made lowercase.
    tabla_sam = models.CharField(db_column='TABLA_SAM', max_length=20)  # Field name made lowercase.
    datos_data_raw = models.IntegerField(db_column='DATOS_DATA_RAW')  # Field name made lowercase.
    datos_sam = models.IntegerField(db_column='DATOS_SAM')  # Field name made lowercase.
    estado_conteo = models.CharField(db_column='ESTADO_CONTEO', max_length=20)  # Field name made lowercase.
    calidad_datos_estado = models.CharField(db_column='CALIDAD_DATOS_ESTADO', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OPERACION_DETALLE'


class OperacionVariable(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nombre_variable = models.TextField(db_column='NOMBRE_VARIABLE')  # Field name made lowercase.
    mediacion = models.CharField(db_column='MEDIACION', max_length=50, blank=True, null=True)  # Field name made lowercase.
    frecuencia = models.CharField(db_column='FRECUENCIA', max_length=30, blank=True, null=True)  # Field name made lowercase.
    uom = models.CharField(db_column='UOM', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fuente = models.CharField(db_column='FUENTE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    tipo = models.CharField(db_column='TIPO', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fecha_actualizacion = models.DateTimeField(db_column='FECHA_ACTUALIZACION')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OPERACION_VARIABLE'


class Procesos(models.Model):
    id_proceso = models.AutoField(primary_key=True)
    nombre_proceso = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.nombre_proceso
    class Meta:
        managed = False
        db_table = 'PROCESOS'
        verbose_name='proceso'
        verbose_name_plural='procesos'
        ordering = ('id_proceso', )


class ProcesosSam(models.Model):
    id_proceso_sam = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.nombre
    class Meta:
        managed = False
        db_table = 'PROCESOS_SAM'
        verbose_name='Procesos SAM'
        verbose_name_plural='Procesos SAM'
        ordering = ('id_proceso_sam', )


class ProcesosHasVariables(models.Model):
    id = models.AutoField(primary_key=True)
    id_proceso = models.ForeignKey('Procesos', models.DO_NOTHING, db_column='id_proceso')
    id_variable = models.ForeignKey('Variables', models.DO_NOTHING, db_column='id_variable')

    def get_proceso_nombre(self):
        return self.id_proceso.nombre_proceso

    def get_variable_nombre(self):
        return self.id_variable.nombre_variable

    get_proceso_nombre.short_description = 'Nombre del Proceso'
    get_variable_nombre.short_description = 'Nombre de la Variable'

    def __str__(self):
        return f'{self.get_proceso_nombre()} - {self.get_variable_nombre()}'

    class Meta:
        managed = False
        db_table = 'PROCESOS_has_VARIABLES'
        verbose_name='Variable con Proceso'
        verbose_name_plural='Variables con Procesos'
        unique_together = (('id_proceso', 'id_variable'),)


class Programas(models.Model):
    id_programa = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=60, blank=True, null=True)

    def __str__(self):
        return self.descripcion
    class Meta:
        managed = False
        db_table = 'PROGRAMAS'
        verbose_name='programa'
        verbose_name_plural='programas'
        ordering = ('id_programa', )


class Tipos(models.Model):
    id_tipo = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=60, blank=True, null=True)

    def __str__(self):
        return self.tipo
    class Meta:
        managed = False
        db_table = 'TIPOS'
        verbose_name='tipo'
        verbose_name_plural='tipos'
        ordering = ('id_tipo', )


class Uom(models.Model):
    id_uom = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=60, blank=True, null=True)

    def __str__(self):
        return self.descripcion
    class Meta:
        managed = False
        db_table = 'UOM'
        verbose_name='Uom'
        verbose_name_plural='Uom'
        ordering = ('id_uom', )


class Usuarios(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255, blank=True, null=True)
    correo = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'USUARIOS'


class Variables(models.Model):
    id_variable = models.BigAutoField(primary_key=True)
    nombre_variable = models.CharField(max_length=255, blank=True, null=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True, editable=False)
    SAM = models.CharField(max_length=45, blank=True, null=True)
    ODS = models.CharField(max_length=45, blank=True, null=True)
    Tipo = models.ForeignKey(Tipos, models.DO_NOTHING, db_column='id_tipo', blank=True, null=True)
    UOM = models.ForeignKey(Uom, models.DO_NOTHING, db_column='id_uom', blank=True, null=True)
    Frecuencia = models.ForeignKey(Frecuencias, models.DO_NOTHING, db_column='id_frecuencia', blank=True, null=True)
    Mediacion = models.ForeignKey(Mediaciones, models.DO_NOTHING, db_column='id_mediacion', blank=True, null=True)
    Programa = models.ForeignKey(Programas, models.DO_NOTHING, db_column='id_programa', blank=True, null=True)
    Comportamiento = models.ForeignKey(Comportamientos, models.DO_NOTHING, db_column='id_comportamiento', blank=True, null=True)
    Variable_Factor = models.ForeignKey('VariablesFactor', models.DO_NOTHING, db_column='id_variable_factor', blank=True, null=True)
    Proceso_SAM = models.ForeignKey(ProcesosSam, models.DO_NOTHING, db_column='id_proceso_sam', blank=True, null=True)

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request, obj, change, **kwargs)
        if obj:
            form.base_fields['fecha_modificacion'].disabled = True
        return form

    def clean(self):
        super().clean()
        if self.SAM not in ['Y', 'N', None]:
            raise ValidationError('SAM debe ser "Y" o "N".')
        if self.ODS not in ['Y', 'N', None]:
            raise ValidationError('ODS debe ser "Y" o "N".')
    def save(self, *args, **kwargs):
        if not self.fecha_modificacion:
            self.fecha_modificacion = timezone.now()
        else:
            self.fecha_modificacion = timezone.now()
        super(Variables, self).save(*args, **kwargs)
    def __str__(self):
        return self.nombre_variable
    class Meta:
        managed = False
        db_table = 'VARIABLES'
        verbose_name='Variable'
        verbose_name_plural='Variables'
        ordering = ('id_variable', )

class Variablesborrador(models.Model):
    data_name = models.CharField(db_column='DATA_NAME', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    sam = models.CharField(db_column='SAM', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    ods = models.CharField(db_column='ODS', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    tipo = models.CharField(db_column='TIPO', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    uom = models.CharField(db_column='UOM', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    frecuencia = models.CharField(db_column='FRECUENCIA', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    mediacion = models.CharField(db_column='MEDIACION', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    programa = models.CharField(db_column='PROGRAMA', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    comportamiento = models.CharField(db_column='COMPORTAMIENTO', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    variable_factor = models.CharField(db_column='VARIABLE_FACTOR', max_length=4000, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'VARIABLESBORRADOR'


class VariablesFactor(models.Model):
    id_variable_factor = models.AutoField(primary_key=True)
    factor = models.CharField(max_length=60, blank=True, null=True)

    def __str__(self):
        return self.factor
    class Meta:
        managed = False
        db_table = 'VARIABLES_FACTOR'
        verbose_name='Variable Factor'
        verbose_name_plural='Variables Factor'
        ordering = ('id_variable_factor', )

class VariablesHasInstancias(models.Model):
    id = models.AutoField(primary_key=True)
    id_instancia = models.ForeignKey('Instancias', models.DO_NOTHING, db_column='id_instancia')
    id_variable = models.ForeignKey('Variables', models.DO_NOTHING, db_column='id_variable')

    def get_instancia_nombre(self):
        return self.id_instancia.tipo

    def get_variable_nombre(self):
        return self.id_variable.nombre_variable

    def __str__(self):
        return f'{self.get_instancia_nombre()} - {self.get_variable_nombre()}'

    class Meta:
        managed = False
        db_table = 'VARIABLES_has_INSTANCIAS'
        verbose_name='Variable con Instancia'
        verbose_name_plural='Variables con Instancias'
        unique_together = (('id_instancia', 'id_variable'),)


class VariablesProgramacion(models.Model):
    id_variable_programacion = models.BigAutoField(primary_key=True)
    id_variable = models.ForeignKey(Variables, models.DO_NOTHING, db_column='id_variable', blank=True, null=True)
    dia_entrega = models.CharField(max_length=45, blank=True, null=True)
    offset = models.CharField(max_length=45, blank=True, null=True)
    hora_ejecucion = models.TimeField(blank=True, null=True)
    observacion = models.CharField(max_length=255, blank=True, null=True)
    id_estado_qa = models.ForeignKey('Estados', models.DO_NOTHING, db_column='id_estado_qa', blank=True, null=True, related_name='variables_programacion_qa')
    id_estado_pdn = models.ForeignKey('Estados', models.DO_NOTHING, db_column='id_estado_pdn', blank=True, null=True, related_name='variables_programacion_pdn')

    def get_variable_nombre(self):
        return self.id_variable.nombre_variable

    get_variable_nombre.short_description = 'Nombre de la Variable'

    def __str__(self):
        return f'{self.get_variable_nombre()}'


    class Meta:
        managed = False
        db_table = 'VARIABLES_PROGRAMACION'
        verbose_name='Variable y Programación'
        verbose_name_plural='Variables y Programaciones'


class Variablespublicablesexcelreferencia(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    creation_date = models.DateTimeField(db_column='CREATION_DATE')  # Field name made lowercase.
    process_name = models.CharField(db_column='PROCESS_NAME', max_length=50)  # Field name made lowercase.
    process_xml_name = models.CharField(db_column='PROCESS_XML_NAME', max_length=50)  # Field name made lowercase.
    process_db_name = models.CharField(db_column='PROCESS_DB_NAME', max_length=50)  # Field name made lowercase.
    variable_name = models.CharField(db_column='VARIABLE_NAME', max_length=150)  # Field name made lowercase.
    tipo = models.CharField(db_column='TIPO', max_length=10)  # Field name made lowercase.
    liqd1 = models.SmallIntegerField(db_column='LIQD1', blank=True, null=True)  # Field name made lowercase.
    liqd2 = models.SmallIntegerField(db_column='LIQD2', blank=True, null=True)  # Field name made lowercase.
    resumen = models.SmallIntegerField(db_column='RESUMEN', blank=True, null=True)  # Field name made lowercase.
    factura = models.SmallIntegerField(db_column='FACTURA', blank=True, null=True)  # Field name made lowercase.
    ajuste = models.SmallIntegerField(db_column='AJUSTE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'VariablesPublicablesExcelReferencia'


class XmlData(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    xml_name = models.CharField(db_column='XML_NAME', max_length=400, blank=True, null=True)  # Field name made lowercase.
    variable_name = models.CharField(db_column='VARIABLE_NAME', max_length=400, blank=True, null=True)  # Field name made lowercase.
    creation_date = models.DateTimeField(db_column='CREATION_DATE', blank=True, null=True)  # Field name made lowercase.
    trade_date_begin = models.DateField(db_column='TRADE_DATE_BEGIN', blank=True, null=True)  # Field name made lowercase.
    trade_date_end = models.DateField(db_column='TRADE_DATE_END', blank=True, null=True)  # Field name made lowercase.
    key01 = models.CharField(db_column='KEY01', max_length=50, blank=True, null=True)  # Field name made lowercase.
    key02 = models.CharField(db_column='KEY02', max_length=50, blank=True, null=True)  # Field name made lowercase.
    key03 = models.CharField(db_column='KEY03', max_length=50, blank=True, null=True)  # Field name made lowercase.
    key04 = models.CharField(db_column='KEY04', max_length=50, blank=True, null=True)  # Field name made lowercase.
    key05 = models.CharField(db_column='KEY05', max_length=50, blank=True, null=True)  # Field name made lowercase.
    key06 = models.CharField(db_column='KEY06', max_length=50, blank=True, null=True)  # Field name made lowercase.
    key07 = models.CharField(db_column='KEY07', max_length=50, blank=True, null=True)  # Field name made lowercase.
    key08 = models.CharField(db_column='KEY08', max_length=50, blank=True, null=True)  # Field name made lowercase.
    key09 = models.CharField(db_column='KEY09', max_length=50, blank=True, null=True)  # Field name made lowercase.
    key10 = models.CharField(db_column='KEY10', max_length=50, blank=True, null=True)  # Field name made lowercase.
    key11 = models.CharField(db_column='KEY11', max_length=50, blank=True, null=True)  # Field name made lowercase.
    key12 = models.CharField(db_column='KEY12', max_length=50, blank=True, null=True)  # Field name made lowercase.
    key13 = models.CharField(db_column='KEY13', max_length=50, blank=True, null=True)  # Field name made lowercase.
    key14 = models.CharField(db_column='KEY14', max_length=50, blank=True, null=True)  # Field name made lowercase.
    key15 = models.CharField(db_column='KEY15', max_length=50, blank=True, null=True)  # Field name made lowercase.
    key16 = models.CharField(db_column='KEY16', max_length=50, blank=True, null=True)  # Field name made lowercase.
    key17 = models.CharField(db_column='KEY17', max_length=50, blank=True, null=True)  # Field name made lowercase.
    key18 = models.CharField(db_column='KEY18', max_length=50, blank=True, null=True)  # Field name made lowercase.
    key19 = models.CharField(db_column='KEY19', max_length=50, blank=True, null=True)  # Field name made lowercase.
    key20 = models.CharField(db_column='KEY20', max_length=50, blank=True, null=True)  # Field name made lowercase.
    key21 = models.CharField(db_column='KEY21', max_length=50, blank=True, null=True)  # Field name made lowercase.
    key22 = models.CharField(db_column='KEY22', max_length=50, blank=True, null=True)  # Field name made lowercase.
    key23 = models.CharField(db_column='KEY23', max_length=50, blank=True, null=True)  # Field name made lowercase.
    key24 = models.CharField(db_column='KEY24', max_length=50, blank=True, null=True)  # Field name made lowercase.
    key25 = models.CharField(db_column='KEY25', max_length=50, blank=True, null=True)  # Field name made lowercase.
    key26 = models.CharField(db_column='KEY26', max_length=50, blank=True, null=True)  # Field name made lowercase.
    key27 = models.CharField(db_column='KEY27', max_length=50, blank=True, null=True)  # Field name made lowercase.
    key28 = models.CharField(db_column='KEY28', max_length=50, blank=True, null=True)  # Field name made lowercase.
    key29 = models.CharField(db_column='KEY29', max_length=50, blank=True, null=True)  # Field name made lowercase.
    key30 = models.CharField(db_column='KEY30', max_length=50, blank=True, null=True)  # Field name made lowercase.
    key31 = models.CharField(db_column='KEY31', max_length=50, blank=True, null=True)  # Field name made lowercase.
    key32 = models.CharField(db_column='KEY32', max_length=50, blank=True, null=True)  # Field name made lowercase.
    key33 = models.CharField(db_column='KEY33', max_length=50, blank=True, null=True)  # Field name made lowercase.
    key34 = models.CharField(db_column='KEY34', max_length=50, blank=True, null=True)  # Field name made lowercase.
    key35 = models.CharField(db_column='KEY35', max_length=50, blank=True, null=True)  # Field name made lowercase.
    key36 = models.CharField(db_column='KEY36', max_length=50, blank=True, null=True)  # Field name made lowercase.
    key37 = models.CharField(db_column='KEY37', max_length=50, blank=True, null=True)  # Field name made lowercase.
    key38 = models.CharField(db_column='KEY38', max_length=50, blank=True, null=True)  # Field name made lowercase.
    key39 = models.CharField(db_column='KEY39', max_length=50, blank=True, null=True)  # Field name made lowercase.
    key40 = models.CharField(db_column='KEY40', max_length=50, blank=True, null=True)  # Field name made lowercase.
    key41 = models.CharField(db_column='KEY41', max_length=50, blank=True, null=True)  # Field name made lowercase.
    key42 = models.CharField(db_column='KEY42', max_length=50, blank=True, null=True)  # Field name made lowercase.
    key43 = models.CharField(db_column='KEY43', max_length=50, blank=True, null=True)  # Field name made lowercase.
    key44 = models.CharField(db_column='KEY44', max_length=50, blank=True, null=True)  # Field name made lowercase.
    key45 = models.CharField(db_column='KEY45', max_length=50, blank=True, null=True)  # Field name made lowercase.
    key46 = models.CharField(db_column='KEY46', max_length=50, blank=True, null=True)  # Field name made lowercase.
    key47 = models.CharField(db_column='KEY47', max_length=50, blank=True, null=True)  # Field name made lowercase.
    key48 = models.CharField(db_column='KEY48', max_length=50, blank=True, null=True)  # Field name made lowercase.
    key49 = models.CharField(db_column='KEY49', max_length=50, blank=True, null=True)  # Field name made lowercase.
    key50 = models.CharField(db_column='KEY50', max_length=50, blank=True, null=True)  # Field name made lowercase.
    val001 = models.CharField(db_column='VAL001', max_length=50, blank=True, null=True)  # Field name made lowercase.
    val002 = models.CharField(db_column='VAL002', max_length=50, blank=True, null=True)  # Field name made lowercase.
    val003 = models.CharField(db_column='VAL003', max_length=50, blank=True, null=True)  # Field name made lowercase.
    val004 = models.CharField(db_column='VAL004', max_length=50, blank=True, null=True)  # Field name made lowercase.
    val005 = models.CharField(db_column='VAL005', max_length=50, blank=True, null=True)  # Field name made lowercase.
    val006 = models.CharField(db_column='VAL006', max_length=50, blank=True, null=True)  # Field name made lowercase.
    val007 = models.CharField(db_column='VAL007', max_length=50, blank=True, null=True)  # Field name made lowercase.
    val008 = models.CharField(db_column='VAL008', max_length=50, blank=True, null=True)  # Field name made lowercase.
    val009 = models.CharField(db_column='VAL009', max_length=50, blank=True, null=True)  # Field name made lowercase.
    val010 = models.CharField(db_column='VAL010', max_length=50, blank=True, null=True)  # Field name made lowercase.
    val011 = models.CharField(db_column='VAL011', max_length=50, blank=True, null=True)  # Field name made lowercase.
    val012 = models.CharField(db_column='VAL012', max_length=50, blank=True, null=True)  # Field name made lowercase.
    val013 = models.CharField(db_column='VAL013', max_length=50, blank=True, null=True)  # Field name made lowercase.
    val014 = models.CharField(db_column='VAL014', max_length=50, blank=True, null=True)  # Field name made lowercase.
    val015 = models.CharField(db_column='VAL015', max_length=50, blank=True, null=True)  # Field name made lowercase.
    val016 = models.CharField(db_column='VAL016', max_length=50, blank=True, null=True)  # Field name made lowercase.
    val017 = models.CharField(db_column='VAL017', max_length=50, blank=True, null=True)  # Field name made lowercase.
    val018 = models.CharField(db_column='VAL018', max_length=50, blank=True, null=True)  # Field name made lowercase.
    val019 = models.CharField(db_column='VAL019', max_length=50, blank=True, null=True)  # Field name made lowercase.
    val020 = models.CharField(db_column='VAL020', max_length=50, blank=True, null=True)  # Field name made lowercase.
    val021 = models.CharField(db_column='VAL021', max_length=50, blank=True, null=True)  # Field name made lowercase.
    val022 = models.CharField(db_column='VAL022', max_length=50, blank=True, null=True)  # Field name made lowercase.
    val023 = models.CharField(db_column='VAL023', max_length=50, blank=True, null=True)  # Field name made lowercase.
    val024 = models.CharField(db_column='VAL024', max_length=50, blank=True, null=True)  # Field name made lowercase.
    process_name = models.CharField(db_column='PROCESS_NAME', max_length=200, blank=True, null=True)  # Field name made lowercase.
    liq_type = models.CharField(db_column='LIQ_TYPE', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'XML_DATA'


class Xmldirectory(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    creation_date = models.DateTimeField(db_column='CREATION_DATE')  # Field name made lowercase.
    xml_name = models.CharField(db_column='XML_NAME', max_length=300)  # Field name made lowercase.
    state = models.CharField(db_column='STATE', max_length=30)  # Field name made lowercase.
    process = models.CharField(db_column='PROCESS', max_length=200, blank=True, null=True)  # Field name made lowercase.
    liq_type = models.CharField(db_column='LIQ_TYPE', max_length=5, blank=True, null=True)  # Field name made lowercase.
    xml_date = models.DateField(db_column='XML_DATE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'XmlDirectory'


class Sysdiagrams(models.Model):
    name = models.CharField(max_length=128)
    principal_id = models.IntegerField()
    diagram_id = models.AutoField(primary_key=True)
    version = models.IntegerField(blank=True, null=True)
    definition = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sysdiagrams'
        unique_together = (('principal_id', 'name'),)
