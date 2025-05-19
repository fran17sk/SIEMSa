from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.custom_login, name='login'),
    path('logout/', views.custom_logout, name='logout'),
    path('home/', views.home, name='home'),
    path('paises/', views.paises, name='pais'),
    path('registrar-pais/', views.registrar_pais, name='registrar_pais'),
    path("editar-pais/", views.editar_pais, name="editar_pais"),
    path('productores/', views.productores_min, name='productores'),
    path('registrar-productor/', views.registrar_productor, name='registrar_productor'),
    path("editar-productor/", views.editar_productor, name="editar_productor"),
    path('minerales/', views.minerales_list ,name='minerales'),
    path('registrar-mineral/', views.registrar_mineral, name='registrar_mineral'),
    path("editar-mineral/", views.editar_mineral, name="editar_mineral"),
    path('minerales/<int:pk>/delete/', views.mineral_delete, name='mineral_delete'),

    path('exportaciones/', views.exportacion_list, name='exportaciones'),
    path('exportaciones/nueva', views.new_exportacion ,name='exportacion'),
    path('exportacion/<int:pk>/editar/', views.edit_exportacion, name='edit_exportacion'),

]