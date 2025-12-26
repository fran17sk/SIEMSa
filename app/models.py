from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.db.models import JSONField
from django.utils.timezone import now


class Mineral(models.Model):
    id_min = models.AutoField(primary_key=True,unique=True)
    nom_min = models.CharField(max_length=255,default='')
    coment_min = models.CharField(max_length=255,default='',blank=True,null=True)

    

    def __str__(self):
        return f"Mineral {self.nom_min}"


class ProdMinero(models.Model):
    id_productor_min = models.AutoField(primary_key=True)
    nom_productor_min = models.CharField(max_length=255)

    def __str__(self):
        return self.nom_productor_min

class Pais(models.Model):
    id_pais = models.AutoField(primary_key=True)
    nom_pais = models.CharField(max_length=255)

    def __str__(self):
        return self.nom_pais

class Exportacion(models.Model):
    id_export = models.AutoField(primary_key=True)
    Num_Exped1 = models.CharField(max_length=100)
    Num_Exped2 = models.CharField(max_length=100, blank=True, null=True)
    fecha_export = models.DateField()
    id_productor_min = models.ForeignKey(ProdMinero, on_delete=models.CASCADE, related_name='productor_min')
    id_pais = models.ForeignKey(Pais, on_delete=models.CASCADE, related_name='exportaciones')
    fecha_present_export = models.DateField()
    pedido_comercial_export = models.CharField(max_length=255, blank=True, null=True)
    Estado_anulacion = models.BooleanField(default=False)

    def __str__(self):
        return f"Exportación {self.id_export}"

class MinExport(models.Model):
    id_min_export = models.AutoField(primary_key=True)
    id_export = models.ForeignKey(Exportacion, on_delete=models.CASCADE, related_name='min_exports')
    id_min = models.ForeignKey(Mineral, on_delete=models.CASCADE, related_name='min_exports')
    Tn_min_export = models.DecimalField(max_digits=10, decimal_places=2)
    FOB_min_export = models.DecimalField(max_digits=15, decimal_places=2)

    def __str__(self):
        return f"MinExport {self.id_min_export}"
  




class Expediente(models.Model):
    expedienteid = models.BigAutoField(primary_key=True)
    expedienteanio = models.SmallIntegerField(null=True, blank=True)
    expedientefecha = models.DateField(null=True, blank=True)
    expedientecaratula = models.TextField()
    expedientereconstruido = models.BooleanField()
    expedienteobs = models.TextField()
    expedientenrocargo = models.BigIntegerField()
    tipoid = models.ForeignKey('Tipo', on_delete=models.SET_NULL, null=True, db_column='tipoid')
    expedientenow = models.DateTimeField(null=True, blank=True)
    expedientewrkst = models.CharField(max_length=20, null=True, blank=True)
    expedienteuser = models.CharField(max_length=20, null=True, blank=True)
    expedientenombremina = models.CharField(max_length=50, null=True, blank=True)
    expedientecateg = models.SmallIntegerField(null=True, blank=True)
    expedientedescdirecto = models.BooleanField(null=True, blank=True)
    expedientefojasini = models.SmallIntegerField()
    expedientecateoid = models.BigIntegerField(null=True, blank=True)
    distritoid = models.IntegerField(null=True, blank=True)
    expedienteparaje = models.CharField(max_length=50, null=True, blank=True)
    expedienteseccion = models.CharField(max_length=50, null=True, blank=True)
    expedienteparcela = models.CharField(max_length=50, null=True, blank=True)
    expedientesupsolicitada = models.DecimalField(max_digits=10, decimal_places=4, null=True, blank=True)
    expedientesuplibre = models.DecimalField(max_digits=10, decimal_places=4, null=True, blank=True)
    expedientedlt = models.BooleanField(default=False)
    expedientedltuser = models.CharField(max_length=20)
    expedientedltwrkst = models.CharField(max_length=20)
    expedientedltnow = models.DateTimeField(null=True, blank=True)
    expedientemuestralegal = models.CharField(max_length=2)
    expedientetasaretrib = models.CharField(max_length=2)
    expedienteiia = models.CharField(max_length=2)
    expedienteestampillado = models.CharField(max_length=2)
    expedientecertpoder = models.CharField(max_length=2)
    expedientecanon = models.CharField(max_length=2)
    expedientecanonsupsolic = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank=True)
    expedientepagocanon = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank=True)
    expedientefchapublicvac = models.DateField(null=True, blank=True)
    expedientemes = models.SmallIntegerField(null=True, blank=True)
    departamentoid = models.SmallIntegerField()
    expedienteordennro = models.IntegerField(null=True, blank=True)
    expedienteordentipolibro = models.CharField(max_length=20, null=True, blank=True)
    expedienteordentomo = models.SmallIntegerField(null=True, blank=True)
    expedienteordenfojas = models.SmallIntegerField(null=True, blank=True)
    expedientedomicilio = models.CharField(max_length=100, null=True, blank=True)
    estadoid = models.ForeignKey('EstadoExp', on_delete=models.SET_NULL, null=True, db_column='estadoid')

    def __str__(self):
        return f"{self.expedienteid} - {self.expedientecaratula}"


