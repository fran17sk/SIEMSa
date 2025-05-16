from django.db import models

class Mineral(models.Model):
    id_min = models.AutoField(primary_key=True,unique=True)
    nom_min = models.CharField(max_length=255,default='')

    

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
    id_productor_min = models.ForeignKey(ProdMinero, on_delete=models.CASCADE, related_name='exportaciones')
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