from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponse
from django.http import JsonResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
from django.template.loader import render_to_string
from django.core.paginator import Paginator
from django.test import RequestFactory
from urllib.parse import urlencode
from django.db.models import Sum, Prefetch
from django.db.models.functions import ExtractYear
import geopandas as gpd
from .models import *
from .forms import MineralForm
from django.db.models import Sum, Q, Prefetch
from django.core.paginator import Paginator
from django.shortcuts import render

from datetime import datetime
from collections import defaultdict
import json
import locale
import tempfile
import io

# ReportLab - PDF
from reportlab.lib.pagesizes import letter, landscape, A4, A3
from reportlab.lib.units import inch, cm
from reportlab.platypus import (
    SimpleDocTemplate, Table, TableStyle, Spacer, Image,
    Paragraph
)
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.pdfgen import canvas
import xlsxwriter

# Matplotlib - Gráficos
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas

# OpenPyXL - Excel
import openpyxl
from openpyxl import Workbook
from openpyxl.styles import Font, Alignment
from django.conf import settings
from django.views.decorators.cache import never_cache

from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import User, Group
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test

def group_required(group_names):
    def in_groups(u):
        if u.is_authenticated:
            if u.is_superuser:
                return True  # siempre permitir al superusuario
            if isinstance(group_names, str):
                groups = [group_names]
            else:
                groups = group_names
            return u.groups.filter(name__in=groups).exists()
        return False
    return user_passes_test(in_groups)

def formatear_fob(valor):
    return f"{valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


@never_cache
def custom_login(request):
    if request.user.is_authenticated:
        logout(request)
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return JsonResponse({"success": True, "redirect_url": settings.LOGIN_REDIRECT_URL})
        else:
            return JsonResponse({"success": False, "error": "Usuario o contraseña incorrectos"}, status=401)

    
    
    return render(request, 'login.html')


def custom_logout(request):
    logout(request)
    return redirect('login')

@login_required(login_url='/login/')
def home(request):
    # tu código aquí
    return render(request, 'base.html')

@login_required(login_url='/login/')
def paises(request):
    paises = Pais.objects.all().order_by('nom_pais')  # ordenado alfabéticamente
    return render(request, 'Paises.html', {'paises': paises})


@login_required(login_url='/login/')
def productores_min(request):
    productores = ProdMinero.objects.all().order_by('nom_productor_min')
    return render(request, 'productores.html', {'productores': productores})



@login_required(login_url='/login/')
def minerales_list(request):
    minerales = Mineral.objects.all().order_by('-id_min')
    return render(request, 'minerales.html', {'minerales': minerales})

def mineral_create(request):
    if request.method == "POST":
        form = MineralForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('minerales_list')
    else:
        form = MineralForm()
    return render(request, 'minerales_create_modal.html', {'form': form})

def mineral_delete(request, pk):
    mineral = get_object_or_404(Mineral, pk=pk)
    if request.method == "POST":
        mineral.delete()
        return redirect('minerales_list')
    return render(request, 'minerales_delete_modal.html', {'mineral': mineral})



@login_required(login_url='/login/')
def new_exportacion(request,exportacion_id=None):

    if request.user.groups.filter(name='Lector').exists():
        return JsonResponse({'status': 'error', 'message': 'No tienes permiso para crear exportaciones.'})

    empresas = ProdMinero.objects.all().order_by('nom_productor_min')
    minerales = Mineral.objects.all().order_by('nom_min')
    paises = Pais.objects.all().order_by('nom_pais')

    if request.method == 'POST':
        try:
            data = request.POST
            detalles = json.loads(request.POST.get('detalles'))

            exportacion = Exportacion.objects.create(
                Num_Exped1=data.get('expediente'),
                fecha_export=data.get('fecha_exportacion'),
                id_productor_min_id=int(data.get('empresa')),
                id_pais_id=int(data.get('pais')),
                fecha_present_export=data.get('fecha_presentacion'),
                pedido_comercial_export=data.get('pedido_comercial'),
                Estado_anulacion=bool(data.get('anulacion')),
            )

            for det in detalles:
                MinExport.objects.create(
                    id_export=exportacion,
                    id_min_id=int(det['mineral_id']),
                    Tn_min_export=det['toneladas'],
                    FOB_min_export=det['valor_fob']
                )

            return JsonResponse({
                'status': 'success',
                'id_exportacion': exportacion.id_export
            })

        except Exception as e:
            return JsonResponse({
                'status': 'error',
                'message': str(e)
            })
    ultima_exportacion = Exportacion.objects.order_by('-id_export').first()
    if not ultima_exportacion:
        id_ultima_exportacion = 0 
    else:
        id_ultima_exportacion = ultima_exportacion.id_export

    return render(request, 'new_exportacion.html', {
        'empresas': empresas,
        'minerales': minerales,
        'paises': paises,
        'numero_exportacion': id_ultima_exportacion + 1,
    })

def edit_exportacion(request, id_export):
    exportacion = get_object_or_404(Exportacion, id_export=id_export)
    detalles = MinExport.objects.filter(id_export=exportacion.id_export)

    if request.method == 'POST':
        # Actualizar los campos principales
        data = json.loads(request.body)
        print(data)

        declaracion = data.get('declaracion', {})

        # Guardar datos de la declaración
        exportacion.Num_Exped1 = declaracion.get('expediente')
        exportacion.fecha_export = declaracion.get('fecha_exportacion')
        exportacion.fecha_present_export = declaracion.get('fecha_presentacion')
        empresa = get_object_or_404(ProdMinero,nom_productor_min = declaracion.get('empresa'))
        exportacion.id_productor_min = empresa
        pais = get_object_or_404(Pais,nom_pais=declaracion.get('pais'))
        exportacion.id_pais = pais
        exportacion.pedido_comercial_export = declaracion.get('pedido_comercial')
        print(data['declaracion'].get('anulacion'))
        if data['declaracion'].get('anulacion'):
            exportacion.Estado_anulacion = 1
        else:
            exportacion.Estado_anulacion = 0

        exportacion.save()

        # Agregar nuevos detalles
        nuevos = data.get("nuevos", [])
        for detalle in nuevos:
            mineral_id = detalle.get("mineral_id")
            toneladas = detalle.get("toneladas")
            valor_fob = detalle.get("valor_fob")

            if mineral_id and toneladas and valor_fob:
                mineral = get_object_or_404(Mineral, id_min=mineral_id)
                MinExport.objects.create(
                    id_export=exportacion,
                    id_min=mineral,
                    Tn_min_export=toneladas,
                    FOB_min_export=valor_fob
                )

        

        # Editar detalles existentes
        editados = data.get("editados", [])
        for detalle in editados:
            detalle_id = detalle.get("id")
            toneladas = detalle.get("toneladas")
            valor_fob = detalle.get("valor_fob")

            if detalle_id and toneladas and valor_fob:
                det = get_object_or_404(MinExport, id_min_export=detalle_id, id_export=exportacion)
                det.Tn_min_export = toneladas
                det.FOB_min_export = valor_fob
                det.save()
        # Eliminar detalles por ID
        eliminados = data.get("eliminados", [])
        if eliminados:
            MinExport.objects.filter(id_min_export__in=eliminados, id_export=exportacion).delete()
        return JsonResponse({"message": "Exportación guardada correctamente."}, status=200)

    context = {
        'exportacion': exportacion,
        'detalles': detalles,
        'empresas': ProdMinero.objects.all(),
        'paises': Pais.objects.all(),
        'minerales': Mineral.objects.all(),
    }
    return render(request, 'edit_exportacion.html', context)

