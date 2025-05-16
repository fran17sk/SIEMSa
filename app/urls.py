from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.custom_login, name='login'),
    path('logout/', views.custom_logout, name='logout'),
    path('home/', views.home, name='home'),
    path('paises/', views.paises, name='pais'),
    path('productores/', views.productores_min, name='productores'),
    path('minerales/', views.minerales_list ,name='minerales'),
    path('registrar-mineral/', views.registrar_mineral, name='registrar_mineral'),
    path('minerales/<int:pk>/delete/', views.mineral_delete, name='mineral_delete'),

    path('exportaciones/', views.exportacion_list, name='exportaciones'),
    path('exportaciones/nueva', views.new_exportacion ,name='exportacion'),
]