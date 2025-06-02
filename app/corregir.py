
from .models import *


for minexp in MinExport.objects.all():
    # Si los valores son muy grandes y quieres dividir por 1000 para corregir:
    minexp.Tn_min_export = minexp.Tn_min_export / 1000
    minexp.save()