@login_required(login_url='/login/')
def exportacion_list(request):
    search = request.GET.get("search", "").strip()

    # Base queryset con anotaciones de totales
    exportaciones_base = Exportacion.objects.select_related(
        'id_productor_min', 'id_pais'
    ).prefetch_related(
        Prefetch(
            'min_exports',
            queryset=MinExport.objects.select_related('id_min')
        )
    ).annotate(
        total_tn=Sum('min_exports__Tn_min_export'),
        total_fob=Sum('min_exports__FOB_min_export')
    ).order_by('-id_export')

    # Filtro por búsqueda (en el queryset)
    if search:
        exportaciones_base = exportaciones_base.filter(
            Q(id_productor_min__nom_productor_min__icontains=search) |
            Q(min_exports__id_min__nom_min__icontains=search)
        ).distinct()

    # Paginación directamente sobre el queryset
    paginator = Paginator(exportaciones_base, 50)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'exportaciones.html', {
        'page_obj': page_obj,
        'search': search,
    })








@csrf_exempt  # Solo si no estás usando el token CSRF en el JS (opcionalmente reemplazable)
def registrar_mineral(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre', '').strip()
        if not nombre:
            return JsonResponse({'success': False, 'error': 'El nombre es requerido.'})
        
        nombre_normalizado = nombre.strip().upper()

        if Mineral.objects.filter(nom_min__iexact=nombre_normalizado).exists():
            return JsonResponse({'success': False, 'error': 'Ya existe un mineral con ese nombre.'})
        
        mineral = Mineral.objects.create(nom_min=nombre_normalizado)
        return JsonResponse({'success': True, 'id_min': mineral.id_min, 'nombre': mineral.nom_min})

    return JsonResponse({'success': False, 'error': 'Método no permitido.'})

@csrf_exempt  # Solo si no estás usando el token CSRF en el JS (opcionalmente reemplazable)
def registrar_pais(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre', '').strip()
        if not nombre:
            return JsonResponse({'success': False, 'error': 'El nombre es requerido.'})
        
        nombre_normalizado = nombre.strip().upper()

        if Pais.objects.filter(nom_pais__iexact=nombre_normalizado).exists():
            return JsonResponse({'success': False, 'error': 'Ya existe un pais con ese nombre.'})
        
        pais = Pais.objects.create(nom_pais=nombre_normalizado)
        return JsonResponse({"success": True, "id": pais.id_pais, "nombre": pais.nom_pais})


    return JsonResponse({'success': False, 'error': 'Método no permitido.'})

@csrf_exempt  # Solo si no estás usando el token CSRF en el JS (opcionalmente reemplazable)
def registrar_productor(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre', '').strip()
        if not nombre:
            return JsonResponse({'success': False, 'error': 'El nombre es requerido.'})
        
        nombre_normalizado = nombre.strip().upper()

        if ProdMinero.objects.filter(nom_productor_min__iexact=nombre_normalizado).exists():
            return JsonResponse({'success': False, 'error': 'Ya existe una Empresa con ese nombre.'})
        
        productor = ProdMinero.objects.create(nom_productor_min=nombre_normalizado)
        return JsonResponse({"success": True,"id": productor.id_productor_min, "nombre": productor.nom_productor_min})

    return JsonResponse({'success': False, 'error': 'Método no permitido.'})





@csrf_exempt
def editar_mineral(request):
    if request.method == "POST":
        data = json.loads(request.body)
        mineral_id = data.get("id")
        nuevo_nombre = data.get("nombre", "").strip().upper()

        if not nuevo_nombre:
            return JsonResponse({"success": False, "error": "El nombre no puede estar vacío."})

        if Mineral.objects.filter(nom_min=nuevo_nombre).exclude(id_min=mineral_id).exists():
            return JsonResponse({"success": False, "error": "Ya existe un mineral con ese nombre."})

        try:
            mineral = Mineral.objects.get(id_min=mineral_id)
            mineral.nom_min = nuevo_nombre
            mineral.save()
            return JsonResponse({"success": True, "nombre": nuevo_nombre})
        except Mineral.DoesNotExist:
            return JsonResponse({"success": False, "error": "El mineral no existe."})
        

@csrf_exempt
def editar_pais(request):
    if request.method == "POST":
        data = json.loads(request.body)
        pais_id = data.get("id")
        nuevo_nombre = data.get("nombre", "").strip().upper()

        if not nuevo_nombre:
            return JsonResponse({"success": False, "error": "El nombre no puede estar vacío."})

        if Pais.objects.filter(nom_pais=nuevo_nombre).exclude(id_pais=pais_id).exists():
            return JsonResponse({"success": False, "error": "Ya existe un Pais con ese nombre."})

        try:
            pais = Pais.objects.get(id_pais=pais_id)
            pais.nom_pais = nuevo_nombre
            pais.save()
            return JsonResponse({"success": True, "nombre": nuevo_nombre})
        except Mineral.DoesNotExist:
            return JsonResponse({"success": False, "error": "El Pais no existe."})
        

@csrf_exempt
def editar_productor(request):
    if request.method == "POST":
        data = json.loads(request.body)
        productor_id = data.get("id")
        nuevo_nombre = data.get("nombre", "").strip().upper()

        if not nuevo_nombre:
            return JsonResponse({"success": False, "error": "El nombre no puede estar vacío."})

        if ProdMinero.objects.filter(nom_productor_min=nuevo_nombre).exclude(id_productor_min=productor_id).exists():
            return JsonResponse({"success": False, "error": "Ya existe una Empresa con ese nombre."})

        try:
            productor = ProdMinero.objects.get(id_productor_min=productor_id)
            productor.nom_productor_min = nuevo_nombre
            productor.save()
            return JsonResponse({"success": True, "nombre": nuevo_nombre})
        except Mineral.DoesNotExist:
            return JsonResponse({"success": False, "error": "La empresa no existe."})
        
@csrf_exempt
def guardar_exportacion(request, id_export):
    try:
        if request.method == 'POST':
            data = json.loads(request.body)

            declaracion = data.get('declaracion', {})

            exportacion = get_object_or_404(Exportacion, id=id_export)

            # Guardar datos de la declaración
            exportacion.Num_Exped1 = declaracion.get('expediente')
            exportacion.fecha_export = declaracion.get('fecha_exportacion')
            exportacion.fecha_present_export = declaracion.get('fecha_presentacion')
            exportacion.id_productor_min = declaracion.get('empresa')
            exportacion.id_pais = declaracion.get('pais')
            exportacion.pedido_comercial_export = declaracion.get('pedido_comercial')
            exportacion.detalles = declaracion.get('detalles', '')
            #exportacion.save()

            # Agregar nuevos detalles
            nuevos = data.get("nuevos", [])
            for detalle in nuevos:
                mineral_id = detalle.get("mineral_id")
                toneladas = detalle.get("toneladas")
                valor_fob = detalle.get("valor_fob")

                if mineral_id and toneladas and valor_fob:
                    mineral = get_object_or_404(Mineral, id=mineral_id)
                    MinExport.objects.create(
                        exportacion=exportacion,
                        mineral=mineral,
                        toneladas=toneladas,
                        valor_fob=valor_fob
                    )

            # Eliminar detalles por ID
            eliminados = data.get("eliminados", [])
            if eliminados:
                MinExport.objects.filter(id__in=eliminados, exportacion=exportacion).delete()

            # Editar detalles existentes
            editados = data.get("editados", [])
            for detalle in editados:
                detalle_id = detalle.get("id")
                toneladas = detalle.get("toneladas")
                valor_fob = detalle.get("valor_fob")

                if detalle_id and toneladas and valor_fob:
                    det = get_object_or_404(MinExport, id=detalle_id, exportacion=exportacion)
                    det.toneladas = toneladas
                    det.valor_fob = valor_fob
                    det.save()

            return JsonResponse({"message": "Exportación guardada correctamente."}, status=200)

        return JsonResponse({"message": "Método no permitido."}, status=405)

    except Exception as e:
        return JsonResponse({"message": f"Error al guardar: {str(e)}"}, status=400)
    





def dashboard_exportaciones(request):
    # Obtener años únicos
    anios = sorted(set(
        Exportacion.objects.dates('fecha_export', 'year')
    ), key=lambda x: x.year)

    # Estructura de datos: { año: { mineral: toneladas } }
    datos = defaultdict(dict)
    minerales_set = set()

    for anio in anios:
        resultados = MinExport.objects.filter(
            id_export__fecha_export__year=anio.year
        ).values(
            'id_min__nom_min'
        ).annotate(
            total=Sum('Tn_min_export')
        )

        for resultado in resultados:
            mineral = resultado['id_min__nom_min']
            toneladas = float(resultado['total'])
            datos[anio.year][mineral] = toneladas
            minerales_set.add(mineral)

    minerales = sorted(minerales_set)
    datos_por_anio = {
        str(anio.year): [datos[anio.year].get(mineral, 0) for mineral in minerales]
        for anio in anios
    }

    context = {
        'minerales': minerales,
        'datos_por_anio': datos_por_anio,
        'anios': [a.year for a in anios],
    }

    return render(request, 'graficos.html', context)


def dashboard(request):
    years = MinExport.objects.annotate(
        year=ExtractYear('id_export__fecha_export')
    ).values_list('year', flat=True).distinct().order_by('-year')
    minerales = Mineral.objects.all()
    context = {
        'years': years,
        'current_year': datetime.now().year,
        'total_empresas' : ProdMinero.objects.count(),
        'total_paises' : Pais.objects.filter(exportaciones__isnull=False).distinct().count(),
        'total_minerales' : Mineral.objects.count(),
        'total_exportaciones' : Exportacion.objects.count(),
        'minerales':minerales
    }
    return render(request, 'dashboard.html',context)


def datos_toneladas_exportadas(request):
    anios = sorted(set(Exportacion.objects.dates('fecha_export', 'year')), key=lambda x: x.year)
    datos = defaultdict(dict)
    minerales_set = set()

    for anio in anios:
        resultados = MinExport.objects.filter(
            id_export__fecha_export__year=anio.year
        ).values(
            'id_min__nom_min'
        ).annotate(
            total=Sum('Tn_min_export')
        )

        for resultado in resultados:
            mineral = resultado['id_min__nom_min']
            toneladas = float(resultado['total'])
            datos[anio.year][mineral] = toneladas
            minerales_set.add(mineral)

    minerales = sorted(minerales_set)

    # Gráfico de líneas: minerales en X, líneas por año
    datos_lineas = {
        str(anio.year): [datos[anio.year].get(mineral, 0) for mineral in minerales]
        for anio in anios
    }

    # Gráfico de barras: años en X, total por mineral
    datos_barras = {}
    for mineral in minerales:
        datos_barras[mineral] = [
            datos[anio.year].get(mineral, 0) for anio in anios
        ]

    # Totales por año
    total_por_anio = [
        sum(datos[anio.year].values()) for anio in anios
    ]

    return JsonResponse({
        'anios': [a.year for a in anios],
        'minerales': minerales,
        'datos_lineas': datos_lineas,
        'datos_barras': datos_barras,
        'totales': total_por_anio,
    })


def datos_fob_exportadas(request):
    anios = sorted(set(Exportacion.objects.dates('fecha_export', 'year')), key=lambda x: x.year)
    datos = defaultdict(dict)
    minerales_set = set()

    for anio in anios:
        resultados = MinExport.objects.filter(
            id_export__fecha_export__year=anio.year
        ).values(
            'id_min__nom_min'
        ).annotate(
            total=Sum('FOB_min_export')
        )

        for resultado in resultados:
            mineral = resultado['id_min__nom_min']
            toneladas = float(resultado['total'])
            datos[anio.year][mineral] = toneladas
            minerales_set.add(mineral)

    minerales = sorted(minerales_set)

    # Gráfico de líneas: minerales en X, líneas por año
    datos_lineas = {
        str(anio.year): [datos[anio.year].get(mineral, 0) for mineral in minerales]
        for anio in anios
    }

    # Gráfico de barras: años en X, total por mineral
    datos_barras = {}
    for mineral in minerales:
        datos_barras[mineral] = [
            datos[anio.year].get(mineral, 0) for anio in anios
        ]

    # Totales por año
    total_por_anio = [
        sum(datos[anio.year].values()) for anio in anios
    ]

    return JsonResponse({
        'anios': [a.year for a in anios],
        'minerales': minerales,
        'datos_lineas': datos_lineas,
        'datos_barras': datos_barras,
        'totales': total_por_anio,
    })


def exportar_toneladas(request, formato):
    # Obtener últimos 5 años
    anios = sorted(set(Exportacion.objects.dates('fecha_export', 'year')), key=lambda x: x.year)[-5:]

    datos = defaultdict(dict)
    minerales_set = set()

    for anio in anios:
        resultados = MinExport.objects.filter(
            id_export__fecha_export__year=anio.year
        ).values(
            'id_min__nom_min'
        ).annotate(
            total=Sum('Tn_min_export')
        )

        for resultado in resultados:
            mineral = resultado['id_min__nom_min']
            toneladas = float(resultado['total'])
            datos[anio.year][mineral] = toneladas
            minerales_set.add(mineral)

    minerales = sorted(minerales_set)

    # Crear tabla: primera fila con años + "Total"
    header = ["Mineral"] + [str(a.year) for a in anios] + ["Total"]
    datos_tabla = [header]

    # Filas: cada mineral con valores por año y total por mineral
    for mineral in minerales:
        fila = [mineral]
        total_min = 0
        for anio in anios:
            val = datos[anio.year].get(mineral, 0)
            fila.append(f"{val:.2f}")
            total_min += val
        fila.append(f"{total_min:.2f}")
        datos_tabla.append(fila)

    if formato == 'pdf':
        buffer = io.BytesIO()
        doc = SimpleDocTemplate(buffer, pagesize=landscape(letter), rightMargin=30,leftMargin=30, topMargin=30,bottomMargin=18)
        elements = []

        styles = getSampleStyleSheet()
        title_style = ParagraphStyle(
            'title',
            parent=styles['Heading1'],
            fontSize=18,
            alignment=TA_CENTER,
            spaceAfter=20,
        )
        title = Paragraph("Reporte de Cantidades Exportadas en toneladas (últimos 5 años)", title_style)
        elements.append(title)

        # Ajustar anchos de columna: mineral más ancho, años y total iguales
        col_widths = [150] + [80]*len(anios) + [80]

        t = Table(datos_tabla, colWidths=col_widths, repeatRows=1)
        t.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#4a90e2")),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (1, 1), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 12),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ]))
        elements.append(t)
        elements.append(Spacer(1, 24))

        # Funciones para gráficos idénticas a antes

        def crear_grafico_lineas():
            fig, ax = plt.subplots(figsize=(12, 5))
            for mineral in minerales:
                y = [datos[anio.year].get(mineral, 0) for anio in anios]
                ax.plot([a.year for a in anios], y, label=mineral, marker='o')
            ax.set_title('Toneladas por Mineral por Año')
            ax.set_xlabel('Año')
            ax.set_ylabel('Toneladas')
            ax.legend(loc='upper left', bbox_to_anchor=(1,1))
            ax.grid(True)
            fig.tight_layout()
            return fig

        def crear_grafico_barras():
            fig, ax = plt.subplots(figsize=(12, 5))
            total_por_anio = [sum(datos[anio.year].values()) for anio in anios]
            ax.bar([a.year for a in anios], total_por_anio, color='skyblue')
            ax.set_title('Toneladas Totales por Año')
            ax.set_xlabel('Año')
            ax.set_ylabel('Toneladas Totales')
            ax.grid(axis='y')
            fig.tight_layout()
            return fig

        for crear_grafico in [crear_grafico_lineas, crear_grafico_barras]:
            fig = crear_grafico()
            img_buffer = io.BytesIO()
            canvas = FigureCanvas(fig)
            canvas.print_png(img_buffer)
            plt.close(fig)
            img_buffer.seek(0)
            img = Image(img_buffer, width=720, height=300)
            elements.append(img)
            elements.append(Spacer(1, 20))

        doc.build(elements)
        pdf = buffer.getvalue()
        buffer.close()

        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="toneladas_exportadas.pdf"'
        response.write(pdf)
        return response
    elif formato == 'excel':
        output = io.BytesIO()
        workbook = xlsxwriter.Workbook(output, {'in_memory': True})
        worksheet = workbook.add_worksheet("Toneladas")

        bold = workbook.add_format({'bold': True, 'bg_color': '#4a90e2', 'color': 'white', 'align': 'center'})
        normal = workbook.add_format({'align': 'center'})

        # Escribir la tabla
        for i, fila in enumerate(datos_tabla):
            for j, celda in enumerate(fila):
                fmt = bold if i == 0 else normal
                worksheet.write(i, j, celda, fmt)

        worksheet.autofilter(0, 0, len(datos_tabla) - 1, len(header) - 1)
        worksheet.freeze_panes(1, 1)

        # Crear gráficos como imágenes
        def crear_grafico_lineas():
            fig, ax = plt.subplots(figsize=(8, 4))
            for mineral in minerales:
                y = [datos[anio.year].get(mineral, 0) for anio in anios]
                ax.plot([a.year for a in anios], y, label=mineral, marker='o')
            ax.set_title('Toneladas por Mineral por Año')
            ax.set_xlabel('Año')
            ax.set_ylabel('Toneladas')
            ax.legend(loc='upper left', bbox_to_anchor=(1,1))
            ax.grid(True)
            fig.tight_layout()
            return fig

        def crear_grafico_barras():
            fig, ax = plt.subplots(figsize=(8, 4))
            total_por_anio = [sum(datos[anio.year].values()) for anio in anios]
            ax.bar([a.year for a in anios], total_por_anio, color='skyblue')
            ax.set_title('Toneladas Totales por Año')
            ax.set_xlabel('Año')
            ax.set_ylabel('Toneladas Totales')
            ax.grid(axis='y')
            fig.tight_layout()
            return fig

        # Agregar hoja con gráficos
        for i, (crear_grafico, nombre_hoja) in enumerate([
            (crear_grafico_lineas, "Gráfico Líneas"),
            (crear_grafico_barras, "Gráfico Barras")
        ]):
            fig = crear_grafico()
            img_buffer = io.BytesIO()
            canvas = FigureCanvas(fig)
            canvas.print_png(img_buffer)
            plt.close(fig)
            img_buffer.seek(0)

            hoja = workbook.add_worksheet(nombre_hoja)
            hoja.insert_image('B2', f'grafico_{i}.png', {'image_data': img_buffer})

        workbook.close()
        output.seek(0)

        response = HttpResponse(output.read(), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename="toneladas_exportadas.xlsx"'
        return response

def exportar_fob(request, formato):
    # Obtener últimos 5 años
    anios = sorted(set(Exportacion.objects.dates('fecha_export', 'year')), key=lambda x: x.year)[-5:]

    datos = defaultdict(dict)
    minerales_set = set()

    for anio in anios:
        resultados = MinExport.objects.filter(
            id_export__fecha_export__year=anio.year
        ).values(
            'id_min__nom_min'
        ).annotate(
            total=Sum('FOB_min_export')
        )

        for resultado in resultados:
            mineral = resultado['id_min__nom_min']
            toneladas = float(resultado['total'])
            datos[anio.year][mineral] = toneladas
            minerales_set.add(mineral)

    minerales = sorted(minerales_set)

    # Crear tabla: primera fila con años + "Total"
    header = ["Mineral"] + [str(a.year) for a in anios] + ["Total"]
    datos_tabla = [header]

    # Filas: cada mineral con valores por año y total por mineral
    for mineral in minerales:
        fila = [mineral]
        total_min = 0
        for anio in anios:
            val = datos[anio.year].get(mineral, 0)
            fila.append(formatear_fob(val))
            total_min += val
        fila.append(formatear_fob(total_min))
        datos_tabla.append(fila)

    if formato == 'pdf':
        buffer = io.BytesIO()
        doc = SimpleDocTemplate(buffer, pagesize=landscape(letter), rightMargin=30,leftMargin=30, topMargin=30,bottomMargin=18)
        elements = []

        styles = getSampleStyleSheet()
        title_style = ParagraphStyle(
            'title',
            parent=styles['Heading1'],
            fontSize=18,
            alignment=TA_CENTER,
            spaceAfter=20,
        )
        title = Paragraph("Reporte de Cantidades Exportadas en Valor FOB USD (últimos 5 años)", title_style)
        elements.append(title)

        # Ajustar anchos de columna: mineral más ancho, años y total iguales
        col_widths = [150] + [80]*len(anios) + [80]

        t = Table(datos_tabla, colWidths=col_widths, repeatRows=1)
        t.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#4a90e2")),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (1, 1), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 12),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ]))
        elements.append(t)
        elements.append(Spacer(1, 24))

        # Funciones para gráficos idénticas a antes

        def crear_grafico_lineas():
            fig, ax = plt.subplots(figsize=(12, 5))
            for mineral in minerales:
                y = [datos[anio.year].get(mineral, 0) for anio in anios]
                ax.plot([a.year for a in anios], y, label=mineral, marker='o')
            ax.set_title('FOB (USD) por Mineral por Año')
            ax.set_xlabel('Año')
            ax.set_ylabel('Valor FOB')
            ax.legend(loc='upper left', bbox_to_anchor=(1,1))
            ax.grid(True)
            fig.tight_layout()
            return fig

        def crear_grafico_barras():
            fig, ax = plt.subplots(figsize=(12, 5))
            total_por_anio = [sum(datos[anio.year].values()) for anio in anios]
            ax.bar([a.year for a in anios], total_por_anio, color='skyblue')
            ax.set_title('Valor FOB Totales por Año')
            ax.set_xlabel('Año')
            ax.set_ylabel('FOB Totales')
            ax.grid(axis='y')
            fig.tight_layout()
            return fig

        for crear_grafico in [crear_grafico_lineas, crear_grafico_barras]:
            fig = crear_grafico()
            img_buffer = io.BytesIO()
            canvas = FigureCanvas(fig)
            canvas.print_png(img_buffer)
            plt.close(fig)
            img_buffer.seek(0)
            img = Image(img_buffer, width=720, height=300)
            elements.append(img)
            elements.append(Spacer(1, 20))

        doc.build(elements)
        pdf = buffer.getvalue()
        buffer.close()

        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="toneladas_exportadas.pdf"'
        response.write(pdf)
        return response
    elif formato == 'excel':
        header = datos_tabla[0]

        output = io.BytesIO()
        workbook = xlsxwriter.Workbook(output, {'in_memory': True})
        worksheet = workbook.add_worksheet("FOB")

        bold = workbook.add_format({'bold': True, 'bg_color': '#4a90e2', 'color': 'white', 'align': 'center'})
        normal = workbook.add_format({'align': 'center'})

        # Escribir la tabla
        for i, fila in enumerate(datos_tabla):
            for j, celda in enumerate(fila):
                fmt = bold if i == 0 else normal
                worksheet.write(i, j, celda, fmt)

        worksheet.autofilter(0, 0, len(datos_tabla) - 1, len(header) - 1)
        worksheet.freeze_panes(1, 1)

        # Crear gráficos como imágenes
        def crear_grafico_lineas():
            fig, ax = plt.subplots(figsize=(8, 4))
            for mineral in minerales:
                y = [datos[anio.year].get(mineral, 0) for anio in anios]
                ax.plot([a.year for a in anios], y, label=mineral, marker='o')
            ax.set_title('FOB por Mineral por Año')
            ax.set_xlabel('Año')
            ax.set_ylabel('FOB (USD)')
            ax.legend(loc='upper left', bbox_to_anchor=(1,1))
            ax.grid(True)
            fig.tight_layout()
            return fig

        def crear_grafico_barras():
            fig, ax = plt.subplots(figsize=(8, 4))
            total_por_anio = [sum(datos[anio.year].values()) for anio in anios]
            ax.bar([a.year for a in anios], total_por_anio, color='skyblue')
            ax.set_title('FOB Total por Año')
            ax.set_xlabel('Año')
            ax.set_ylabel('FOB Total (USD)')
            ax.grid(axis='y')
            fig.tight_layout()
            return fig

        # Agregar hoja con gráficos
        for i, (crear_grafico, nombre_hoja) in enumerate([
            (crear_grafico_lineas, "Gráfico Líneas"),
            (crear_grafico_barras, "Gráfico Barras")
        ]):
            fig = crear_grafico()
            img_buffer = io.BytesIO()
            canvas = FigureCanvas(fig)
            canvas.print_png(img_buffer)
            plt.close(fig)
            img_buffer.seek(0)

            hoja = workbook.add_worksheet(nombre_hoja)
            hoja.insert_image('B2', f'grafico_{i}.png', {'image_data': img_buffer})

        workbook.close()
        output.seek(0)

        response = HttpResponse(
            output.read(),
            content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        )
        response['Content-Disposition'] = 'attachment; filename="fob_exportado.xlsx"'
        return response

def top_productores_exportacion(request):
    year = request.GET.get('year')

    queryset = MinExport.objects.all()
    if year:
        queryset = queryset.filter(id_export__fecha_export__year=year)

    resultados = (
        queryset
        .values('id_export__id_productor_min__nom_productor_min')
        .annotate(total=Sum('Tn_min_export'))
        .order_by('-total')[:5]
    )

    productores = [r['id_export__id_productor_min__nom_productor_min'] for r in resultados]
    valores = [round(r['total'] or 0, 2) for r in resultados]

    return JsonResponse({
        'empresas': productores,
        'valores': valores,
    })

def top_productores_valor_fob(request):
    year = request.GET.get('year')

    queryset = MinExport.objects.all()
    if year:
        queryset = queryset.filter(id_export__fecha_export__year=year)

    resultados = (
        queryset
        .values('id_export__id_productor_min__nom_productor_min')
        .annotate(total_fob=Sum('FOB_min_export'))
        .order_by('-total_fob')[:5]
    )

    empresas = [r['id_export__id_productor_min__nom_productor_min'] for r in resultados]
    valores = [round(r['total_fob'] or 0, 2) for r in resultados]

    return JsonResponse({
        'empresas': empresas,
        'valores': valores,
    })

def exportar_excel_top_productores(request, year):
    year = int(year)
    wb = Workbook()
    ws = wb.active
    ws.title = f'Top Productores {year}'

    # TÍTULO PRINCIPAL
    titulo = f"Reporte Top 5 Productores Mineros - {year}"
    ws.merge_cells('A1:B1')
    cell = ws['A1']
    cell.value = titulo
    cell.font = Font(size=14, bold=True)
    cell.alignment = Alignment(horizontal='center')

    # Espacio debajo del título
    ws.append([])

    # Top por Toneladas
    toneladas_data = (
        MinExport.objects.filter(id_export__fecha_export__year=year)
        .values('id_export__id_productor_min__nom_productor_min')
        .annotate(total=Sum('Tn_min_export'))
        .order_by('-total')[:5]
    )

    ws.append(["Top 5 Productores por Toneladas", "Toneladas Exportadas"])
    for r in toneladas_data:
        ws.append([
            r['id_export__id_productor_min__nom_productor_min'],
            round(r['total'], 2)
        ])
    ws.append([])

    # Top por Valor FOB
    valor_data = (
        MinExport.objects.filter(id_export__fecha_export__year=year)
        .values('id_export__id_productor_min__nom_productor_min')
        .annotate(total=Sum('FOB_min_export'))
        .order_by('-total')[:5]
    )

    ws.append(["Top 5 Productores por Valor FOB (USD)", "Valor Exportado"])
    for r in valor_data:
        ws.append([
            r['id_export__id_productor_min__nom_productor_min'],
            round(r['total'], 2)
        ])

    # Generar respuesta
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    filename = f'top_productores_{year}.xlsx'
    response['Content-Disposition'] = f'attachment; filename={filename}'
    wb.save(response)
    return response


def exportar_pdf_top_productores(request, year):
    year = int(year)
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=A4)
    elements = []
    styles = getSampleStyleSheet()

    elements.append(Paragraph(f"<b>Reporte Top 5 Productores Mineros ({year})</b>", styles['Title']))
    elements.append(Spacer(1, 12))

    # Toneladas
    toneladas_data = (
        MinExport.objects.filter(id_export__fecha_export__year=year)
        .values('id_export__id_productor_min__nom_productor_min')
        .annotate(total=Sum('Tn_min_export'))
        .order_by('-total')[:5]
    )
    elements.append(Paragraph("Top 5 por Toneladas Exportadas (en Tn)", styles['Heading2']))
    tabla_toneladas = [["Empresa", "Toneladas"]]
    total_ton = sum(r['total'] for r in toneladas_data)
    for r in toneladas_data:
        nombre = r['id_export__id_productor_min__nom_productor_min']
        valor = round(r['total'], 2)
        porcentaje = f"{(valor / total_ton) * 100:.2f} %"
        tabla_toneladas.append([nombre, f"{valor} ({porcentaje})"])
    elements.append(Table(tabla_toneladas))
    elements.append(Spacer(1, 20))

    # Valor FOB
    valor_data = (
        MinExport.objects.filter(id_export__fecha_export__year=year)
        .values('id_export__id_productor_min__nom_productor_min')
        .annotate(total=Sum('FOB_min_export'))
        .order_by('-total')[:5]
    )
    elements.append(Paragraph("Top 5 por Valor FOB Exportado (USD)", styles['Heading2']))
    tabla_valor = [["Empresa", "Valor FOB"]]
    total_val = sum(r['total'] for r in valor_data)
    for r in valor_data:
        nombre = r['id_export__id_productor_min__nom_productor_min']
        valor = round(r['total'], 2)
        porcentaje = f"{(valor / total_val) * 100:.2f} %"
        tabla_valor.append([nombre, f"${valor} ({porcentaje})"])
    elements.append(Table(tabla_valor))

    doc.build(elements)
    buffer.seek(0)
    return HttpResponse(buffer, content_type='application/pdf')



def export_data_api(request):
    year = request.GET.get('year')
    mineral_id = request.GET.get('mineral')
    PAISES_MAP = {
            "ARGENTINA": "Argentina",
            "BRASIL": "Brazil",
            "BOLIVIA": "Bolivia",
            "CHILE": "Chile",
            "MALASIA": "Malaysia",
            "REINO UNIDO": "United Kingdom",
            "BANGLADESH": "Bangladesh",
            "ESTADOS UNIDOS": "United States of America",
            "INDIA": "India",
            "AUSTRALIA": "Australia",
            "PAKISTAN": "Pakistan",
            "CHINA": "China",
            "HOLANDA": "Netherlands",
            "POLONIA": "Poland",
            "BELGICA": "Belgium",
            "NUEVA ZELANDA": "New Zealand",
            "SUDAFRICA": "South Africa",
            "FRANCIA": "France",
            "JAPON": "Japan",
            "ITALIA": "Italy",
            "ESPAÑA": "Spain",
            "ALEMANIA": "Germany",
            "INDONESIA": "Indonesia",
            "COSTA RICA": "Costa Rica",
            "CANADA": "Canada",
            "MEXICO": "Mexico",
            "EGIPTO": "Egypt",
            "NICARAGUA": "Nicaragua",
            "URUGUAY": "Uruguay",
            "PARAGUAY": "Paraguay",
            "ARABIA SAUDITA": "Saudi Arabia",
            "COLOMBIA": "Colombia",
            "COREA": "South Korea",
            "KOREA": "South Korea",
            "ECUADOR": "Ecuador",
            "GUATEMALA": "Guatemala",
            "IRAN": "Iran",
            "KENIA": "Kenya",
            "MARRUECOS": "Morocco",
            "PUERTO RICO": "Puerto Rico",
            "TAIWAN": "Taiwan",
            "TAILANDIA": "Thailand",
            "THAILANDIA": "Thailand",
            "VENEZUELA": "Venezuela",
            "PERU": "Peru",
            "PANAMA": "Panama",
            "MONTENEGRO": "Montenegro",
            "TURQUIA": "Turkey",
            "RUSIA": "Russia",
            "MADAGASCAR": "Madagascar",
            "EMIRATOS ARABES UNID": "United Arab Emirates",
            "HONDURAS": "Honduras",
            "REP. DOMINICANA": "Dominican Republic",
            "REPUBLICA DOMINICANA": "Dominican Republic",
            "VIETNAM": "Vietnam",
            "NEPAL": "Nepal",
            "TUNEZ": "Tunisia",
            "PAPUA NUEVA GUINEA": "Papua New Guinea",
            "NIGERIA": "Nigeria",
            "BIRMANIA": "Myanmar",
            "ARGELIA": "Algeria",
            "EL SALVADOR": "El Salvador",
            "SRI LANKA": "Sri Lanka",
            "INGLATERRA": "United Kingdom",
            "IRLANDA DEL SUR": "Ireland",
            "HUNGRIA": "Hungary",
            "SENEGAL": "Senegal",
            "SIRIA": "Syria",
            "HONG KONG": "Hong Kong",
            "DINAMARCA": "Denmark",
            "IRLANDA": "Ireland",
            "SINGAPUR": "Singapore",
            "RUMANIA": "Romania",
            "FILIPINAS": "Philippines",
            "ISRAEL": "Israel"
        }

    qs = MinExport.objects.all()

    if year:
        qs = qs.filter(id_export__fecha_export__year=year)

    if mineral_id:
        qs = qs.filter(id_min=mineral_id)

    data = (
        qs
        .values('id_export__id_pais__nom_pais', 'id_export__id_pais__id_pais')
        .annotate(
            total_toneladas=Sum('Tn_min_export'),
            total_fob=Sum('FOB_min_export')
        )
    )

    response_data = []
    for entry in data:
        nom_pais = entry['id_export__id_pais__nom_pais'].upper()
        nom_normalizado = PAISES_MAP.get(nom_pais, entry['id_export__id_pais__nom_pais'])
        response_data.append({
            'pais': nom_normalizado,
            'id_pais': entry['id_export__id_pais__id_pais'],
            'toneladas': float(entry['total_toneladas']),
            'fob': float(entry['total_fob']),
            'year': year
        })

    return JsonResponse(response_data, safe=False)

def exportar_pdf(request):
    year = request.GET.get("year")
    mineral_nombre = request.GET.get("mineral_nombre", "")

    # Definir años a mostrar
    if year and year.lower() != "todos":
        years = [int(year)]
    else:
        actual_year = datetime.now().year
        years = list(range(actual_year - 4, actual_year + 1))

    # Obtener datos desde la API original
    parsed_data = []
    factory = RequestFactory()

    if not year or year.lower() == "todos":
        for y in years:
            # Clonar GET y asignar el año correcto
            params = request.GET.copy()
            params["year"] = str(y)

            query_string = urlencode(params)
            url = f"{request.path}?{query_string}"


            fake_req = factory.get(url)
            fake_req.user = request.user

            response = export_data_api(fake_req)
            year_data = json.loads(response.content)

            for item in year_data:
                if "year" not in item or not item["year"]:
                    continue
                parsed_data.append(item)
    else:
        response = export_data_api(request)
        parsed_data = json.loads(response.content)
    # Organizar datos
    report_data = {}
    for item in parsed_data:
        if "year" not in item or not item["year"]:
            continue

        anio = int(item["year"])
        
        # Filtro explícito por año consultado (cuando no es "todos")
        if year and year.lower() != "todos" and anio != int(year):
            continue

        pais = item["pais"]
        toneladas = float(item.get("toneladas", 0))
        fob = float(item.get("fob", 0))

        if pais not in report_data:
            report_data[pais] = {}
        report_data[pais][anio] = {'toneladas': toneladas, 'fob': fob}

    buffer = io.BytesIO()
    doc = SimpleDocTemplate(
        buffer,
        pagesize=landscape(A3),
        rightMargin=20,
        leftMargin=20,
        topMargin=20,
        bottomMargin=20,
    )
    elements = []
    styles = getSampleStyleSheet()

    title = "Reporte de exportaciones por países, anuales"
    if year and year.lower() != "todos":
        title += f" - Año {year}"
    if mineral_nombre:
        title += f" - Mineral: {mineral_nombre}"

    elements.append(Paragraph(title, styles["Title"]))
    elements.append(Spacer(1, 12))

    # Construir encabezados
    header = ["País"]
    for y in years:
        header.append(f"Tn {y}")
        header.append(f"FOB {y}")
    header.append("Totales Tn")
    header.append("Totales FOB")

    table_data = [header]

    total_por_columna = {y: {'toneladas': 0, 'fob': 0} for y in years}
    total_general_tn = 0
    total_general_fob = 0

    for pais, anios_data in report_data.items():
        fila = [pais]
        suma_tn_fila = 0
        suma_fob_fila = 0
        for y in years:
            tn = anios_data.get(y, {}).get('toneladas', 0)
            fob = anios_data.get(y, {}).get('fob', 0)
            fila.append(f"{tn:,.2f}")
            fila.append(f"{fob:,.2f}")

            suma_tn_fila += tn
            suma_fob_fila += fob
            total_por_columna[y]['toneladas'] += tn
            total_por_columna[y]['fob'] += fob

        fila.append(f"{suma_tn_fila:,.2f}")
        fila.append(f"{suma_fob_fila:,.2f}")

        total_general_tn += suma_tn_fila
        total_general_fob += suma_fob_fila

        table_data.append(fila)

    # Fila de totales
    fila_totales = ["Totales"]
    for y in years:
        fila_totales.append(f"{total_por_columna[y]['toneladas']:,.2f}")
        fila_totales.append(f"{total_por_columna[y]['fob']:,.2f}")
    fila_totales.append(f"{total_general_tn:,.2f}")
    fila_totales.append(f"{total_general_fob:,.2f}")

    table_data.append(fila_totales)

    col_widths = [120] + [80] * (2 * len(years)) + [90, 90]
    t = Table(table_data, repeatRows=1, colWidths=col_widths)
    style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#d3d3d3")),
        ('BACKGROUND', (0, -1), (-1, -1), colors.HexColor("#e0e0e0")),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTNAME', (0, -1), (-1, -1), 'Helvetica-Bold'),
        ('ALIGN', (1, 1), (-1, -2), 'RIGHT'),
        ('ALIGN', (1, -1), (-1, -1), 'RIGHT'),
        ('ALIGN', (0, 0), (0, -1), 'LEFT'),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
    ])
    t.setStyle(style)
    elements.append(t)

    doc.build(elements)
    buffer.seek(0)
    return HttpResponse(
        buffer,
        content_type='application/pdf',
        headers={'Content-Disposition': 'attachment; filename="reporte_exportaciones.pdf"'}
    )


def exportar_excel(request):
    year = request.GET.get("anio")
    mineral_id = request.GET.get("mineral")
    mineral_nombre = request.GET.get("mineral_nombre", "")

    qs = MinExport.objects.all()
    if mineral_id:
        qs = qs.filter(id_min=mineral_id)

    if not year or year.lower() == "todos":
        current_year = datetime.now().year
        years = list(range(current_year - 4, current_year + 1))
        qs = qs.filter(id_export__fecha_export__year__in=years)
    else:
        years = [int(year)]
        qs = qs.filter(id_export__fecha_export__year=year)

    data = (
        qs
        .values('id_export__id_pais__nom_pais', 'id_export__fecha_export__year')
        .annotate(
            total_toneladas=Sum('Tn_min_export'),
            total_fob=Sum('FOB_min_export')
        )
        .order_by('id_export__id_pais__nom_pais', 'id_export__fecha_export__year')
    )

    PAISES_MAP = {
        # ... tu diccionario de países ...
    }

    report_data = {}
    for entry in data:
        pais_raw = entry['id_export__id_pais__nom_pais'].upper()
        pais = PAISES_MAP.get(pais_raw, entry['id_export__id_pais__nom_pais'])
        anio = entry['id_export__fecha_export__year']
        tonel = entry['total_toneladas'] or 0
        fob = entry['total_fob'] or 0

        if pais not in report_data:
            report_data[pais] = {}
        report_data[pais][anio] = {
            'toneladas': tonel,
            'fob': fob
        }

    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Exportaciones"

    titulo = "Reporte de exportaciones por países, anuales"
    if year and year.lower() != "todos":
        titulo += f" - Año {year}"
    if mineral_nombre:
        titulo += f" - Mineral: {mineral_nombre}"

    ws.merge_cells(start_row=1, start_column=1, end_row=1, end_column=1 + len(years)*2 + 1)
    ws.cell(row=1, column=1).value = titulo
    ws.cell(row=1, column=1).font = Font(bold=True, size=14)
    ws.cell(row=1, column=1).alignment = Alignment(horizontal="center")

    # Encabezados
    ws.cell(row=2, column=1).value = "País"
    ws.cell(row=2, column=1).font = Font(bold=True)
    ws.merge_cells(start_row=2, start_column=1, end_row=3, end_column=1)

    col = 2
    for y in years:
        ws.merge_cells(start_row=2, start_column=col, end_row=2, end_column=col+1)
        ws.cell(row=2, column=col).value = f"Año {y}"
        ws.cell(row=2, column=col).font = Font(bold=True)
        ws.cell(row=2, column=col).alignment = Alignment(horizontal="center")

        ws.cell(row=3, column=col).value = "Tn"
        ws.cell(row=3, column=col).font = Font(bold=True)
        ws.cell(row=3, column=col+1).value = "FOB (USD)"
        ws.cell(row=3, column=col+1).font = Font(bold=True)

        col += 2

    # Columna extra para totales por fila
    ws.merge_cells(start_row=2, start_column=col, end_row=3, end_column=col)
    ws.cell(row=2, column=col).value = "Totales"
    ws.cell(row=2, column=col).font = Font(bold=True)
    ws.cell(row=2, column=col).alignment = Alignment(horizontal="center")

    # Datos y totales por fila
    fila = 4
    total_por_columna = {y: {'toneladas': 0, 'fob': 0} for y in years}
    total_general_toneladas = 0
    total_general_fob = 0

    for pais, anios_data in report_data.items():
        ws.cell(row=fila, column=1).value = pais
        suma_tn_fila = 0
        suma_fob_fila = 0
        col = 2
        for y in years:
            toneladas = anios_data.get(y, {}).get('toneladas', 0)
            fob = anios_data.get(y, {}).get('fob', 0)

            ws.cell(row=fila, column=col).value = round(toneladas, 2)
            ws.cell(row=fila, column=col+1).value = round(fob, 2)

            suma_tn_fila += toneladas
            suma_fob_fila += fob

            total_por_columna[y]['toneladas'] += toneladas
            total_por_columna[y]['fob'] += fob

            col += 2

        # Total fila: mostrar suma tn + fob juntos (puede separar si querés)
        ws.cell(row=fila, column=col).value = f"Tn: {round(suma_tn_fila, 2)}\nFOB: {round(suma_fob_fila, 2)}"
        ws.cell(row=fila, column=col).alignment = Alignment(wrap_text=True)

        total_general_toneladas += suma_tn_fila
        total_general_fob += suma_fob_fila

        fila += 1

    # Fila total final para columnas
    ws.cell(row=fila, column=1).value = "Totales"
    ws.cell(row=fila, column=1).font = Font(bold=True)

    col = 2
    for y in years:
        tn_col = total_por_columna[y]['toneladas']
        fob_col = total_por_columna[y]['fob']

        ws.cell(row=fila, column=col).value = round(tn_col, 2)
        ws.cell(row=fila, column=col).font = Font(bold=True)
        ws.cell(row=fila, column=col+1).value = round(fob_col, 2)
        ws.cell(row=fila, column=col+1).font = Font(bold=True)

        col += 2

    # Total general en la última columna
    ws.cell(row=fila, column=col).value = f"Tn: {round(total_general_toneladas, 2)}\nFOB: {round(total_general_fob, 2)}"
    ws.cell(row=fila, column=col).font = Font(bold=True)
    ws.cell(row=fila, column=col).alignment = Alignment(wrap_text=True)

    # Ajustar ancho columnas
    ws.column_dimensions['A'].width = 25
    for i in range(2, 2 + len(years)*2 + 1):
        col_letter = openpyxl.utils.get_column_letter(i)
        ws.column_dimensions[col_letter].width = 18

    output = io.BytesIO()
    wb.save(output)
    output.seek(0)

    return HttpResponse(output, content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet", headers={
        'Content-Disposition': 'attachment; filename="reporte_exportaciones.xlsx"',
    })
























