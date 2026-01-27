
from django.db import models
import os
from django.utils.text import slugify
def path_contratos_por_empresa(instance, filename):
    # Como es un CharField, instance.id_concesionario es solo el ID (ej: "123")
    try:
        # Buscamos manualmente el nombre de la empresa usando el ID
        # Nota: Usamos .using('catastro') porque tus modelos están en esa BD
        empresa = Concesionarios.objects.using('catastro').get(id=instance.id_concesionario)
        nombre_carpeta = slugify(empresa.concesionario)
    except:
        # Si algo falla (empresa no encontrada), lo manda a una carpeta genérica
        nombre_carpeta = "desconocido"
    
    return os.path.join('Contratos', nombre_carpeta, filename)

class AnotacionesLineas(models.Model):
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.
    nombre = models.TextField(blank=True, null=True)
    observaciones = models.TextField(blank=True, null=True)
    expediente = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'anotaciones_lineas'


class AnotacionesPoligonos(models.Model):
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.
    nombre = models.TextField(blank=True, null=True)
    observaciones = models.TextField(blank=True, null=True)
    expediente = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'anotaciones_poligonos'


class AnotacionesPuntos(models.Model):
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.
    nombre = models.TextField(blank=True, null=True)
    observaciones = models.TextField(blank=True, null=True)
    expediente = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'anotaciones_puntos'


class AppContratos(models.Model):
    relacion_id_concesionario = models.CharField(max_length=255)
    pago_cano = models.BooleanField()
    explotacion = models.CharField(max_length=255)
    mineral_explotacion = models.CharField(max_length=255)
    exploracion = models.CharField(max_length=255)
    iia = models.CharField(max_length=255)
    activo = models.BooleanField()
    fecha_ini = models.DateField(blank=True, null=True)
    fecha_fin = models.DateField(blank=True, null=True)
    pago_regalias = models.BooleanField()
    id = models.BigAutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'app_contratos'


class AppSimsaexpedientescontratos(models.Model):
    id = models.BigAutoField(primary_key=True)
    nro_expediente = models.CharField(max_length=255)
    id_contrato = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'app_simsaexpedientescontratos'
        unique_together = (('nro_expediente', 'id_contrato'),)


class AreasProtegidas(models.Model):
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.
    nombre = models.TextField(blank=True, null=True)
    categoria = models.TextField(blank=True, null=True)
    rotulo = models.TextField(blank=True, null=True)
    f_area = models.FloatField(blank=True, null=True)
    nombre_res = models.TextField(blank=True, null=True)
    expediente = models.TextField(blank=True, null=True)
    observacion = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'areas_protegidas'


class AreasSecretaria(models.Model):
    id = models.IntegerField(primary_key=True)
    area = models.TextField()
    nombre = models.TextField()

    class Meta:
        managed = False
        db_table = 'areas_secretaria'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Borrame(models.Model):
    expediente = models.IntegerField(blank=True, null=True)
    id_conc = models.IntegerField(blank=True, null=True)
    conc = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'borrame'


class Canon(models.Model):
    id = models.IntegerField(primary_key=True)
    yacencia = models.TextField()
    fecha = models.DateField()
    observacion = models.TextField(blank=True, null=True)
    canon = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'canon'


class CanonMunicipios(models.Model):
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.
    nombre = models.CharField(max_length=254, blank=True, null=True)
    ley = models.CharField(max_length=254, blank=True, null=True)
    departamen = models.CharField(max_length=254, blank=True, null=True)
    shape_leng = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'canon_municipios'


class CanonObs(models.Model):
    sit_legal = models.ForeignKey('SitLegal', models.DO_NOTHING)
    expediente = models.IntegerField()
    fecha = models.DateField(blank=True, null=True)
    raz_social = models.TextField(blank=True, null=True)
    observacion = models.TextField(blank=True, null=True)
    fecha_especulativa = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'canon_obs'


class CanonPago(models.Model):
    pk = models.CompositePrimaryKey('expediente', 'num_semestre', 'toshi')
    expediente = models.IntegerField()
    num_semestre = models.IntegerField()
    toshi = models.IntegerField()
    fecha = models.DateField(blank=True, null=True)
    canon = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    meses = models.IntegerField(blank=True, null=True)
    multa = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    importe = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    porcentaje = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'canon_pago'


class CanterasF2(models.Model):
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.
    jerarquia = models.TextField(blank=True, null=True)
    expediente = models.IntegerField()
    nombre = models.TextField(blank=True, null=True)
    concesionario = models.TextField(blank=True, null=True)
    mineral = models.TextField(blank=True, null=True)
    mineral_iia = models.TextField(blank=True, null=True)
    estado = models.TextField(blank=True, null=True)
    privada = models.BooleanField(blank=True, null=True)
    fecha_inicio = models.DateTimeField(blank=True, null=True)
    fecha_concesion_oficio = models.DateField(blank=True, null=True)
    fecha_aprobacion_mensura = models.DateField(blank=True, null=True)
    fecha_publicacion_archivo = models.DateField(blank=True, null=True)
    archivo_prov = models.BooleanField(blank=True, null=True)
    departamento = models.TextField(blank=True, null=True)
    municipio = models.TextField(blank=True, null=True)
    lugar = models.TextField(blank=True, null=True)
    nro_orden = models.IntegerField(blank=True, null=True)
    servidumbres = models.TextField(blank=True, null=True)
    observaciones = models.TextField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    create_date = models.DateTimeField()
    informe_ambiente = models.DateField(blank=True, null=True)
    rio = models.TextField(blank=True, null=True)
    seca = models.BooleanField(blank=True, null=True)
    fecha_reg_decanon = models.BooleanField()
    fecha_reg_aconfirmar = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'canteras_f2'


class CanterasF3(models.Model):
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.
    jerarquia = models.TextField(blank=True, null=True)
    expediente = models.IntegerField()
    nombre = models.TextField(blank=True, null=True)
    concesionario = models.TextField(blank=True, null=True)
    mineral = models.TextField(blank=True, null=True)
    mineral_iia = models.TextField(blank=True, null=True)
    estado = models.TextField(blank=True, null=True)
    privada = models.BooleanField(blank=True, null=True)
    fecha_inicio = models.DateTimeField(blank=True, null=True)
    fecha_concesion_oficio = models.DateField(blank=True, null=True)
    fecha_aprobacion_mensura = models.DateField(blank=True, null=True)
    fecha_publicacion_archivo = models.DateField(blank=True, null=True)
    archivo_prov = models.BooleanField(blank=True, null=True)
    departamento = models.TextField(blank=True, null=True)
    municipio = models.TextField(blank=True, null=True)
    lugar = models.TextField(blank=True, null=True)
    nro_orden = models.IntegerField(blank=True, null=True)
    servidumbres = models.TextField(blank=True, null=True)
    observaciones = models.TextField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    create_date = models.DateTimeField()
    informe_ambiente = models.DateField(blank=True, null=True)
    rio = models.TextField(blank=True, null=True)
    seca = models.BooleanField(blank=True, null=True)
    fecha_reg_decanon = models.BooleanField()
    fecha_reg_aconfirmar = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'canteras_f3'


class CanterasF4(models.Model):
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.
    jerarquia = models.TextField(blank=True, null=True)
    expediente = models.IntegerField()
    nombre = models.TextField(blank=True, null=True)
    concesionario = models.TextField(blank=True, null=True)
    mineral = models.TextField(blank=True, null=True)
    mineral_iia = models.TextField(blank=True, null=True)
    estado = models.TextField(blank=True, null=True)
    privada = models.BooleanField(blank=True, null=True)
    fecha_inicio = models.DateTimeField(blank=True, null=True)
    fecha_concesion_oficio = models.DateField(blank=True, null=True)
    fecha_aprobacion_mensura = models.DateField(blank=True, null=True)
    fecha_publicacion_archivo = models.DateField(blank=True, null=True)
    archivo_prov = models.BooleanField(blank=True, null=True)
    departamento = models.TextField(blank=True, null=True)
    municipio = models.TextField(blank=True, null=True)
    lugar = models.TextField(blank=True, null=True)
    nro_orden = models.IntegerField(blank=True, null=True)
    servidumbres = models.TextField(blank=True, null=True)
    observaciones = models.TextField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    create_date = models.DateTimeField()
    informe_ambiente = models.DateField(blank=True, null=True)
    rio = models.TextField(blank=True, null=True)
    seca = models.BooleanField(blank=True, null=True)
    fecha_reg_decanon = models.BooleanField()
    fecha_reg_aconfirmar = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'canteras_f4'


class CateosF2(models.Model):
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.
    jerarquia = models.TextField(blank=True, null=True)
    expediente = models.IntegerField(blank=True, null=True)
    concesionario = models.TextField(blank=True, null=True)
    categoria = models.TextField(blank=True, null=True)
    estado = models.TextField(blank=True, null=True)
    fecha_inicio = models.DateTimeField(blank=True, null=True)
    fecha_publicacion_archivo = models.DateField(blank=True, null=True)
    remsa = models.TextField(blank=True, null=True)  # This field type is a guess.
    archivo_prov = models.BooleanField(blank=True, null=True)
    departamento = models.TextField(blank=True, null=True)
    municipio = models.TextField(blank=True, null=True)
    lugar = models.TextField(blank=True, null=True)
    nro_orden = models.IntegerField(blank=True, null=True)
    observaciones = models.TextField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    create_date = models.DateTimeField()
    informe_ambiente = models.DateField(blank=True, null=True)
    fecha_concesion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cateos_f2'


class CateosF3(models.Model):
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.
    jerarquia = models.TextField(blank=True, null=True)
    expediente = models.IntegerField(blank=True, null=True)
    concesionario = models.TextField(blank=True, null=True)
    categoria = models.TextField(blank=True, null=True)
    estado = models.TextField(blank=True, null=True)
    fecha_inicio = models.DateTimeField(blank=True, null=True)
    fecha_publicacion_archivo = models.DateField(blank=True, null=True)
    remsa = models.TextField(blank=True, null=True)  # This field type is a guess.
    archivo_prov = models.BooleanField(blank=True, null=True)
    departamento = models.TextField(blank=True, null=True)
    municipio = models.TextField(blank=True, null=True)
    lugar = models.TextField(blank=True, null=True)
    nro_orden = models.IntegerField(blank=True, null=True)
    observaciones = models.TextField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    create_date = models.DateTimeField()
    informe_ambiente = models.DateField(blank=True, null=True)
    fecha_concesion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cateos_f3'


