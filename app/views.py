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
def new_exportacion(request):
    empresas = ProdMinero.objects.all()
    minerales = Mineral.objects.all()
    paises = Pais.objects.all()
    ultimo_numero = int(Exportacion.objects.last().Num_Exped1) + 1000000 if Exportacion.objects.exists() else 1

    return render(request, 'new_exportacion.html', {
        'empresas': empresas,
        'minerales': minerales,
        'paises': paises,
        'numero_exportacion': ultimo_numero
    })

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