class Tipo(models.Model):
    tipoid = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=100)
    tipoexpedientesigla = models.CharField(max_length=20)
    tipocolorhexa = models.CharField(max_length=20)
    tipocolorr = models.SmallIntegerField()
    tipocolorg = models.SmallIntegerField()
    tipocolorb = models.SmallIntegerField()
    tipoexpedientevinculados = models.BooleanField()
    tipoexpedientenombre = models.BooleanField()
    tipoexpedientedminero = models.BooleanField()
    tipoexpedienteconcesiones = models.BooleanField()

    def __str__(self):
        return self.tipo.strip()  

class EstadoExp(models.Model):
    estadoid = models.AutoField(primary_key=True)
    estado = models.CharField(max_length=100)
    estadomapa = models.CharField(max_length=20,null=True,blank=True)
    
    def __str__(self):
        return self.estado.strip()  

class Organismo(models.Model):
    organismoid = models.SmallIntegerField(primary_key=True)
    organismonombre = models.CharField(max_length=50)
    areasorden = models.SmallIntegerField()
    organismopadreid = models.SmallIntegerField(null=True, blank=True)


    def __str__(self):
        return self.organismonombre.strip()

class Pase(models.Model):
    expedienteid = models.ForeignKey('Expediente', on_delete=models.SET_NULL, null=True, db_column='expedienteid')
    pasenro = models.SmallIntegerField()
    pasefecha = models.DateTimeField(null=True, blank=True)
    paseobservacion = models.TextField(null=True, blank=True)
    paseorigen = models.SmallIntegerField()
    paseuser = models.CharField(max_length=20, null=True, blank=True)
    pasewrkst = models.CharField(max_length=20, null=True, blank=True)
    pasenow = models.DateTimeField(null=True, blank=True)
    pasedestino = models.SmallIntegerField()
    paserecibido = models.BooleanField()
    pasefecharecibo = models.DateTimeField(null=True, blank=True)
    paseuserrecibo = models.CharField(max_length=20, null=True, blank=True)
    pasewrkstrecibo = models.CharField(max_length=20, null=True, blank=True)
    pasediftiempohs = models.BigIntegerField(null=True, blank=True)
    pasefojasadd = models.SmallIntegerField()
    paseaux1 = models.BigIntegerField()
    pasemotivoid = models.IntegerField(null=True, blank=True)
    paselugarid = models.IntegerField()
    paseusuariodest = models.CharField(max_length=30, null=True, blank=True)
    paseaux2 = models.BigIntegerField(null=True, blank=True)
    paseaux3 = models.BigIntegerField(default=0, null=True, blank=True)
    pasepexpedienteid = models.BigIntegerField(null=True, blank=True)
    paseppasenro = models.SmallIntegerField(null=True, blank=True)


    def __str__(self):
        return f"Pase {self.pasenro} - Expediente {self.expedienteid}"