class CateosF4(models.Model):
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.
    jerarquia = models.TextField(blank=True, null=True)
    expediente = models.IntegerField(blank=True, null=True)
    concesionario = models.TextField(blank=True, null=True)
    categoria = models.TextField(blank=True, null=True)
    estado = models.TextField(blank=True, null=True)
    fecha_inicio = models.DateTimeField(blank=True, null=True)
    fecha_publicacion_archivo = models.DateField(blank=True, null=True)
    remsa = models.TextField(blank=True, null=True)  # This field type is a guess.
    archivo_prov = models.BooleanField(blank=True, null=True)
    departamento = models.TextField(blank=True, null=True)
    municipio = models.TextField(blank=True, null=True)
    lugar = models.TextField(blank=True, null=True)
    nro_orden = models.IntegerField(blank=True, null=True)
    observaciones = models.TextField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    create_date = models.DateTimeField()
    informe_ambiente = models.DateField(blank=True, null=True)
    fecha_concesion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cateos_f4'


class Codfajas(models.Model):
    id = models.IntegerField(primary_key=True)
    codigofaja = models.IntegerField(blank=True, null=True)
    nombre = models.CharField(max_length=40, blank=True, null=True)
    posgar94 = models.IntegerField(blank=True, null=True)
    posgar07 = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'codfajas'


