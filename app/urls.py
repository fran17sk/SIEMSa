from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login/', views.custom_login, name='login'),
    path('logout/', views.custom_logout, name='logout'),
    path('home/', views.home, name='home'),
    path('paises/', views.paises, name='pais'),
    path('administracion/', views.gestion_usuarios, name='admin_users'),
    path('editar-usuario/', views.editar_usuario, name='editar_usuario'),
    path('usuarios/eliminar/<int:pk>/', views.eliminar_usuario, name='eliminar_usuario'),
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
    path('exportacion/<int:id_export>/editar/', views.edit_exportacion, name='edit_exportacion'),
    #path('exportacion/<int:id_export>/editar/', views.guardar_exportacion, name='edit_export'),
    path("grafico/", views.dashboard, name="vista_graficos"),
    path("grafico/general", views.dashboard, name="vista_graficos_general"),
    path("grafico/toneladas", views.dashboard, name="vista_graficos_toneladas"),
    path("grafico/fob", views.dashboard, name="vista_graficos_fob"),
    path("grafico/varios", views.dashboard, name="vista_graficos_varios"),
    path('api/datos-toneladas/', views.datos_toneladas_exportadas, name='datos_toneladas'),
    path('api/datos-fob/', views.datos_fob_exportadas, name='datos_fob'),
    path('exportar-toneladas/<str:formato>/', views.exportar_toneladas, name='exportar_toneladas'),
    path('exportar-fob/<str:formato>/', views.exportar_fob, name='exportar_fob'),
    path('api/top-productores/', views.top_productores_exportacion, name='exportar_toneladas'),
    path('api/top-productores-fob/', views.top_productores_valor_fob, name='top_productores_valor_fob'),
    path('exportar/top_productores/excel/<int:year>/', views.exportar_excel_top_productores, name='exportar_top_excel'),
    path('exportar/top_productores/pdf/<int:year>/', views.exportar_pdf_top_productores, name='exportar_top_pdf'),
    
    path('mapa-exportaciones/', views.dashboard, name='mapa_exportaciones'),
    path('api/exportaciones/', views.export_data_api, name='api_exportaciones'),
    
    path('exportaciones/reporte/pdf/', views.exportar_pdf, name='exportar_pdf'),
    path('exportaciones/reporte/excel/', views.exportar_excel, name='exportar_excel'),


    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset_form.html'), name='password_reset'),

    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_done'),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'), name='password_reset_confirm'),

    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), name='password_reset_complete'),
    
]