class Lugar(models.Model):
    lugarid = models.AutoField(primary_key=True)
    lugardesc = models.CharField(max_length=100)

    def __str__(self):
        return self.lugardesc.strip()  # para evitar espacios del tipo CHAR
    
class Motivo(models.Model):
    motivoid = models.AutoField(primary_key=True)
    motivodesc = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.motivodesc.strip()
    
class PerfilUsuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    usuariopass = models.CharField(max_length=128, blank=True, null=True)  # puede ser encriptado o no
    usuariopin = models.CharField(max_length=10, blank=True, null=True)
    usuarioemail = models.EmailField(blank=True, null=True)
    usuarioestado = models.CharField(max_length=20, blank=True, null=True)
    usuarioserialaudit = models.IntegerField(blank=True, null=True)
    perfilid = models.IntegerField(blank=True, null=True)
    usuariocelular = models.CharField(max_length=20, blank=True, null=True)
    usuarionom = models.CharField(max_length=150, blank=True, null=True)
    debe_cambiar_password = models.BooleanField(default=True)

    def __str__(self):
        return self.usuarionom or self.user.username

    
class OrganismoUsuario(models.Model):
    
    organismo = models.ForeignKey(Organismo, on_delete=models.CASCADE,default=None)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE,related_name='organismos_usuario')

    class Meta:
        unique_together = ('organismo', 'usuario')  # Evita duplicados

    def __str__(self):
        return f"{self.usuario.username} - {self.organismo.nombre}"
    
class InspeccionProveedores(models.Model):
    empresa = models.CharField(max_length=255)
    anio = models.IntegerField(blank=True, null=True)
    inspector = models.CharField(max_length=255)
    codigo_inspeccion = models.CharField(max_length=50, unique=True, blank=True, null=True)
    fecha_inspeccion = models.DateField(null=True, blank=True)
    columna_proveedores = models.PositiveIntegerField()
    columna_dni = models.PositiveIntegerField(null=True, blank=True)  # 👈 Te faltaba guardar esta también
    archivo_excel = models.FileField(upload_to='inspecciones_excel/')
    observaciones = models.TextField(blank=True, null=True)
    usuario_registro = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    # Nuevos campos para guardar resultados procesados
    resultados_vigentes = JSONField(blank=True, null=True)
    resultados_vencidos = JSONField(blank=True, null=True)
    resultados_no_encontrados = JSONField(blank=True, null=True)
    total_referencias = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return f"Inspección {self.codigo_inspeccion or self.pk} - {self.empresa}"