def gestion_usuarios(request):
    usuarios = User.objects.all()
    grupos = Group.objects.all()
    mensaje = ''
    tipo_mensaje = ''

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        grupo_nombre = request.POST.get('grupo')

        if username and email and password and grupo_nombre:
            if User.objects.filter(username=username).exists():
                mensaje = 'El nombre de usuario ya existe.'
                tipo_mensaje = 'error'
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                grupo = Group.objects.get(name=grupo_nombre)
                user.groups.add(grupo)
                mensaje = 'Usuario creado exitosamente.'
                tipo_mensaje = 'success'
        else:
            mensaje = 'Complete todos los campos.'
            tipo_mensaje = 'error'

    return render(request, 'admin.html', {
        'usuarios': usuarios,
        'grupos': grupos,
        'mensaje': mensaje,
        'tipo_mensaje': tipo_mensaje
    })

@csrf_exempt
def editar_usuario(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        username = request.POST.get('username')
        email = request.POST.get('email')
        grupo_nombre = request.POST.get('grupo')

        user = get_object_or_404(User, id=user_id)
        user.username = username
        user.email = email
        user.save()

        if grupo_nombre:
            grupo = Group.objects.get(name=grupo_nombre)
            user.groups.clear()
            user.groups.add(grupo)
        
        return redirect('admin_users')
    
@login_required
def eliminar_usuario(request, pk):
    if request.method == 'POST':
        # Verificamos que el usuario tenga permisos adecuados
        if not request.user.is_superuser:
            return HttpResponseForbidden("No tienes permiso para eliminar usuarios.")

        usuario = get_object_or_404(User, pk=pk)

        # Evitar que el usuario se elimine a sí mismo
        if request.user == usuario:
            return JsonResponse({'error': 'No puedes eliminar tu propio usuario.'}, status=400)

        usuario.delete()
        return JsonResponse({'mensaje': 'Usuario eliminado correctamente.'})

    return HttpResponseBadRequest('Método no permitido.')