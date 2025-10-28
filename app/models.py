from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.db.models import JSONField
from django.utils.timezone import now

class Contratos(models.Model):
    id_concesionario = models.CharField(max_length=255)
    paga_canon = models.BooleanField(default=False)
    mineral_explotacion = models.CharField(max_length=255)
    activo = models.BooleanField(default=True)
    fecha_ini = models.DateField(blank=True, null=True)
    fecha_fin = models.DateField(blank=True, null=True)
    opcion_compra = models.BooleanField(default=False)
    expediente = models.IntegerField(blank=True, null=True)
    createby = models.CharField(max_length=255)
    createdate = models.DateField(auto_now_add=True)
    updateby = models.CharField(max_length=255, blank=True, null=True)
    updatedate = models.DateField(auto_now=True)
    deleteby = models.CharField(max_length=255, blank=True, null=True)
    deletedate = models.DateField(blank=True, null=True)






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
    