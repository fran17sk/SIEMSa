from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.contrib.auth.decorators import login_required
from .models import *
from django.core.paginator import Paginator
from django.db.models import Prefetch,Sum
from .forms import MineralForm
from django.shortcuts import render, get_object_or_404, redirect
import json

def custom_login(request):
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
    empresas = ProdMinero.objects.all().order_by('nom_productor_min')
    minerales = Mineral.objects.all().order_by('nom_min')
    paises = Pais.objects.all().order_by('nom_pais')

    if request.method == 'POST':
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

        return redirect('exportaciones')  # Cambia por la URL deseada
    ultima_exportacion = Exportacion.objects.order_by('-id_export').first()

    return render(request, 'new_exportacion.html', {
        'empresas': empresas,
        'minerales': minerales,
        'paises': paises,
        'numero_exportacion': ultima_exportacion.id_export + 1,
    })

def edit_exportacion(request, pk):
    exportacion = get_object_or_404(Exportacion, pk=pk)
    detalles = MinExport.objects.filter(id_export=exportacion.id_export)

    if request.method == 'POST':
        # Actualizar los campos principales
        exportacion.Num_Exped1 = request.POST.get('expediente')
        exportacion.fecha_export = request.POST.get('fecha_exportacion')
        exportacion.fecha_present_export = request.POST.get('fecha_presentacion')
        exportacion.pedido_comercial_export = request.POST.get('pedido_comercial')
        exportacion.Estado_anulacion = bool(request.POST.get('anulacion'))
        exportacion.id_productor_min = request.POST.get('empresa')
        exportacion.id_pais = request.POST.get('pais')
        exportacion.save()

        # Reemplazar los detalles
        MinExport.objects.filter(exportacion=exportacion).delete()

        import json
        detalles_data = json.loads(request.POST.get('detalles', '[]'))
        for detalle in detalles_data:
            MinExport.objects.create(
                exportacion=exportacion,
                id_min=detalle['mineral_id'],
                Tn_min_export=detalle['toneladas'],
                FOB_min_export=detalle['valor_fob']
            )

        return redirect('exportaciones_list')  # o la vista que quieras

    context = {
        'exportacion': exportacion,
        'detalles': detalles,
        'empresas': ProdMinero.objects.all(),
        'paises': Pais.objects.all(),
        'minerales': Mineral.objects.all(),
    }
    return render(request, 'new_exportacion.html', context)

@login_required(login_url='/login/')
def exportacion_list(request):
    exportaciones_base = Exportacion.objects.select_related(
        'id_productor_min', 'id_pais'
    ).prefetch_related(
        'min_exports__id_min'
    ).order_by('-fecha_export')

    # Armamos una lista enriquecida
    exportaciones_list = []
    for exp in exportaciones_base:
        minerales = exp.min_exports.all()
        total_tn = sum([m.Tn_min_export for m in minerales])
        total_fob = sum([m.FOB_min_export for m in minerales])

        exportaciones_list.append({
            'exportacion': exp,
            'min_exports': minerales,
            'total_tn': total_tn,
            'total_fob': total_fob,
        })

    paginator = Paginator(exportaciones_list, 50)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'exportaciones.html', {'page_obj': page_obj})








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
        return JsonResponse({'success': True, 'nombre': mineral.nom_min})

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
        return JsonResponse({'success': True, 'nombre': pais.nom_pais})

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
        return JsonResponse({'success': True, 'nombre': productor.nom_pais})

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