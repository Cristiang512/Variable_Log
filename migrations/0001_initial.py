# Generated by Django 5.0.4 on 2024-04-16 02:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comportamientos',
            fields=[
                ('id_comportamiento', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(blank=True, max_length=60, null=True)),
            ],
            options={
                'db_table': 'COMPORTAMIENTOS',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='EjecucionesLog',
            fields=[
                ('id_ejecucion', models.BigAutoField(primary_key=True, serialize=False)),
                ('tipo_modificacion', models.CharField(blank=True, max_length=255, null=True)),
                ('columna_modificacion', models.CharField(blank=True, max_length=255, null=True)),
                ('valor_modificado', models.CharField(blank=True, max_length=255, null=True)),
                ('fecha_modificado', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'EJECUCIONES_LOG',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Estados',
            fields=[
                ('id_estado', models.AutoField(primary_key=True, serialize=False)),
                ('estado', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'ESTADOS',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Frecuencias',
            fields=[
                ('id_frecuencia', models.AutoField(primary_key=True, serialize=False)),
                ('tipo', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'FRECUENCIAS',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='JobSamData',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('external_job_id', models.IntegerField(blank=True, db_column='EXTERNAL_JOB_ID', null=True)),
                ('variable_name', models.CharField(blank=True, db_column='VARIABLE_NAME', max_length=400, null=True)),
                ('creation_date', models.DateTimeField(blank=True, db_column='CREATION_DATE', null=True)),
                ('trade_date_begin', models.DateField(blank=True, db_column='TRADE_DATE_BEGIN', null=True)),
                ('key01', models.CharField(blank=True, db_column='KEY01', max_length=50, null=True)),
                ('key11', models.CharField(blank=True, db_column='KEY11', max_length=50, null=True)),
                ('val001', models.CharField(blank=True, db_column='VAL001', max_length=50, null=True)),
                ('val002', models.CharField(blank=True, db_column='VAL002', max_length=50, null=True)),
                ('val003', models.CharField(blank=True, db_column='VAL003', max_length=50, null=True)),
                ('val004', models.CharField(blank=True, db_column='VAL004', max_length=50, null=True)),
                ('val005', models.CharField(blank=True, db_column='VAL005', max_length=50, null=True)),
                ('val006', models.CharField(blank=True, db_column='VAL006', max_length=50, null=True)),
                ('val007', models.CharField(blank=True, db_column='VAL007', max_length=50, null=True)),
                ('val008', models.CharField(blank=True, db_column='VAL008', max_length=50, null=True)),
                ('val009', models.CharField(blank=True, db_column='VAL009', max_length=50, null=True)),
                ('val010', models.CharField(blank=True, db_column='VAL010', max_length=50, null=True)),
                ('val011', models.CharField(blank=True, db_column='VAL011', max_length=50, null=True)),
                ('val012', models.CharField(blank=True, db_column='VAL012', max_length=50, null=True)),
                ('val013', models.CharField(blank=True, db_column='VAL013', max_length=50, null=True)),
                ('val014', models.CharField(blank=True, db_column='VAL014', max_length=50, null=True)),
                ('val015', models.CharField(blank=True, db_column='VAL015', max_length=50, null=True)),
                ('val016', models.CharField(blank=True, db_column='VAL016', max_length=50, null=True)),
                ('val017', models.CharField(blank=True, db_column='VAL017', max_length=50, null=True)),
                ('val018', models.CharField(blank=True, db_column='VAL018', max_length=50, null=True)),
                ('val019', models.CharField(blank=True, db_column='VAL019', max_length=50, null=True)),
                ('val020', models.CharField(blank=True, db_column='VAL020', max_length=50, null=True)),
                ('val021', models.CharField(blank=True, db_column='VAL021', max_length=50, null=True)),
                ('val022', models.CharField(blank=True, db_column='VAL022', max_length=50, null=True)),
                ('val023', models.CharField(blank=True, db_column='VAL023', max_length=50, null=True)),
                ('val024', models.CharField(blank=True, db_column='VAL024', max_length=50, null=True)),
            ],
            options={
                'db_table': 'JOB_SAM_DATA',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Mediaciones',
            fields=[
                ('id_mediacion', models.AutoField(primary_key=True, serialize=False)),
                ('tipo', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'MEDIACIONES',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Operacion',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('id_variable', models.TextField(db_column='ID_VARIABLE')),
                ('ambiente', models.CharField(db_column='AMBIENTE', max_length=10)),
                ('offset', models.CharField(db_column='OFFSET', max_length=10)),
                ('fecha_proceso', models.DateField(blank=True, db_column='FECHA_PROCESO', null=True)),
                ('fecha_ejecucion', models.DateTimeField(blank=True, db_column='FECHA_EJECUCION', null=True)),
                ('fecha_consulta', models.DateTimeField(blank=True, db_column='FECHA_CONSULTA', null=True)),
                ('file_id', models.CharField(blank=True, db_column='FILE_ID', max_length=10, null=True)),
                ('estado', models.CharField(db_column='ESTADO', max_length=20)),
                ('observaciones', models.TextField(blank=True, db_column='OBSERVACIONES', null=True)),
                ('liquidacion', models.CharField(blank=True, db_column='LIQUIDACION', max_length=15, null=True)),
                ('validar', models.CharField(blank=True, db_column='VALIDAR', max_length=1, null=True)),
            ],
            options={
                'db_table': 'OPERACION',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='OperacionDetalle',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('id_operacion', models.IntegerField(db_column='ID_OPERACION')),
                ('datos_legados', models.IntegerField(db_column='DATOS_LEGADOS')),
                ('tabla_sam', models.CharField(db_column='TABLA_SAM', max_length=20)),
                ('datos_data_raw', models.IntegerField(db_column='DATOS_DATA_RAW')),
                ('datos_sam', models.IntegerField(db_column='DATOS_SAM')),
                ('estado_conteo', models.CharField(db_column='ESTADO_CONTEO', max_length=20)),
                ('calidad_datos_estado', models.CharField(db_column='CALIDAD_DATOS_ESTADO', max_length=20)),
            ],
            options={
                'db_table': 'OPERACION_DETALLE',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='OperacionVariable',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('nombre_variable', models.TextField(db_column='NOMBRE_VARIABLE')),
                ('mediacion', models.CharField(blank=True, db_column='MEDIACION', max_length=50, null=True)),
                ('frecuencia', models.CharField(blank=True, db_column='FRECUENCIA', max_length=30, null=True)),
                ('uom', models.CharField(blank=True, db_column='UOM', max_length=30, null=True)),
                ('fuente', models.CharField(blank=True, db_column='FUENTE', max_length=30, null=True)),
                ('tipo', models.CharField(blank=True, db_column='TIPO', max_length=30, null=True)),
                ('fecha_actualizacion', models.DateTimeField(db_column='FECHA_ACTUALIZACION')),
            ],
            options={
                'db_table': 'OPERACION_VARIABLE',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Procesos',
            fields=[
                ('id_proceso', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_proceso', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'PROCESOS',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ProcesosSam',
            fields=[
                ('id_proceso_sam', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'PROCESOS_SAM',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Programas',
            fields=[
                ('id_programa', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(blank=True, max_length=60, null=True)),
            ],
            options={
                'db_table': 'PROGRAMAS',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Sysdiagrams',
            fields=[
                ('name', models.CharField(max_length=128)),
                ('principal_id', models.IntegerField()),
                ('diagram_id', models.AutoField(primary_key=True, serialize=False)),
                ('version', models.IntegerField(blank=True, null=True)),
                ('definition', models.BinaryField(blank=True, max_length='max', null=True)),
            ],
            options={
                'db_table': 'sysdiagrams',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tipos',
            fields=[
                ('id_tipo', models.AutoField(primary_key=True, serialize=False)),
                ('tipo', models.CharField(blank=True, max_length=60, null=True)),
            ],
            options={
                'db_table': 'TIPOS',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Uom',
            fields=[
                ('id_uom', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(blank=True, max_length=60, null=True)),
            ],
            options={
                'db_table': 'UOM',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id_usuario', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=255, null=True)),
                ('correo', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'USUARIOS',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Variables',
            fields=[
                ('id_variable', models.BigAutoField(primary_key=True, serialize=False)),
                ('nombre_variable', models.CharField(blank=True, max_length=255, null=True)),
                ('fecha_modificacion', models.DateTimeField(blank=True, null=True)),
                ('sam', models.CharField(blank=True, max_length=45, null=True)),
                ('ods', models.CharField(blank=True, max_length=45, null=True)),
                ('id_comportamiento', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'VARIABLES',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Variablesborrador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_name', models.CharField(blank=True, db_column='DATA_NAME', max_length=4000, null=True)),
                ('sam', models.CharField(blank=True, db_column='SAM', max_length=4000, null=True)),
                ('ods', models.CharField(blank=True, db_column='ODS', max_length=4000, null=True)),
                ('tipo', models.CharField(blank=True, db_column='TIPO', max_length=4000, null=True)),
                ('uom', models.CharField(blank=True, db_column='UOM', max_length=4000, null=True)),
                ('frecuencia', models.CharField(blank=True, db_column='FRECUENCIA', max_length=4000, null=True)),
                ('mediacion', models.CharField(blank=True, db_column='MEDIACION', max_length=4000, null=True)),
                ('programa', models.CharField(blank=True, db_column='PROGRAMA', max_length=4000, null=True)),
                ('comportamiento', models.CharField(blank=True, db_column='COMPORTAMIENTO', max_length=4000, null=True)),
                ('variable_factor', models.CharField(blank=True, db_column='VARIABLE_FACTOR', max_length=4000, null=True)),
            ],
            options={
                'db_table': 'VARIABLESBORRADOR',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='VariablesFactor',
            fields=[
                ('id_variable_factor', models.AutoField(primary_key=True, serialize=False)),
                ('factor', models.CharField(blank=True, max_length=60, null=True)),
            ],
            options={
                'db_table': 'VARIABLES_FACTOR',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='VariablesProgramacion',
            fields=[
                ('id_variable_programacion', models.BigAutoField(primary_key=True, serialize=False)),
                ('dia_entrega', models.CharField(blank=True, max_length=45, null=True)),
                ('offset', models.CharField(blank=True, max_length=45, null=True)),
                ('hora_ejecucion', models.DateTimeField(blank=True, null=True)),
                ('observacion', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'VARIABLES_PROGRAMACION',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Variablespublicablesexcelreferencia',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('creation_date', models.DateTimeField(db_column='CREATION_DATE')),
                ('process_name', models.CharField(db_column='PROCESS_NAME', max_length=50)),
                ('process_xml_name', models.CharField(db_column='PROCESS_XML_NAME', max_length=50)),
                ('process_db_name', models.CharField(db_column='PROCESS_DB_NAME', max_length=50)),
                ('variable_name', models.CharField(db_column='VARIABLE_NAME', max_length=150)),
                ('tipo', models.CharField(db_column='TIPO', max_length=10)),
                ('liqd1', models.SmallIntegerField(blank=True, db_column='LIQD1', null=True)),
                ('liqd2', models.SmallIntegerField(blank=True, db_column='LIQD2', null=True)),
                ('resumen', models.SmallIntegerField(blank=True, db_column='RESUMEN', null=True)),
                ('factura', models.SmallIntegerField(blank=True, db_column='FACTURA', null=True)),
                ('ajuste', models.SmallIntegerField(blank=True, db_column='AJUSTE', null=True)),
            ],
            options={
                'db_table': 'VariablesPublicablesExcelReferencia',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='XmlData',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('xml_name', models.CharField(blank=True, db_column='XML_NAME', max_length=400, null=True)),
                ('variable_name', models.CharField(blank=True, db_column='VARIABLE_NAME', max_length=400, null=True)),
                ('creation_date', models.DateTimeField(blank=True, db_column='CREATION_DATE', null=True)),
                ('trade_date_begin', models.DateField(blank=True, db_column='TRADE_DATE_BEGIN', null=True)),
                ('trade_date_end', models.DateField(blank=True, db_column='TRADE_DATE_END', null=True)),
                ('key01', models.CharField(blank=True, db_column='KEY01', max_length=50, null=True)),
                ('key02', models.CharField(blank=True, db_column='KEY02', max_length=50, null=True)),
                ('key03', models.CharField(blank=True, db_column='KEY03', max_length=50, null=True)),
                ('key04', models.CharField(blank=True, db_column='KEY04', max_length=50, null=True)),
                ('key05', models.CharField(blank=True, db_column='KEY05', max_length=50, null=True)),
                ('key06', models.CharField(blank=True, db_column='KEY06', max_length=50, null=True)),
                ('key07', models.CharField(blank=True, db_column='KEY07', max_length=50, null=True)),
                ('key08', models.CharField(blank=True, db_column='KEY08', max_length=50, null=True)),
                ('key09', models.CharField(blank=True, db_column='KEY09', max_length=50, null=True)),
                ('key10', models.CharField(blank=True, db_column='KEY10', max_length=50, null=True)),
                ('key11', models.CharField(blank=True, db_column='KEY11', max_length=50, null=True)),
                ('key12', models.CharField(blank=True, db_column='KEY12', max_length=50, null=True)),
                ('key13', models.CharField(blank=True, db_column='KEY13', max_length=50, null=True)),
                ('key14', models.CharField(blank=True, db_column='KEY14', max_length=50, null=True)),
                ('key15', models.CharField(blank=True, db_column='KEY15', max_length=50, null=True)),
                ('key16', models.CharField(blank=True, db_column='KEY16', max_length=50, null=True)),
                ('key17', models.CharField(blank=True, db_column='KEY17', max_length=50, null=True)),
                ('key18', models.CharField(blank=True, db_column='KEY18', max_length=50, null=True)),
                ('key19', models.CharField(blank=True, db_column='KEY19', max_length=50, null=True)),
                ('key20', models.CharField(blank=True, db_column='KEY20', max_length=50, null=True)),
                ('key21', models.CharField(blank=True, db_column='KEY21', max_length=50, null=True)),
                ('key22', models.CharField(blank=True, db_column='KEY22', max_length=50, null=True)),
                ('key23', models.CharField(blank=True, db_column='KEY23', max_length=50, null=True)),
                ('key24', models.CharField(blank=True, db_column='KEY24', max_length=50, null=True)),
                ('key25', models.CharField(blank=True, db_column='KEY25', max_length=50, null=True)),
                ('key26', models.CharField(blank=True, db_column='KEY26', max_length=50, null=True)),
                ('key27', models.CharField(blank=True, db_column='KEY27', max_length=50, null=True)),
                ('key28', models.CharField(blank=True, db_column='KEY28', max_length=50, null=True)),
                ('key29', models.CharField(blank=True, db_column='KEY29', max_length=50, null=True)),
                ('key30', models.CharField(blank=True, db_column='KEY30', max_length=50, null=True)),
                ('key31', models.CharField(blank=True, db_column='KEY31', max_length=50, null=True)),
                ('key32', models.CharField(blank=True, db_column='KEY32', max_length=50, null=True)),
                ('key33', models.CharField(blank=True, db_column='KEY33', max_length=50, null=True)),
                ('key34', models.CharField(blank=True, db_column='KEY34', max_length=50, null=True)),
                ('key35', models.CharField(blank=True, db_column='KEY35', max_length=50, null=True)),
                ('key36', models.CharField(blank=True, db_column='KEY36', max_length=50, null=True)),
                ('key37', models.CharField(blank=True, db_column='KEY37', max_length=50, null=True)),
                ('key38', models.CharField(blank=True, db_column='KEY38', max_length=50, null=True)),
                ('key39', models.CharField(blank=True, db_column='KEY39', max_length=50, null=True)),
                ('key40', models.CharField(blank=True, db_column='KEY40', max_length=50, null=True)),
                ('key41', models.CharField(blank=True, db_column='KEY41', max_length=50, null=True)),
                ('key42', models.CharField(blank=True, db_column='KEY42', max_length=50, null=True)),
                ('key43', models.CharField(blank=True, db_column='KEY43', max_length=50, null=True)),
                ('key44', models.CharField(blank=True, db_column='KEY44', max_length=50, null=True)),
                ('key45', models.CharField(blank=True, db_column='KEY45', max_length=50, null=True)),
                ('key46', models.CharField(blank=True, db_column='KEY46', max_length=50, null=True)),
                ('key47', models.CharField(blank=True, db_column='KEY47', max_length=50, null=True)),
                ('key48', models.CharField(blank=True, db_column='KEY48', max_length=50, null=True)),
                ('key49', models.CharField(blank=True, db_column='KEY49', max_length=50, null=True)),
                ('key50', models.CharField(blank=True, db_column='KEY50', max_length=50, null=True)),
                ('val001', models.CharField(blank=True, db_column='VAL001', max_length=50, null=True)),
                ('val002', models.CharField(blank=True, db_column='VAL002', max_length=50, null=True)),
                ('val003', models.CharField(blank=True, db_column='VAL003', max_length=50, null=True)),
                ('val004', models.CharField(blank=True, db_column='VAL004', max_length=50, null=True)),
                ('val005', models.CharField(blank=True, db_column='VAL005', max_length=50, null=True)),
                ('val006', models.CharField(blank=True, db_column='VAL006', max_length=50, null=True)),
                ('val007', models.CharField(blank=True, db_column='VAL007', max_length=50, null=True)),
                ('val008', models.CharField(blank=True, db_column='VAL008', max_length=50, null=True)),
                ('val009', models.CharField(blank=True, db_column='VAL009', max_length=50, null=True)),
                ('val010', models.CharField(blank=True, db_column='VAL010', max_length=50, null=True)),
                ('val011', models.CharField(blank=True, db_column='VAL011', max_length=50, null=True)),
                ('val012', models.CharField(blank=True, db_column='VAL012', max_length=50, null=True)),
                ('val013', models.CharField(blank=True, db_column='VAL013', max_length=50, null=True)),
                ('val014', models.CharField(blank=True, db_column='VAL014', max_length=50, null=True)),
                ('val015', models.CharField(blank=True, db_column='VAL015', max_length=50, null=True)),
                ('val016', models.CharField(blank=True, db_column='VAL016', max_length=50, null=True)),
                ('val017', models.CharField(blank=True, db_column='VAL017', max_length=50, null=True)),
                ('val018', models.CharField(blank=True, db_column='VAL018', max_length=50, null=True)),
                ('val019', models.CharField(blank=True, db_column='VAL019', max_length=50, null=True)),
                ('val020', models.CharField(blank=True, db_column='VAL020', max_length=50, null=True)),
                ('val021', models.CharField(blank=True, db_column='VAL021', max_length=50, null=True)),
                ('val022', models.CharField(blank=True, db_column='VAL022', max_length=50, null=True)),
                ('val023', models.CharField(blank=True, db_column='VAL023', max_length=50, null=True)),
                ('val024', models.CharField(blank=True, db_column='VAL024', max_length=50, null=True)),
                ('process_name', models.CharField(blank=True, db_column='PROCESS_NAME', max_length=200, null=True)),
                ('liq_type', models.CharField(blank=True, db_column='LIQ_TYPE', max_length=10, null=True)),
            ],
            options={
                'db_table': 'XML_DATA',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Xmldirectory',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('creation_date', models.DateTimeField(db_column='CREATION_DATE')),
                ('xml_name', models.CharField(db_column='XML_NAME', max_length=300)),
                ('state', models.CharField(db_column='STATE', max_length=30)),
                ('process', models.CharField(blank=True, db_column='PROCESS', max_length=200, null=True)),
                ('liq_type', models.CharField(blank=True, db_column='LIQ_TYPE', max_length=5, null=True)),
                ('xml_date', models.DateField(blank=True, db_column='XML_DATE', null=True)),
            ],
            options={
                'db_table': 'XmlDirectory',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ProcesosHasVariables',
            fields=[
                ('id_proceso', models.OneToOneField(db_column='id_proceso', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='Bitacora.procesos')),
            ],
            options={
                'db_table': 'PROCESOS_has_VARIABLES',
                'managed': False,
            },
        ),
    ]
