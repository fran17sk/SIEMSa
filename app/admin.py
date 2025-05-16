from django.contrib import admin
from .models import Exportacion, MinExport, ProdMinero, Pais, Mineral


admin.site.register(Exportacion)
admin.site.register(MinExport)
admin.site.register(ProdMinero)
admin.site.register(Pais)
admin.site.register(Mineral)