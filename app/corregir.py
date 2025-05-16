from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.contrib.auth.decorators import login_required
from .models import *
from django.core.paginator import Paginator
from django.db.models import Prefetch,Sum

for minexp in MinExport.objects.all():
    # Si los valores son muy grandes y quieres dividir por 1000 para corregir:
    minexp.Tn_min_export = minexp.Tn_min_export / 1000
    minexp.save()