class RegistroProveedores(models.Model):
    creado = models.DateTimeField()
    numero_tramite = models.CharField(max_length=255,blank=True, null=True)
    mes = models.CharField(max_length=255,blank=True, null=True)
    anio = models.PositiveIntegerField(blank=True, null=True)
    numero_certificado = models.CharField(max_length=255,blank=True, null=True)
    tipo_registro = models.CharField(max_length=255,blank=True, null=True)
    tramite = models.CharField(max_length=255,blank=True, null=True)
    fecha_alta = models.DateField(blank=True, null=True)
    fecha_vto = models.DateField(blank=True, null=True)
    estado = models.CharField(max_length=255,blank=True, null=True)
    numero_expediente = models.CharField(max_length=255,blank=True, null=True)
    nombre_razon_social = models.CharField(max_length=255,blank=True, null=True)
    cuit_cuil = models.CharField(max_length=255,blank=True, null=True)
    domicilio_real = models.CharField(max_length=255, blank=True, null=True,)
    domicilio_social = models.CharField(max_length=255, blank=True, null=True)
    localidad = models.CharField(max_length=255,blank=True, null=True)
    domicilio_fiscal = models.CharField(max_length=255, blank=True, null=True)
    telefono = models.CharField(max_length=255, blank=True, null=True)
    representante_legal = models.TextField(blank=True, null=True)
    documento_identidad = models.CharField(max_length=255, blank=True, null=True)
    correo_electronico = models.EmailField(blank=True, null=True)
    actividad = models.CharField(max_length=500,blank=True, null=True)
    camara = models.CharField(max_length=255, blank=True, null=True)
    declaracion_jurada = models.BooleanField(default=False,blank=True, null=True)
    persona_asignada = models.CharField(max_length=255, blank=True, null=True)

    # Campos de verificación (checkboxes tipo sí/no)
    nomina_trabajadores = models.BooleanField(default=False,blank=True, null=True)
    fotocopia_dni = models.BooleanField(default=False,blank=True, null=True)
    certificado_residencia = models.BooleanField(default=False,blank=True, null=True)
    inscripcion_afip_dgr = models.BooleanField(default=False,blank=True, null=True)
    regularizacion_fiscal = models.BooleanField(default=False,blank=True, null=True)
    contrato_social = models.BooleanField(default=False,blank=True, null=True)
    acta_designacion_autoridades = models.BooleanField(default=False,blank=True, null=True)
    dni_autoridades = models.BooleanField(default=False,blank=True, null=True)
    certificado_residencia_autoridades = models.BooleanField(default=False,blank=True, null=True)
    dni_representante = models.BooleanField(default=False,blank=True, null=True)
    certificado_residencia_representante = models.BooleanField(default=False,blank=True, null=True)
    poder_otorgado_representante = models.BooleanField(default=False,blank=True, null=True)
    f931_seguridad_social = models.BooleanField(default=False,blank=True, null=True)
    constancia_matriculacion_trabajadores = models.BooleanField(default=False,blank=True, null=True)
    constancia_cuil = models.BooleanField(default=False,blank=True, null=True)

    def __str__(self):
        return f"{self.numero_expediente} - {self.nombre_razon_social}"
    
#######################INDORMATICA#######################################

class InventarioInformatico(models.Model):
    TIPO_EQUIPO_CHOICES = [
        ('Escaner', 'Escaner'),
        ('Impresora', 'Impresora'),
        ('Monitor', 'Monitor'),
        ('Pc', 'Pc'),
        ('Switch', 'Switch'),
        ('Ups', 'Ups'),
        ('Router', 'Router'),
        ('Modem', 'Modem'),
        ('Parlante', 'Parlante'),
        ('Notebook Vieja', 'Notebook Vieja'),
        ('Notebook', 'Notebook'),
        ('Telefono', 'Telefono'),
        ('Telefono Satelital', 'Telefono Satelital'),
        ('GPS', 'GPS'),
        ('Cargador', 'Cargador'),
        ('Switch Telefono', 'Switch Telefono'),
        ('Lectora  Externa', 'Lectora Externa'),
        ('Camara', 'Camara'),
        ('Otros', 'Otros'),
        ('', ''),
    ]

    ESTADO_CHOICES = [
        ('En uso', 'En uso'),
        ('Desuso', 'Desuso'),
        ('Archivado', 'Archivado'),
        ('Defectuoso', 'Defectuoso'),
        ('De baja', 'De baja'),
    ]

    equipo = models.CharField(max_length=50, choices=TIPO_EQUIPO_CHOICES, null=True, blank=True)
    marca = models.CharField(max_length=255, null=True, blank=True)
    modelo = models.CharField(max_length=255, null=True, blank=True)
    numero_inventario = models.CharField(max_length=100, null=True, blank=True)
    numero_serie = models.CharField(max_length=100, null=True, blank=True)
    estado = models.CharField(max_length=50, choices=ESTADO_CHOICES, null=True, blank=True)
    ubicacion = models.CharField(max_length=255, null=True, blank=True)
    observaciones = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.equipo or 'Equipo sin nombre'} - {self.numero_inventario or 'Sin inventario'}"

class InventarioXUsuario(models.Model):
    inventario = models.ForeignKey(InventarioInformatico, on_delete=models.SET_NULL, null=True, blank=True, related_name='asignaciones')
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='inventarios_asignados')
    fecha_asignacion = models.DateField(default=now)
    fecha_desvinculacion = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.inventario} asignado a {self.usuario}"