class Concesionarios(models.Model):
    id = models.IntegerField(primary_key=True)
    concesionario = models.TextField(unique=True)
    direc_cedula = models.TextField(blank=True, null=True)
    telefono = models.TextField(blank=True, null=True)
    correo = models.TextField(blank=True, null=True)
    cuit = models.TextField(blank=True, null=True)
    fecha_ult_modif = models.DateField(blank=True, null=True)
    dni = models.IntegerField(unique=True, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'concesionarios'


class ConveniosF2(models.Model):
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.
    expediente = models.TextField(blank=True, null=True)
    tipo = models.TextField(blank=True, null=True)
    nombre = models.TextField(blank=True, null=True)
    concesionario = models.TextField(blank=True, null=True)
    resolucion = models.TextField(blank=True, null=True)
    activo = models.BooleanField(blank=True, null=True)
    fecha_inicio = models.DateField(blank=True, null=True)
    fecha_caducidad = models.DateField(blank=True, null=True)
    departamento = models.TextField(blank=True, null=True)
    municipio = models.TextField(blank=True, null=True)
    lugar = models.TextField(blank=True, null=True)
    mineral = models.TextField(blank=True, null=True)
    observaciones = models.TextField(blank=True, null=True)
    informe_ambiente = models.DateField(blank=True, null=True)
    rio = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'convenios_f2'


class ConveniosF3(models.Model):
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.
    expediente = models.TextField(blank=True, null=True)
    tipo = models.TextField(blank=True, null=True)
    nombre = models.TextField(blank=True, null=True)
    concesionario = models.TextField(blank=True, null=True)
    resolucion = models.TextField(blank=True, null=True)
    activo = models.BooleanField(blank=True, null=True)
    fecha_inicio = models.DateField(blank=True, null=True)
    fecha_caducidad = models.DateField(blank=True, null=True)
    departamento = models.TextField(blank=True, null=True)
    municipio = models.TextField(blank=True, null=True)
    lugar = models.TextField(blank=True, null=True)
    mineral = models.TextField(blank=True, null=True)
    observaciones = models.TextField(blank=True, null=True)
    informe_ambiente = models.DateField(blank=True, null=True)
    rio = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'convenios_f3'


class ConveniosF4(models.Model):
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.
    expediente = models.TextField(blank=True, null=True)
    tipo = models.TextField(blank=True, null=True)
    nombre = models.TextField(blank=True, null=True)
    concesionario = models.TextField(blank=True, null=True)
    resolucion = models.TextField(blank=True, null=True)
    activo = models.BooleanField(blank=True, null=True)
    fecha_inicio = models.DateField(blank=True, null=True)
    fecha_caducidad = models.DateField(blank=True, null=True)
    departamento = models.TextField(blank=True, null=True)
    municipio = models.TextField(blank=True, null=True)
    lugar = models.TextField(blank=True, null=True)
    mineral = models.TextField(blank=True, null=True)
    observaciones = models.TextField(blank=True, null=True)
    informe_ambiente = models.DateField(blank=True, null=True)
    rio = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'convenios_f4'


class Departamentos(models.Model):
    departamento = models.TextField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'departamentos'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Estado(models.Model):
    estado = models.TextField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'estado'


class ExcentricosF2(models.Model):
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.
    observaciones = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'excentricos_f2'


class ExcentricosF3(models.Model):
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.
    observaciones = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'excentricos_f3'


class ExcentricosF4(models.Model):
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.
    observaciones = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'excentricos_f4'


class GlaciaresUtm19(models.Model):
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.
    provincia = models.CharField(max_length=254, blank=True, null=True)
    cuenca = models.CharField(max_length=254, blank=True, null=True)
    subcuenca = models.CharField(max_length=254, blank=True, null=True)
    codigo_cue = models.CharField(max_length=254, blank=True, null=True)
    id_local = models.CharField(max_length=254, blank=True, null=True)
    tipo_geofo = models.CharField(max_length=254, blank=True, null=True)
    id_glims = models.CharField(max_length=254, blank=True, null=True)
    nombre_com = models.CharField(max_length=254, blank=True, null=True)
    clas_prima = models.CharField(max_length=254, blank=True, null=True)
    forma = models.CharField(max_length=254, blank=True, null=True)
    frente = models.CharField(max_length=254, blank=True, null=True)
    perf_long = models.CharField(max_length=254, blank=True, null=True)
    fuente_ali = models.CharField(max_length=254, blank=True, null=True)
    act_lengua = models.CharField(max_length=254, blank=True, null=True)
    morena_1 = models.CharField(max_length=254, blank=True, null=True)
    morena_2 = models.CharField(max_length=254, blank=True, null=True)
    cob_lengua = models.CharField(max_length=254, blank=True, null=True)
    origen_ge = models.CharField(max_length=254, blank=True, null=True)
    act_ge = models.CharField(max_length=254, blank=True, null=True)
    forma_ge = models.CharField(max_length=254, blank=True, null=True)
    estruct_i = models.CharField(max_length=254, blank=True, null=True)
    estruct_ii = models.CharField(max_length=254, blank=True, null=True)
    longitud = models.FloatField(blank=True, null=True)
    latitud = models.FloatField(blank=True, null=True)
    area = models.FloatField(blank=True, null=True)
    largo_tota = models.BigIntegerField(blank=True, null=True)
    h_max_tota = models.BigIntegerField(blank=True, null=True)
    h_media_to = models.BigIntegerField(blank=True, null=True)
    h_min_tota = models.BigIntegerField(blank=True, null=True)
    pendiente = models.FloatField(blank=True, null=True)
    orientacio = models.CharField(max_length=254, blank=True, null=True)
    h_max_parc = models.BigIntegerField(blank=True, null=True)
    h_media_pa = models.BigIntegerField(blank=True, null=True)
    h_min_parc = models.BigIntegerField(blank=True, null=True)
    img_ba_f = models.CharField(max_length=254, blank=True, null=True)
    img_ba_s = models.CharField(max_length=254, blank=True, null=True)
    img_ap_f = models.CharField(max_length=254, blank=True, null=True)
    img_ap_s = models.CharField(max_length=254, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glaciares_utm19'


class GlaciaresUtm20(models.Model):
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.
    provincia = models.CharField(max_length=255, blank=True, null=True)
    cuenca = models.CharField(max_length=255, blank=True, null=True)
    subcuenca = models.CharField(max_length=255, blank=True, null=True)
    codigo_cue = models.CharField(max_length=255, blank=True, null=True)
    id_local = models.CharField(max_length=255, blank=True, null=True)
    tipo_geofo = models.CharField(max_length=255, blank=True, null=True)
    id_glims = models.CharField(max_length=255, blank=True, null=True)
    nombre_com = models.CharField(max_length=255, blank=True, null=True)
    clas_prima = models.CharField(max_length=255, blank=True, null=True)
    forma = models.CharField(max_length=255, blank=True, null=True)
    frente = models.CharField(max_length=255, blank=True, null=True)
    perf_long = models.CharField(max_length=255, blank=True, null=True)
    fuente_ali = models.CharField(max_length=255, blank=True, null=True)
    act_lengua = models.CharField(max_length=255, blank=True, null=True)
    morena_1 = models.CharField(max_length=255, blank=True, null=True)
    morena_2 = models.CharField(max_length=255, blank=True, null=True)
    cob_lengua = models.CharField(max_length=255, blank=True, null=True)
    origen_ge = models.CharField(max_length=255, blank=True, null=True)
    act_ge = models.CharField(max_length=255, blank=True, null=True)
    forma_ge = models.CharField(max_length=255, blank=True, null=True)
    estruct_i = models.CharField(max_length=255, blank=True, null=True)
    estruct_ii = models.CharField(max_length=255, blank=True, null=True)
    longitud = models.FloatField(blank=True, null=True)
    latitud = models.FloatField(blank=True, null=True)
    area = models.FloatField(blank=True, null=True)
    largo_tota = models.FloatField(blank=True, null=True)
    h_max_tota = models.FloatField(blank=True, null=True)
    h_media_to = models.FloatField(blank=True, null=True)
    h_min_tota = models.FloatField(blank=True, null=True)
    pendiente = models.FloatField(blank=True, null=True)
    orientacio = models.CharField(max_length=255, blank=True, null=True)
    h_max_parc = models.FloatField(blank=True, null=True)
    h_media_pa = models.FloatField(blank=True, null=True)
    h_min_parc = models.FloatField(blank=True, null=True)
    img_ba_f = models.CharField(max_length=255, blank=True, null=True)
    img_ba_s = models.CharField(max_length=255, blank=True, null=True)
    img_ap_f = models.CharField(max_length=255, blank=True, null=True)
    img_ap_s = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glaciares_utm20'


class GruposMinerosF2(models.Model):
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.
    expediente = models.IntegerField(blank=True, null=True)
    concesionario = models.TextField(blank=True, null=True)
    departamento = models.TextField(blank=True, null=True)
    municipio = models.TextField(blank=True, null=True)
    lugar = models.TextField(blank=True, null=True)
    observaciones = models.TextField(blank=True, null=True)
    nombre = models.TextField(blank=True, null=True)
    minas = models.TextField(blank=True, null=True)
    fecha_inicio = models.DateTimeField(blank=True, null=True)
    nro_orden = models.SmallIntegerField(blank=True, null=True)
    estado = models.TextField(blank=True, null=True)
    coordenadas = models.TextField(blank=True, null=True)
    informe_ambiente = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'grupos_mineros_f2'


class GruposMinerosF3(models.Model):
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.
    expediente = models.IntegerField(blank=True, null=True)
    concesionario = models.TextField(blank=True, null=True)
    departamento = models.TextField(blank=True, null=True)
    municipio = models.TextField(blank=True, null=True)
    lugar = models.TextField(blank=True, null=True)
    observaciones = models.TextField(blank=True, null=True)
    nombre = models.TextField(blank=True, null=True)
    minas = models.TextField(blank=True, null=True)
    fecha_inicio = models.DateTimeField(blank=True, null=True)
    nro_orden = models.SmallIntegerField(blank=True, null=True)
    estado = models.TextField(blank=True, null=True)
    coordenadas = models.TextField(blank=True, null=True)
    informe_ambiente = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'grupos_mineros_f3'


class GruposMinerosF4(models.Model):
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.
    expediente = models.IntegerField(blank=True, null=True)
    concesionario = models.TextField(blank=True, null=True)
    departamento = models.TextField(blank=True, null=True)
    municipio = models.TextField(blank=True, null=True)
    lugar = models.TextField(blank=True, null=True)
    observaciones = models.TextField(blank=True, null=True)
    nombre = models.TextField(blank=True, null=True)
    minas = models.TextField(blank=True, null=True)
    fecha_inicio = models.DateTimeField(blank=True, null=True)
    nro_orden = models.SmallIntegerField(blank=True, null=True)
    estado = models.TextField(blank=True, null=True)
    coordenadas = models.TextField(blank=True, null=True)
    informe_ambiente = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'grupos_mineros_f4'


class ImpactoAmbiental(models.Model):
    expediente = models.IntegerField()
    etapa = models.TextField(blank=True, null=True)
    bianual = models.TextField(blank=True, null=True)
    resultado = models.TextField(blank=True, null=True)
    fecha_entrada = models.DateField(blank=True, null=True)
    fecha_salida = models.DateField(blank=True, null=True)
    n_resolucion = models.IntegerField(blank=True, null=True)
    mineral = models.TextField(blank=True, null=True)
    observacion = models.TextField(blank=True, null=True)
    responsable = models.TextField(blank=True, null=True)
    visado = models.BooleanField(blank=True, null=True)
    evaluador = models.TextField(blank=True, null=True)
    fecha_renovacion = models.DateField(blank=True, null=True)
    foja_entrada = models.IntegerField(blank=True, null=True)
    foja_salida = models.IntegerField(blank=True, null=True)
    cd = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'impacto_ambiental'


class Inspecciones(models.Model):
    pk = models.CompositePrimaryKey('expediente', 'fecha')
    expediente = models.IntegerField()
    fecha = models.DateField()
    lugar = models.TextField(blank=True, null=True)
    inspectores = models.TextField(blank=True, null=True)
    admin_inspeccion = models.TextField(blank=True, null=True)
    admin_saf = models.TextField(blank=True, null=True)
    paralizado = models.BooleanField(blank=True, null=True)
    coord_entrada = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'inspecciones'


class Jerarquia(models.Model):
    jerarquia = models.TextField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'jerarquia'


class LayerStyles(models.Model):
    f_table_catalog = models.CharField(blank=True, null=True)
    f_table_schema = models.CharField(blank=True, null=True)
    f_table_name = models.CharField(blank=True, null=True)
    f_geometry_column = models.CharField(blank=True, null=True)
    stylename = models.TextField(blank=True, null=True)
    styleqml = models.TextField(blank=True, null=True)  # This field type is a guess.
    stylesld = models.TextField(blank=True, null=True)  # This field type is a guess.
    useasdefault = models.BooleanField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    owner = models.CharField(max_length=63, blank=True, null=True)
    ui = models.TextField(blank=True, null=True)  # This field type is a guess.
    update_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'layer_styles'


class LineasDeRiberaF2(models.Model):
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.
    resolucion = models.TextField(blank=True, null=True)
    rio = models.TextField(blank=True, null=True)
    tipo = models.TextField(blank=True, null=True)
    catastro = models.TextField(blank=True, null=True)
    observaciones = models.TextField(blank=True, null=True)
    activo = models.BooleanField(blank=True, null=True)
    etiqueta = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lineas_de_ribera_f2'


class LineasDeRiberaF3(models.Model):
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.
    resolucion = models.TextField(blank=True, null=True)
    rio = models.TextField(blank=True, null=True)
    tipo = models.TextField(blank=True, null=True)
    catastro = models.TextField(blank=True, null=True)
    observaciones = models.TextField(blank=True, null=True)
    activo = models.BooleanField(blank=True, null=True)
    etiqueta = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lineas_de_ribera_f3'


class LineasDeRiberaF4(models.Model):
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.
    resolucion = models.TextField(blank=True, null=True)
    rio = models.TextField(blank=True, null=True)
    tipo = models.TextField(blank=True, null=True)
    catastro = models.TextField(blank=True, null=True)
    observaciones = models.TextField(blank=True, null=True)
    activo = models.BooleanField(blank=True, null=True)
    etiqueta = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lineas_de_ribera_f4'


class LlF2(models.Model):
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.
    expediente = models.IntegerField(blank=True, null=True)
    estado = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'll_f2'


class LlF3(models.Model):
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.
    expediente = models.IntegerField(blank=True, null=True)
    estado = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'll_f3'


class LlF4(models.Model):
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.
    expediente = models.IntegerField(blank=True, null=True)
    estado = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'll_f4'


class MinasF2(models.Model):
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.
    jerarquia = models.TextField(blank=True, null=True)
    expediente = models.IntegerField()
    nombre = models.TextField(blank=True, null=True)
    concesionario = models.TextField(blank=True, null=True)
    yacencia = models.TextField(blank=True, null=True)
    mineral = models.TextField(blank=True, null=True)
    mineral_iia = models.TextField(blank=True, null=True)
    pertenencias = models.SmallIntegerField(blank=True, null=True)
    estado = models.TextField(blank=True, null=True)
    fecha_inicio = models.DateTimeField(blank=True, null=True)
    fecha_registro_oficio = models.DateField(blank=True, null=True)
    fecha_registro_cedula = models.DateField(blank=True, null=True)
    fecha_aprobacion_mensura = models.DateField(blank=True, null=True)
    fecha_resolucion_vacante = models.DateField(blank=True, null=True)
    fecha_publicacion_vacante = models.DateField(blank=True, null=True)
    fecha_concesion_vacante = models.DateField(blank=True, null=True)
    fecha_publicacion_archivo = models.DateField(blank=True, null=True)
    remsa = models.TextField(blank=True, null=True)  # This field type is a guess.
    vacante_prov = models.BooleanField(blank=True, null=True)
    archivo_prov = models.BooleanField(blank=True, null=True)
    departamento = models.TextField(blank=True, null=True)
    municipio = models.TextField(blank=True, null=True)
    lugar = models.TextField(blank=True, null=True)
    nro_orden = models.IntegerField(blank=True, null=True)
    cateo = models.IntegerField(blank=True, null=True)
    descubrimiento_directo = models.BooleanField(blank=True, null=True)
    servidumbres = models.TextField(blank=True, null=True)
    grupo_minero = models.IntegerField(blank=True, null=True)
    observaciones = models.TextField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    create_date = models.DateTimeField()
    informe_ambiente = models.DateField(blank=True, null=True)
    proyecto = models.TextField(blank=True, null=True)
    vacancia_solicitada = models.BooleanField(blank=True, null=True)
    pertenencia_canon = models.BooleanField()
    fecha_reg_decanon = models.BooleanField()
    fecha_reg_aconfirmar = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'minas_f2'


class MinasF3(models.Model):
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.
    jerarquia = models.TextField(blank=True, null=True)
    expediente = models.IntegerField()
    nombre = models.TextField(blank=True, null=True)
    concesionario = models.TextField(blank=True, null=True)
    yacencia = models.TextField(blank=True, null=True)
    mineral = models.TextField(blank=True, null=True)
    mineral_iia = models.TextField(blank=True, null=True)
    pertenencias = models.SmallIntegerField(blank=True, null=True)
    estado = models.TextField(blank=True, null=True)
    fecha_inicio = models.DateTimeField(blank=True, null=True)
    fecha_registro_oficio = models.DateField(blank=True, null=True)
    fecha_registro_cedula = models.DateField(blank=True, null=True)
    fecha_aprobacion_mensura = models.DateField(blank=True, null=True)
    fecha_resolucion_vacante = models.DateField(blank=True, null=True)
    fecha_publicacion_vacante = models.DateField(blank=True, null=True)
    fecha_concesion_vacante = models.DateField(blank=True, null=True)
    fecha_publicacion_archivo = models.DateField(blank=True, null=True)
    remsa = models.TextField(blank=True, null=True)  # This field type is a guess.
    vacante_prov = models.BooleanField(blank=True, null=True)
    archivo_prov = models.BooleanField(blank=True, null=True)
    departamento = models.TextField(blank=True, null=True)
    municipio = models.TextField(blank=True, null=True)
    lugar = models.TextField(blank=True, null=True)
    nro_orden = models.IntegerField(blank=True, null=True)
    cateo = models.IntegerField(blank=True, null=True)
    descubrimiento_directo = models.BooleanField(blank=True, null=True)
    servidumbres = models.TextField(blank=True, null=True)
    grupo_minero = models.IntegerField(blank=True, null=True)
    observaciones = models.TextField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    create_date = models.DateTimeField()
    informe_ambiente = models.DateField(blank=True, null=True)
    proyecto = models.TextField(blank=True, null=True)
    vacancia_solicitada = models.BooleanField(blank=True, null=True)
    pertenencia_canon = models.BooleanField()
    fecha_reg_decanon = models.BooleanField()
    fecha_reg_aconfirmar = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'minas_f3'


class MinasF4(models.Model):
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.
    jerarquia = models.TextField(blank=True, null=True)
    expediente = models.IntegerField()
    nombre = models.TextField(blank=True, null=True)
    concesionario = models.TextField(blank=True, null=True)
    yacencia = models.TextField(blank=True, null=True)
    mineral = models.TextField(blank=True, null=True)
    mineral_iia = models.TextField(blank=True, null=True)
    pertenencias = models.SmallIntegerField(blank=True, null=True)
    estado = models.TextField(blank=True, null=True)
    fecha_inicio = models.DateTimeField(blank=True, null=True)
    fecha_registro_oficio = models.DateField(blank=True, null=True)
    fecha_registro_cedula = models.DateField(blank=True, null=True)
    fecha_aprobacion_mensura = models.DateField(blank=True, null=True)
    fecha_resolucion_vacante = models.DateField(blank=True, null=True)
    fecha_publicacion_vacante = models.DateField(blank=True, null=True)
    fecha_concesion_vacante = models.DateField(blank=True, null=True)
    fecha_publicacion_archivo = models.DateField(blank=True, null=True)
    remsa = models.TextField(blank=True, null=True)  # This field type is a guess.
    vacante_prov = models.BooleanField(blank=True, null=True)
    archivo_prov = models.BooleanField(blank=True, null=True)
    departamento = models.TextField(blank=True, null=True)
    municipio = models.TextField(blank=True, null=True)
    lugar = models.TextField(blank=True, null=True)
    nro_orden = models.IntegerField(blank=True, null=True)
    cateo = models.IntegerField(blank=True, null=True)
    descubrimiento_directo = models.BooleanField(blank=True, null=True)
    servidumbres = models.TextField(blank=True, null=True)
    grupo_minero = models.IntegerField(blank=True, null=True)
    observaciones = models.TextField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    create_date = models.DateTimeField()
    informe_ambiente = models.DateField(blank=True, null=True)
    proyecto = models.TextField(blank=True, null=True)
    vacancia_solicitada = models.BooleanField(blank=True, null=True)
    pertenencia_canon = models.BooleanField()
    fecha_reg_decanon = models.BooleanField()
    fecha_reg_aconfirmar = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'minas_f4'


class Minerales(models.Model):
    mindet = models.TextField(blank=True, null=True)
    mineral = models.TextField(primary_key=True)
    categoria = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'minerales'


class Municipios(models.Model):
    municipio = models.TextField(primary_key=True)
    departamento = models.ForeignKey(Departamentos, models.DO_NOTHING, db_column='departamento', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'municipios'


class ObrasDeArte(models.Model):
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.
    revisionnu = models.FloatField(blank=True, null=True)
    id_estado = models.IntegerField(blank=True, null=True)
    id_tipo_fu = models.IntegerField(blank=True, null=True)
    id_loc = models.IntegerField(blank=True, null=True)
    nombre_fue = models.CharField(max_length=100, blank=True, null=True)
    id_fuente = models.IntegerField(blank=True, null=True)
    featid = models.FloatField(blank=True, null=True)
    fch_alta = models.DateField(blank=True, null=True)
    id_usu_alt = models.CharField(max_length=10, blank=True, null=True)
    observaciones = models.TextField(blank=True, null=True)  # This field type is a guess.
    expediente = models.TextField(blank=True, null=True)
    angulo = models.IntegerField(blank=True, null=True)
    activo = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'obras_de_arte'


class ObrasDeArteL(models.Model):
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.
    expediente = models.TextField(blank=True, null=True)
    tipo_obra = models.TextField(blank=True, null=True)
    concesionario = models.TextField(blank=True, null=True)
    activo = models.BooleanField(blank=True, null=True)
    observaciones = models.TextField(blank=True, null=True)
    ancho_cm = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'obras_de_arte_l'


class PasmaP94F3(models.Model):
    id = models.IntegerField(primary_key=True)
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.
    nombre = models.TextField(blank=True, null=True)
    estado = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pasma_p94_f3'


class PersonalSecretaria(models.Model):
    dni = models.IntegerField(primary_key=True)
    apellido = models.TextField()
    nombre = models.TextField()
    area = models.IntegerField()
    filtro = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'personal_secretaria'


class PertenenciasF2(models.Model):
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.
    expediente = models.IntegerField(blank=True, null=True)
    estado = models.TextField(blank=True, null=True)
    observaciones = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pertenencias_f2'


class PertenenciasF3(models.Model):
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.
    expediente = models.IntegerField(blank=True, null=True)
    estado = models.TextField(blank=True, null=True)
    observaciones = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pertenencias_f3'


class PmdF2(models.Model):
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.
    expediente = models.IntegerField(blank=True, null=True)
    estado = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pmd_f2'


class PmdF3(models.Model):
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.
    expediente = models.IntegerField(blank=True, null=True)
    estado = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pmd_f3'


class PmdF4(models.Model):
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.
    expediente = models.IntegerField(blank=True, null=True)
    estado = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pmd_f4'


class PozosSrh(models.Model):
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.
    srh = models.CharField(max_length=254, blank=True, null=True)
    lat = models.CharField(max_length=254, blank=True, null=True)
    long = models.CharField(max_length=254, blank=True, null=True)
    field_4 = models.CharField(max_length=254, blank=True, null=True)
    año = models.CharField(max_length=254, blank=True, null=True)
    apoderado = models.CharField(max_length=254, blank=True, null=True)
    titular = models.CharField(max_length=254, blank=True, null=True)
    direccion = models.CharField(max_length=254, blank=True, null=True)
    departamen = models.CharField(max_length=254, blank=True, null=True)
    localidad = models.CharField(max_length=254, blank=True, null=True)
    matrÝcula = models.CharField(max_length=254, blank=True, null=True)
    uso = models.CharField(max_length=254, blank=True, null=True)
    motivo = models.CharField(max_length=254, blank=True, null=True)
    tipo_capta = models.CharField(db_column='tipo capta', max_length=254, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    fecha = models.CharField(max_length=254, blank=True, null=True)
    profundida = models.CharField(max_length=254, blank=True, null=True)
    entubado = models.CharField(max_length=254, blank=True, null=True)
    nivel_esta = models.CharField(db_column='nivel esta', max_length=254, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    nivel_dina = models.CharField(db_column='nivel dina', max_length=254, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    depresion = models.CharField(max_length=254, blank=True, null=True)
    caudal_esp = models.CharField(db_column='caudal esp', max_length=254, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    caudal_afo = models.CharField(db_column='caudal afo', max_length=254, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    analisis_f = models.CharField(db_column='analisis f', max_length=254, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    estado_tra = models.CharField(db_column='estado tra', max_length=254, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    estado_t_1 = models.CharField(db_column='estado t_1', max_length=254, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    pedir_en = models.CharField(db_column='pedir en', max_length=254, blank=True, null=True)  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'pozos_srh'


class ProvCanterasF2(models.Model):
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.
    jerarquia = models.TextField(blank=True, null=True)
    concesionario = models.TextField(blank=True, null=True)
    departamento = models.TextField(blank=True, null=True)
    municipio = models.TextField(blank=True, null=True)
    lugar = models.TextField(blank=True, null=True)
    mineral = models.TextField(blank=True, null=True)
    mineral_detallado = models.TextField(blank=True, null=True)
    expediente = models.IntegerField()
    nombre = models.TextField(blank=True, null=True)
    nro_orden = models.IntegerField(blank=True, null=True)
    fecha_inicio = models.DateTimeField(blank=True, null=True)
    fecha_concesion = models.DateField(blank=True, null=True)
    fecha_mensura = models.DateField(blank=True, null=True)
    fecha_archivo = models.DateField(blank=True, null=True)
    estado = models.TextField(blank=True, null=True)
    observaciones = models.TextField(blank=True, null=True)
    privada = models.BooleanField(blank=True, null=True)
    servidumbres = models.TextField(blank=True, null=True)
    seca = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'prov_canteras_f2'


class ProvCanterasF3(models.Model):
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.
    jerarquia = models.TextField(blank=True, null=True)
    concesionario = models.TextField(blank=True, null=True)
    departamento = models.TextField(blank=True, null=True)
    municipio = models.TextField(blank=True, null=True)
    lugar = models.TextField(blank=True, null=True)
    mineral = models.TextField(blank=True, null=True)
    mineral_detallado = models.TextField(blank=True, null=True)
    expediente = models.IntegerField()
    nombre = models.TextField(blank=True, null=True)
    nro_orden = models.IntegerField(blank=True, null=True)
    fecha_inicio = models.DateTimeField(blank=True, null=True)
    fecha_concesion = models.DateField(blank=True, null=True)
    fecha_mensura = models.DateField(blank=True, null=True)
    fecha_archivo = models.DateField(blank=True, null=True)
    estado = models.TextField(blank=True, null=True)
    observaciones = models.TextField(blank=True, null=True)
    privada = models.BooleanField(blank=True, null=True)
    servidumbres = models.TextField(blank=True, null=True)
    seca = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'prov_canteras_f3'


class ProvCanterasF4(models.Model):
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.
    jerarquia = models.TextField(blank=True, null=True)
    concesionario = models.TextField(blank=True, null=True)
    departamento = models.TextField(blank=True, null=True)
    municipio = models.TextField(blank=True, null=True)
    lugar = models.TextField(blank=True, null=True)
    mineral = models.TextField(blank=True, null=True)
    mineral_detallado = models.TextField(blank=True, null=True)
    expediente = models.IntegerField()
    nombre = models.TextField(blank=True, null=True)
    nro_orden = models.IntegerField(blank=True, null=True)
    fecha_inicio = models.DateTimeField(blank=True, null=True)
    fecha_concesion = models.DateField(blank=True, null=True)
    fecha_mensura = models.DateField(blank=True, null=True)
    fecha_archivo = models.DateField(blank=True, null=True)
    estado = models.TextField(blank=True, null=True)
    observaciones = models.TextField(blank=True, null=True)
    privada = models.BooleanField(blank=True, null=True)
    servidumbres = models.TextField(blank=True, null=True)
    seca = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'prov_canteras_f4'


class ProvCateosF2(models.Model):
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.
    jerarquia = models.TextField(blank=True, null=True)
    concesionario = models.TextField(blank=True, null=True)
    departamento = models.TextField(blank=True, null=True)
    municipio = models.TextField(blank=True, null=True)
    lugar = models.TextField(blank=True, null=True)
    categoria = models.TextField(blank=True, null=True)
    expediente = models.IntegerField()
    nro_orden = models.IntegerField(blank=True, null=True)
    fecha_inicio = models.DateTimeField(blank=True, null=True)
    estado = models.TextField(blank=True, null=True)
    coordenadas = models.TextField(blank=True, null=True)
    archivo_prov = models.BooleanField(blank=True, null=True)
    observaciones = models.TextField(blank=True, null=True)
    fecha_publicacion_archivo = models.DateField(blank=True, null=True)
    remsa = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'prov_cateos_f2'


class ProvCateosF3(models.Model):
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.
    jerarquia = models.TextField(blank=True, null=True)
    concesionario = models.TextField(blank=True, null=True)
    departamento = models.TextField(blank=True, null=True)
    municipio = models.TextField(blank=True, null=True)
    lugar = models.TextField(blank=True, null=True)
    categoria = models.TextField(blank=True, null=True)
    expediente = models.IntegerField()
    nro_orden = models.IntegerField(blank=True, null=True)
    fecha_inicio = models.DateTimeField(blank=True, null=True)
    estado = models.TextField(blank=True, null=True)
    coordenadas = models.TextField(blank=True, null=True)
    archivo_prov = models.BooleanField(blank=True, null=True)
    observaciones = models.TextField(blank=True, null=True)
    fecha_publicacion_archivo = models.DateField(blank=True, null=True)
    remsa = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'prov_cateos_f3'


class ProvConveniosF2(models.Model):
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.
    observaciones = models.TextField(blank=True, null=True)
    expediente = models.TextField(blank=True, null=True)
    concesionario = models.TextField(blank=True, null=True)
    departamento = models.TextField(blank=True, null=True)
    municipio = models.TextField(blank=True, null=True)
    lugar = models.TextField(blank=True, null=True)
    mineral = models.TextField(blank=True, null=True)
    resolucion = models.TextField(blank=True, null=True)
    fecha_inicio = models.DateField(blank=True, null=True)
    fecha_caducidad = models.DateField(blank=True, null=True)
    nombre = models.TextField(blank=True, null=True)
    activo = models.BooleanField(blank=True, null=True)
    tipo = models.TextField(blank=True, null=True)
    informe_ambiente = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'prov_convenios_f2'


class ProvConveniosF3(models.Model):
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.
    observaciones = models.TextField(blank=True, null=True)
    expediente = models.TextField(blank=True, null=True)
    concesionario = models.TextField(blank=True, null=True)
    departamento = models.TextField(blank=True, null=True)
    municipio = models.TextField(blank=True, null=True)
    lugar = models.TextField(blank=True, null=True)
    mineral = models.TextField(blank=True, null=True)
    resolucion = models.TextField(blank=True, null=True)
    fecha_inicio = models.DateField(blank=True, null=True)
    fecha_caducidad = models.DateField(blank=True, null=True)
    nombre = models.TextField(blank=True, null=True)
    activo = models.BooleanField(blank=True, null=True)
    tipo = models.TextField(blank=True, null=True)
    informe_ambiente = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'prov_convenios_f3'


class ProvConveniosF4(models.Model):
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.
    observaciones = models.TextField(blank=True, null=True)
    expediente = models.TextField(blank=True, null=True)
    concesionario = models.TextField(blank=True, null=True)
    departamento = models.TextField(blank=True, null=True)
    municipio = models.TextField(blank=True, null=True)
    lugar = models.TextField(blank=True, null=True)
    mineral = models.TextField(blank=True, null=True)
    resolucion = models.TextField(blank=True, null=True)
    fecha_inicio = models.DateField(blank=True, null=True)
    fecha_caducidad = models.DateField(blank=True, null=True)
    nombre = models.TextField(blank=True, null=True)
    activo = models.BooleanField(blank=True, null=True)
    tipo = models.TextField(blank=True, null=True)
    informe_ambiente = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'prov_convenios_f4'


class ProvGruposMinerosF2(models.Model):
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.
    expediente = models.IntegerField(blank=True, null=True)
    concesionario = models.TextField(blank=True, null=True)
    departamento = models.TextField(blank=True, null=True)
    municipio = models.TextField(blank=True, null=True)
    lugar = models.TextField(blank=True, null=True)
    observaciones = models.TextField(blank=True, null=True)
    nombre = models.TextField(blank=True, null=True)
    minas = models.TextField(blank=True, null=True)
    fecha_inicio = models.DateTimeField(blank=True, null=True)
    nro_orden = models.SmallIntegerField(blank=True, null=True)
    estado = models.TextField(blank=True, null=True)
    coordenadas = models.TextField(blank=True, null=True)
    informe_ambiente = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'prov_grupos_mineros_f2'


class ProvGruposMinerosF3(models.Model):
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.
    expediente = models.IntegerField(blank=True, null=True)
    concesionario = models.TextField(blank=True, null=True)
    departamento = models.TextField(blank=True, null=True)
    municipio = models.TextField(blank=True, null=True)
    lugar = models.TextField(blank=True, null=True)
    observaciones = models.TextField(blank=True, null=True)
    nombre = models.TextField(blank=True, null=True)
    minas = models.TextField(blank=True, null=True)
    fecha_inicio = models.DateTimeField(blank=True, null=True)
    nro_orden = models.SmallIntegerField(blank=True, null=True)
    estado = models.TextField(blank=True, null=True)
    coordenadas = models.TextField(blank=True, null=True)
    informe_ambiente = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'prov_grupos_mineros_f3'


class ProvMinasF2(models.Model):
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.
    jerarquia = models.TextField(blank=True, null=True)
    concesionario = models.TextField(blank=True, null=True)
    departamento = models.TextField(blank=True, null=True)
    municipio = models.TextField(blank=True, null=True)
    lugar = models.TextField(blank=True, null=True)
    mineral = models.TextField(blank=True, null=True)
    observaciones = models.TextField(blank=True, null=True)
    yacencia = models.TextField(blank=True, null=True)
    expediente = models.IntegerField()
    nombre = models.TextField(blank=True, null=True)
    nro_orden = models.IntegerField(blank=True, null=True)
    fecha_inicio = models.DateTimeField(blank=True, null=True)
    mineral_detallado = models.TextField(blank=True, null=True)
    descubrimiento_directo = models.BooleanField(blank=True, null=True)
    cateo = models.IntegerField(blank=True, null=True)
    fecha_registro_oficio = models.DateField(blank=True, null=True)
    fecha_registro_cedula = models.DateField(blank=True, null=True)
    fecha_aprobacion_mensura = models.DateField(blank=True, null=True)
    fecha_concesion = models.DateField(blank=True, null=True)
    fecha_publicacion_vacante = models.DateField(blank=True, null=True)
    fecha_publicacion_archivo = models.DateField(blank=True, null=True)
    estado = models.TextField(blank=True, null=True)
    pertenencias = models.SmallIntegerField(blank=True, null=True)
    grupo_minero = models.IntegerField(blank=True, null=True)
    servidumbres = models.TextField(blank=True, null=True)
    archivo_prov = models.BooleanField(blank=True, null=True)
    vacante_prov = models.BooleanField(blank=True, null=True)
    remsa = models.TextField(blank=True, null=True)  # This field type is a guess.
    fecha_resolucion_vacante = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'prov_minas_f2'


class ProvMinasF3(models.Model):
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.
    jerarquia = models.TextField(blank=True, null=True)
    concesionario = models.TextField(blank=True, null=True)
    departamento = models.TextField(blank=True, null=True)
    municipio = models.TextField(blank=True, null=True)
    lugar = models.TextField(blank=True, null=True)
    mineral = models.TextField(blank=True, null=True)
    observaciones = models.TextField(blank=True, null=True)
    yacencia = models.TextField(blank=True, null=True)
    expediente = models.IntegerField()
    nombre = models.TextField(blank=True, null=True)
    nro_orden = models.IntegerField(blank=True, null=True)
    fecha_inicio = models.DateTimeField(blank=True, null=True)
    mineral_detallado = models.TextField(blank=True, null=True)
    descubrimiento_directo = models.BooleanField(blank=True, null=True)
    cateo = models.IntegerField(blank=True, null=True)
    fecha_registro_oficio = models.DateField(blank=True, null=True)
    fecha_registro_cedula = models.DateField(blank=True, null=True)
    fecha_aprobacion_mensura = models.DateField(blank=True, null=True)
    fecha_concesion = models.DateField(blank=True, null=True)
    fecha_resolucion_vacante = models.DateField(blank=True, null=True)
    fecha_publicacion_archivo = models.DateField(blank=True, null=True)
    estado = models.TextField(blank=True, null=True)
    pertenencias = models.SmallIntegerField(blank=True, null=True)
    grupo_minero = models.IntegerField(blank=True, null=True)
    servidumbres = models.TextField(blank=True, null=True)
    archivo_prov = models.BooleanField(blank=True, null=True)
    vacante_prov = models.BooleanField(blank=True, null=True)
    remsa = models.TextField(blank=True, null=True)  # This field type is a guess.
    fecha_publicacion_vacante = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'prov_minas_f3'


class ProvMinasF4(models.Model):
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.
    jerarquia = models.TextField(blank=True, null=True)
    concesionario = models.TextField(blank=True, null=True)
    departamento = models.TextField(blank=True, null=True)
    municipio = models.TextField(blank=True, null=True)
    lugar = models.TextField(blank=True, null=True)
    mineral = models.TextField(blank=True, null=True)
    observaciones = models.TextField(blank=True, null=True)
    yacencia = models.TextField(blank=True, null=True)
    expediente = models.IntegerField()
    nombre = models.TextField(blank=True, null=True)
    fecha_inicio = models.DateTimeField(blank=True, null=True)
    mineral_detallado = models.TextField(blank=True, null=True)
    descubrimiento_directo = models.BooleanField(blank=True, null=True)
    cateo = models.IntegerField(blank=True, null=True)
    estado = models.TextField(blank=True, null=True)
    archivo_prov = models.BooleanField(blank=True, null=True)
    fecha_aprobacion_mensura = models.DateField(blank=True, null=True)
    fecha_concesion = models.DateField(blank=True, null=True)
    fecha_publicacion_archivo = models.DateField(blank=True, null=True)
    fecha_publicacion_vacante = models.DateField(blank=True, null=True)
    fecha_registro_cedula = models.DateField(blank=True, null=True)
    fecha_registro_oficio = models.DateField(blank=True, null=True)
    fecha_resolucion_vacante = models.DateField(blank=True, null=True)
    grupo_minero = models.IntegerField(blank=True, null=True)
    nro_orden = models.IntegerField(blank=True, null=True)
    pertenencias = models.SmallIntegerField(blank=True, null=True)
    remsa = models.TextField(blank=True, null=True)  # This field type is a guess.
    servidumbres = models.TextField(blank=True, null=True)
    vacante_prov = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'prov_minas_f4'


class ProvPertenenciasF2(models.Model):
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.
    expediente = models.IntegerField(blank=True, null=True)
    estado = models.TextField(blank=True, null=True)
    observaciones = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'prov_pertenencias_f2'


class ProvPertenenciasF3(models.Model):
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.
    expediente = models.IntegerField(blank=True, null=True)
    estado = models.TextField(blank=True, null=True)
    observaciones = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'prov_pertenencias_f3'


class ProvServidumbresF2(models.Model):
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.
    tipo_serv = models.TextField(blank=True, null=True)
    expediente = models.IntegerField(blank=True, null=True)
    concesionario = models.TextField(blank=True, null=True)
    departamento = models.TextField(blank=True, null=True)
    municipio = models.TextField(blank=True, null=True)
    lugar = models.TextField(blank=True, null=True)
    pertenece_a = models.TextField(blank=True, null=True)
    observaciones = models.TextField(blank=True, null=True)
    fecha_inicio = models.DateTimeField(blank=True, null=True)
    estado = models.TextField(blank=True, null=True)
    nro_orden = models.SmallIntegerField(blank=True, null=True)
    jerarquia = models.TextField(blank=True, null=True)
    remsa = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'prov_servidumbres_f2'


class ProvServidumbresF3(models.Model):
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.
    tipo_serv = models.TextField(blank=True, null=True)
    expediente = models.IntegerField(blank=True, null=True)
    observaciones = models.TextField(blank=True, null=True)
    pertenece_a = models.TextField(blank=True, null=True)
    departamento = models.TextField(blank=True, null=True)
    municipio = models.TextField(blank=True, null=True)
    lugar = models.TextField(blank=True, null=True)
    concesionario = models.TextField(blank=True, null=True)
    fecha_inicio = models.DateTimeField(blank=True, null=True)
    estado = models.TextField(blank=True, null=True)
    nro_orden = models.SmallIntegerField(blank=True, null=True)
    jerarquia = models.TextField(blank=True, null=True)
    remsa = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'prov_servidumbres_f3'


class ProvServidumbresF4(models.Model):
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.
    tipo_serv = models.TextField(blank=True, null=True)
    expediente = models.IntegerField(blank=True, null=True)
    observaciones = models.TextField(blank=True, null=True)
    pertenece_a = models.TextField(blank=True, null=True)
    departamento = models.TextField(blank=True, null=True)
    municipio = models.TextField(blank=True, null=True)
    lugar = models.TextField(blank=True, null=True)
    concesionario = models.TextField(blank=True, null=True)
    fecha_inicio = models.DateTimeField(blank=True, null=True)
    estado = models.TextField(blank=True, null=True)
    nro_orden = models.SmallIntegerField(blank=True, null=True)
    jerarquia = models.TextField(blank=True, null=True)
    remsa = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'prov_servidumbres_f4'


class ProvServidumbresLF2(models.Model):
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.
    tipo_serv = models.TextField(blank=True, null=True)
    expediente = models.IntegerField(blank=True, null=True)
    observaciones = models.TextField(blank=True, null=True)
    pertenece_a = models.TextField(blank=True, null=True)
    concesionario = models.TextField(blank=True, null=True)
    departamento = models.TextField(blank=True, null=True)
    municipio = models.TextField(blank=True, null=True)
    lugar = models.TextField(blank=True, null=True)
    fecha_inicio = models.DateTimeField(blank=True, null=True)
    estado = models.TextField(blank=True, null=True)
    nro_orden = models.SmallIntegerField(blank=True, null=True)
    jerarquia = models.TextField(blank=True, null=True)
    remsa = models.TextField(blank=True, null=True)  # This field type is a guess.
    ancho_cm = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'prov_servidumbres_l_f2'


class ProvServidumbresLF3(models.Model):
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.
    tipo_serv = models.TextField(blank=True, null=True)
    expediente = models.IntegerField(blank=True, null=True)
    observaciones = models.TextField(blank=True, null=True)
    pertenece_a = models.TextField(blank=True, null=True)
    departamento = models.TextField(blank=True, null=True)
    municipio = models.TextField(blank=True, null=True)
    lugar = models.TextField(blank=True, null=True)
    concesionario = models.TextField(blank=True, null=True)
    fecha_inicio = models.DateTimeField(blank=True, null=True)
    estado = models.TextField(blank=True, null=True)
    nro_orden = models.SmallIntegerField(blank=True, null=True)
    jerarquia = models.TextField(blank=True, null=True)
    remsa = models.TextField(blank=True, null=True)  # This field type is a guess.
    ancho_cm = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'prov_servidumbres_l_f3'


class ProvServidumbresLF4(models.Model):
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.
    tipo_serv = models.TextField(blank=True, null=True)
    expediente = models.IntegerField(blank=True, null=True)
    observaciones = models.TextField(blank=True, null=True)
    concesionario = models.TextField(blank=True, null=True)
    departamento = models.TextField(blank=True, null=True)
    municipio = models.TextField(blank=True, null=True)
    lugar = models.TextField(blank=True, null=True)
    fecha_inicio = models.DateTimeField(blank=True, null=True)
    estado = models.TextField(blank=True, null=True)
    nro_orden = models.SmallIntegerField(blank=True, null=True)
    jerarquia = models.TextField(blank=True, null=True)
    remsa = models.TextField(blank=True, null=True)  # This field type is a guess.
    ancho_cm = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'prov_servidumbres_l_f4'


class ProvServidumbresPF2(models.Model):
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.
    jerarquia = models.TextField(blank=True, null=True)
    expediente = models.IntegerField(blank=True, null=True)
    tipo_serv = models.TextField(blank=True, null=True)
    concesionario = models.TextField(blank=True, null=True)
    pertenece_a = models.TextField(blank=True, null=True)
    fecha_inicio = models.DateTimeField(blank=True, null=True)
    fecha_aprobacion_mensura = models.DateField(blank=True, null=True)
    fecha_publicacion_archivo = models.DateField(blank=True, null=True)
    remsa = models.TextField(blank=True, null=True)  # This field type is a guess.
    departamento = models.TextField(blank=True, null=True)
    municipio = models.TextField(blank=True, null=True)
    lugar = models.TextField(blank=True, null=True)
    nro_orden = models.SmallIntegerField(blank=True, null=True)
    estado = models.TextField(blank=True, null=True)
    observaciones = models.TextField(blank=True, null=True)
    informe_ambiente = models.DateField(blank=True, null=True)
    proyecto = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'prov_servidumbres_p_f2'


class ProvServidumbresPF3(models.Model):
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.
    jerarquia = models.TextField(blank=True, null=True)
    expediente = models.IntegerField(blank=True, null=True)
    tipo_serv = models.TextField(blank=True, null=True)
    concesionario = models.TextField(blank=True, null=True)
    pertenece_a = models.TextField(blank=True, null=True)
    fecha_inicio = models.DateTimeField(blank=True, null=True)
    fecha_aprobacion_mensura = models.DateField(blank=True, null=True)
    fecha_publicacion_archivo = models.DateField(blank=True, null=True)
    remsa = models.TextField(blank=True, null=True)  # This field type is a guess.
    departamento = models.TextField(blank=True, null=True)
    municipio = models.TextField(blank=True, null=True)
    lugar = models.TextField(blank=True, null=True)
    nro_orden = models.SmallIntegerField(blank=True, null=True)
    estado = models.TextField(blank=True, null=True)
    observaciones = models.TextField(blank=True, null=True)
    informe_ambiente = models.DateField(blank=True, null=True)
    proyecto = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'prov_servidumbres_p_f3'


class ProvZonaDeInvestigacionF2(models.Model):
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.
    expediente = models.IntegerField(blank=True, null=True)
    departamento = models.TextField(blank=True, null=True)
    municipio = models.TextField(blank=True, null=True)
    lugar = models.TextField(blank=True, null=True)
    observaciones = models.TextField(blank=True, null=True)
    minas = models.TextField(blank=True, null=True)
    fecha_inicio = models.DateTimeField(blank=True, null=True)
    estado = models.TextField(blank=True, null=True)
    nombre = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'prov_zona_de_investigacion_f2'


class ProvZonaDeInvestigacionF3(models.Model):
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.
    expediente = models.IntegerField(blank=True, null=True)
    departamento = models.TextField(blank=True, null=True)
    municipio = models.TextField(blank=True, null=True)
    lugar = models.TextField(blank=True, null=True)
    observaciones = models.TextField(blank=True, null=True)
    minas = models.TextField(blank=True, null=True)
    fecha_inicio = models.DateTimeField(blank=True, null=True)
    estado = models.TextField(blank=True, null=True)
    nombre = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'prov_zona_de_investigacion_f3'


class ProvZonaDeInvestigacionF4(models.Model):
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.
    expediente = models.IntegerField(blank=True, null=True)
    departamento = models.TextField(blank=True, null=True)
    municipio = models.TextField(blank=True, null=True)
    lugar = models.TextField(blank=True, null=True)
    observaciones = models.TextField(blank=True, null=True)
    minas = models.TextField(blank=True, null=True)
    fecha_inicio = models.DateTimeField(blank=True, null=True)
    estado = models.TextField(blank=True, null=True)
    nombre = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'prov_zona_de_investigacion_f4'


class Proyectos(models.Model):
    proyecto = models.TextField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'proyectos'


class ServidumbresF2(models.Model):
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.
    jerarquia = models.TextField(blank=True, null=True)
    expediente = models.IntegerField(blank=True, null=True)
    tipo_serv = models.TextField(blank=True, null=True)
    concesionario = models.TextField(blank=True, null=True)
    pertenece_a = models.TextField(blank=True, null=True)
    fecha_inicio = models.DateTimeField(blank=True, null=True)
    fecha_aprobacion_mensura = models.DateField(blank=True, null=True)
    fecha_publicacion_archivo = models.DateField(blank=True, null=True)
    remsa = models.TextField(blank=True, null=True)  # This field type is a guess.
    departamento = models.TextField(blank=True, null=True)
    municipio = models.TextField(blank=True, null=True)
    lugar = models.TextField(blank=True, null=True)
    nro_orden = models.SmallIntegerField(blank=True, null=True)
    estado = models.TextField(blank=True, null=True)
    observaciones = models.TextField(blank=True, null=True)
    informe_ambiente = models.DateField(blank=True, null=True)
    proyecto = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'servidumbres_f2'


class ServidumbresF3(models.Model):
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.
    jerarquia = models.TextField(blank=True, null=True)
    expediente = models.IntegerField(blank=True, null=True)
    tipo_serv = models.TextField(blank=True, null=True)
    concesionario = models.TextField(blank=True, null=True)
    pertenece_a = models.TextField(blank=True, null=True)
    fecha_inicio = models.DateTimeField(blank=True, null=True)
    fecha_aprobacion_mensura = models.DateField(blank=True, null=True)
    fecha_publicacion_archivo = models.DateField(blank=True, null=True)
    remsa = models.TextField(blank=True, null=True)  # This field type is a guess.
    departamento = models.TextField(blank=True, null=True)
    municipio = models.TextField(blank=True, null=True)
    lugar = models.TextField(blank=True, null=True)
    nro_orden = models.SmallIntegerField(blank=True, null=True)
    estado = models.TextField(blank=True, null=True)
    observaciones = models.TextField(blank=True, null=True)
    informe_ambiente = models.DateField(blank=True, null=True)
    proyecto = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'servidumbres_f3'


class ServidumbresF4(models.Model):
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.
    jerarquia = models.TextField(blank=True, null=True)
    expediente = models.IntegerField(blank=True, null=True)
    tipo_serv = models.TextField(blank=True, null=True)
    concesionario = models.TextField(blank=True, null=True)
    pertenece_a = models.TextField(blank=True, null=True)
    fecha_inicio = models.DateTimeField(blank=True, null=True)
    fecha_aprobacion_mensura = models.DateField(blank=True, null=True)
    fecha_publicacion_archivo = models.DateField(blank=True, null=True)
    remsa = models.TextField(blank=True, null=True)  # This field type is a guess.
    departamento = models.TextField(blank=True, null=True)
    municipio = models.TextField(blank=True, null=True)
    lugar = models.TextField(blank=True, null=True)
    nro_orden = models.SmallIntegerField(blank=True, null=True)
    estado = models.TextField(blank=True, null=True)
    observaciones = models.TextField(blank=True, null=True)
    informe_ambiente = models.DateField(blank=True, null=True)
    proyecto = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'servidumbres_f4'


class ServidumbresGis(models.Model):
    gid = models.AutoField(primary_key=True)
    expediente = models.CharField(max_length=254)
    nombre = models.CharField(max_length=254, blank=True, null=True)
    titular = models.CharField(max_length=254, blank=True, null=True)
    mineral = models.CharField(max_length=254, blank=True, null=True)
    estado_legal = models.CharField(max_length=254, blank=True, null=True)
    geog = models.TextField(blank=True, null=True)  # This field type is a guess.
    write_date = models.DateTimeField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'servidumbres_gis'


class ServidumbresLF2(models.Model):
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.
    jerarquia = models.TextField(blank=True, null=True)
    expediente = models.IntegerField(blank=True, null=True)
    tipo_serv = models.TextField(blank=True, null=True)
    concesionario = models.TextField(blank=True, null=True)
    pertenece_a = models.TextField(blank=True, null=True)
    fecha_inicio = models.DateTimeField(blank=True, null=True)
    fecha_aprobacion_mensura = models.DateField(blank=True, null=True)
    fecha_publicacion_archivo = models.DateField(blank=True, null=True)
    remsa = models.TextField(blank=True, null=True)  # This field type is a guess.
    departamento = models.TextField(blank=True, null=True)
    municipio = models.TextField(blank=True, null=True)
    lugar = models.TextField(blank=True, null=True)
    nro_orden = models.SmallIntegerField(blank=True, null=True)
    estado = models.TextField(blank=True, null=True)
    observaciones = models.TextField(blank=True, null=True)
    informe_ambiente = models.DateField(blank=True, null=True)
    proyecto = models.TextField(blank=True, null=True)
    ancho_cm = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'servidumbres_l_f2'


class ServidumbresLF3(models.Model):
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.
    jerarquia = models.TextField(blank=True, null=True)
    expediente = models.IntegerField(blank=True, null=True)
    tipo_serv = models.TextField(blank=True, null=True)
    concesionario = models.TextField(blank=True, null=True)
    pertenece_a = models.TextField(blank=True, null=True)
    fecha_inicio = models.DateTimeField(blank=True, null=True)
    fecha_aprobacion_mensura = models.DateField(blank=True, null=True)
    fecha_publicacion_archivo = models.DateField(blank=True, null=True)
    remsa = models.TextField(blank=True, null=True)  # This field type is a guess.
    departamento = models.TextField(blank=True, null=True)
    municipio = models.TextField(blank=True, null=True)
    lugar = models.TextField(blank=True, null=True)
    nro_orden = models.SmallIntegerField(blank=True, null=True)
    estado = models.TextField(blank=True, null=True)
    observaciones = models.TextField(blank=True, null=True)
    informe_ambiente = models.DateField(blank=True, null=True)
    proyecto = models.TextField(blank=True, null=True)
    ancho_cm = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'servidumbres_l_f3'


class ServidumbresLF4(models.Model):
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.
    jerarquia = models.TextField(blank=True, null=True)
    expediente = models.IntegerField(blank=True, null=True)
    tipo_serv = models.TextField(blank=True, null=True)
    concesionario = models.TextField(blank=True, null=True)
    pertenece_a = models.TextField(blank=True, null=True)
    fecha_inicio = models.DateTimeField(blank=True, null=True)
    fecha_aprobacion_mensura = models.DateField(blank=True, null=True)
    fecha_publicacion_archivo = models.DateField(blank=True, null=True)
    remsa = models.TextField(blank=True, null=True)  # This field type is a guess.
    departamento = models.TextField(blank=True, null=True)
    municipio = models.TextField(blank=True, null=True)
    lugar = models.TextField(blank=True, null=True)
    nro_orden = models.SmallIntegerField(blank=True, null=True)
    estado = models.TextField(blank=True, null=True)
    observaciones = models.TextField(blank=True, null=True)
    informe_ambiente = models.DateField(blank=True, null=True)
    proyecto = models.TextField(blank=True, null=True)
    ancho_cm = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'servidumbres_l_f4'


class ServidumbresPF2(models.Model):
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.
    jerarquia = models.TextField(blank=True, null=True)
    expediente = models.IntegerField(blank=True, null=True)
    tipo_serv = models.TextField(blank=True, null=True)
    concesionario = models.TextField(blank=True, null=True)
    pertenece_a = models.TextField(blank=True, null=True)
    fecha_inicio = models.DateTimeField(blank=True, null=True)
    fecha_aprobacion_mensura = models.DateField(blank=True, null=True)
    fecha_publicacion_archivo = models.DateField(blank=True, null=True)
    remsa = models.TextField(blank=True, null=True)  # This field type is a guess.
    departamento = models.TextField(blank=True, null=True)
    municipio = models.TextField(blank=True, null=True)
    lugar = models.TextField(blank=True, null=True)
    nro_orden = models.SmallIntegerField(blank=True, null=True)
    estado = models.TextField(blank=True, null=True)
    observaciones = models.TextField(blank=True, null=True)
    informe_ambiente = models.DateField(blank=True, null=True)
    proyecto = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'servidumbres_p_f2'


class ServidumbresPF3(models.Model):
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.
    jerarquia = models.TextField(blank=True, null=True)
    expediente = models.IntegerField(blank=True, null=True)
    tipo_serv = models.TextField(blank=True, null=True)
    concesionario = models.TextField(blank=True, null=True)
    pertenece_a = models.TextField(blank=True, null=True)
    fecha_inicio = models.DateTimeField(blank=True, null=True)
    fecha_aprobacion_mensura = models.DateField(blank=True, null=True)
    fecha_publicacion_archivo = models.DateField(blank=True, null=True)
    remsa = models.TextField(blank=True, null=True)  # This field type is a guess.
    departamento = models.TextField(blank=True, null=True)
    municipio = models.TextField(blank=True, null=True)
    lugar = models.TextField(blank=True, null=True)
    nro_orden = models.SmallIntegerField(blank=True, null=True)
    estado = models.TextField(blank=True, null=True)
    observaciones = models.TextField(blank=True, null=True)
    informe_ambiente = models.DateField(blank=True, null=True)
    proyecto = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'servidumbres_p_f3'


class SitLegal(models.Model):
    tipo_sit = models.TextField()
    paga = models.BooleanField()
    estado = models.TextField(blank=True, null=True)
    jerarquia = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sit_legal'


class SpatialRefSys(models.Model):
    srid = models.IntegerField(primary_key=True)
    auth_name = models.CharField(max_length=256, blank=True, null=True)
    auth_srid = models.IntegerField(blank=True, null=True)
    srtext = models.CharField(max_length=2048, blank=True, null=True)
    proj4text = models.CharField(max_length=2048, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spatial_ref_sys'


class TipoConvenios(models.Model):
    tipo = models.TextField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'tipo_convenios'


class TipoServidumbres(models.Model):
    jerarquia = models.TextField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'tipo_servidumbres'


class ToponimiaLineas(models.Model):
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.
    nombre = models.TextField(blank=True, null=True)
    tipo = models.TextField(blank=True, null=True)
    altitud = models.IntegerField(blank=True, null=True)
    observaciones = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'toponimia_lineas'


class ToponimiaPoligonos(models.Model):
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.
    nombre = models.TextField(blank=True, null=True)
    tipo = models.TextField(blank=True, null=True)
    altitud = models.IntegerField(blank=True, null=True)
    observaciones = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'toponimia_poligonos'


class ToponimiaPuntos(models.Model):
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.
    nombre = models.TextField(blank=True, null=True)
    tipo = models.TextField(blank=True, null=True)
    altitud = models.IntegerField(blank=True, null=True)
    observaciones = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'toponimia_puntos'


class Yacencia(models.Model):
    yacencia = models.TextField(primary_key=True)
    costo_por_pertenencia = models.TextField(blank=True, null=True)  # This field type is a guess.
    categoria = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'yacencia'


class ZonaDeInvestigacionF2(models.Model):
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.
    expediente = models.IntegerField(blank=True, null=True)
    nombre = models.TextField(blank=True, null=True)
    minas = models.TextField(blank=True, null=True)
    fecha_inicio = models.DateTimeField(blank=True, null=True)
    departamento = models.TextField(blank=True, null=True)
    municipio = models.TextField(blank=True, null=True)
    lugar = models.TextField(blank=True, null=True)
    estado = models.TextField(blank=True, null=True)
    observaciones = models.TextField(blank=True, null=True)
    jerarquia = models.TextField(blank=True, null=True)
    fecha_vencimiento = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zona_de_investigacion_f2'


class ZonaDeInvestigacionF3(models.Model):
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.
    expediente = models.IntegerField(blank=True, null=True)
    nombre = models.TextField(blank=True, null=True)
    minas = models.TextField(blank=True, null=True)
    fecha_inicio = models.DateTimeField(blank=True, null=True)
    departamento = models.TextField(blank=True, null=True)
    municipio = models.TextField(blank=True, null=True)
    lugar = models.TextField(blank=True, null=True)
    estado = models.TextField(blank=True, null=True)
    observaciones = models.TextField(blank=True, null=True)
    jerarquia = models.TextField(blank=True, null=True)
    fecha_vencimiento = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zona_de_investigacion_f3'


class ZonaDeInvestigacionF4(models.Model):
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.
    expediente = models.IntegerField(blank=True, null=True)
    nombre = models.TextField(blank=True, null=True)
    minas = models.TextField(blank=True, null=True)
    fecha_inicio = models.DateTimeField(blank=True, null=True)
    departamento = models.TextField(blank=True, null=True)
    municipio = models.TextField(blank=True, null=True)
    lugar = models.TextField(blank=True, null=True)
    estado = models.TextField(blank=True, null=True)
    observaciones = models.TextField(blank=True, null=True)
    jerarquia = models.TextField(blank=True, null=True)
    fecha_vencimiento = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zona_de_investigacion_f4'





class CanteraCateoMina(models.Model):
    id = models.IntegerField(primary_key=True)
    expediente = models.CharField(max_length=255, null=True, blank=True)
    geom = models.CharField(null=True, blank=True) 
    superficie = models.FloatField(null=True, blank=True)
    jerarquia = models.CharField(max_length=255, null=True, blank=True)
    nombre = models.CharField(max_length=255, null=True, blank=True)
    concesionario = models.CharField(max_length=255, null=True, blank=True)
    mineral = models.CharField(max_length=255, null=True, blank=True)
    mineral_iia = models.CharField(max_length=255, null=True, blank=True)
    estado = models.CharField(max_length=255, null=True, blank=True)
    privada = models.BooleanField(null=True, blank=True)
    fecha_inicio = models.DateField(null=True, blank=True)
    fecha_concesion_oficio = models.DateField(null=True, blank=True)
    fecha_aprobacion_mensura = models.DateField(null=True, blank=True)
    fecha_publicacion_archivo = models.DateField(null=True, blank=True)
    archivo_prov = models.CharField(max_length=255, null=True, blank=True)
    departamento = models.CharField(max_length=255, null=True, blank=True)
    municipio = models.CharField(max_length=255, null=True, blank=True)
    lugar = models.CharField(max_length=255, null=True, blank=True)
    nro_orden = models.CharField(max_length=100, null=True, blank=True)
    servidumbres = models.CharField(max_length=255, null=True, blank=True)
    observaciones = models.TextField(null=True, blank=True)
    informe_ambiente = models.CharField(max_length=255, null=True, blank=True)
    rio = models.CharField(max_length=255, null=True, blank=True)
    categoria = models.CharField(max_length=255, null=True, blank=True)
    remsa = models.CharField(max_length=255, null=True, blank=True)
    yacencia = models.CharField(max_length=255, null=True, blank=True)
    pertenencias = models.IntegerField(null=True, blank=True)
    fecha_concesion = models.DateField(null=True, blank=True)
    fecha_resolucion_vacante = models.DateField(null=True, blank=True)
    fecha_publicacion_vacante = models.DateField(null=True, blank=True)
    fecha_concesion_vacante = models.DateField(null=True, blank=True)
    vacante_prov = models.CharField(max_length=255, null=True, blank=True)
    cateo = models.CharField(max_length=255, null=True, blank=True)
    descubrimiento_directo = models.CharField(max_length=255, null=True, blank=True)
    grupo_minero = models.CharField(max_length=255, null=True, blank=True)
    proyecto = models.CharField(max_length=255, null=True, blank=True)
    tipo = models.CharField(max_length=255, null=True, blank=True)
    faja = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        managed = False  
        db_table = 'canteras_cateos_minas'

class GrupoMinero(models.Model):
    id = models.AutoField(primary_key=True)
    expediente = models.CharField(max_length=100)
    geom = models.CharField(null=True, blank=True)
    superficie = models.FloatField(null=True, blank=True)
    concesionario = models.CharField(max_length=255, null=True, blank=True)
    departamento = models.CharField(max_length=100, null=True, blank=True)
    municipio = models.CharField(max_length=100, null=True, blank=True)
    lugar = models.CharField(max_length=255, null=True, blank=True)
    observaciones = models.TextField(null=True, blank=True)
    nombre = models.CharField(max_length=255, null=True, blank=True)
    minas = models.CharField(max_length=255, null=True, blank=True)
    fecha_inicio = models.DateField(null=True, blank=True)
    nro_orden = models.IntegerField(null=True, blank=True)
    estado = models.CharField(max_length=100, null=True, blank=True)
    coordenadas = models.CharField(max_length=255, null=True, blank=True)
    informe_ambiente = models.TextField(null=True, blank=True)

    class Meta:
        managed = False  
        db_table = 'grupos_mineros'  
        verbose_name = 'Grupo Minero'
        verbose_name_plural = 'Grupos Mineros'

    def __str__(self):
        return f"{self.nombre or 'Sin nombre'} - Expediente {self.expediente}"
    


########################################################################################
class TipoContratos(models.Model):
    id = models.AutoField(primary_key=True)
    contratos_nombre = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipo_contratos'

class Contratos(models.Model):
    id_concesionario = models.CharField(max_length=255)
    paga_canon = models.BooleanField()
    ##explotacion = models.CharField(max_length=255)
    mineral_explotacion = models.CharField(max_length=255)
    ##exploracion = models.CharField(max_length=255)
    ##iia = models.CharField(max_length=255)
    activo = models.BooleanField()
    fecha_ini = models.DateField(blank=True, null=True)
    fecha_fin = models.DateField(blank=True, null=True)
    #pago_regalias = models.BooleanField()
    opcion_compra = models.BooleanField(default=False)
    expediente = models.IntegerField(blank=True, null=True)
    createby = models.TextField()
    createdate = models.DateField()
    updateby = models.TextField(blank=True, null=True)
    updatedate = models.DateField(blank=True, null=True)
    deleteby = models.TextField(blank=True, null=True)
    deletedate = models.DateField(blank=True, null=True)
    observaciones = models.TextField(blank=True, null=True)
    tipo = models.ForeignKey(TipoContratos, on_delete=models.CASCADE,db_column="tipo", related_name='contratos')
    file = models.FileField(upload_to=path_contratos_por_empresa, null=True, blank=True)

    class Meta:
        managed = False
        db_table = 'contratos'

