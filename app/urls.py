from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login/', views.custom_login, name='login'),
    path('cambiar-password/', views.CambioPasswordObligatorioView.as_view(), name='cambiar_password'),
    path('logout/', views.custom_logout, name='logout'),
    path('home/', views.home, name='home'),
    path('', views.home, name='home'),
    path('paises/', views.paises, name='pais'),
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
    path("exportaciones/duplicadas/pdf/", views.exportaciones_duplicadas_pdf, name="exportaciones_duplicadas_pdf"),

    path('contratos/', views.contratos_view, name='contratos'),
    path('contratos-list/', views.lista_contratos, name='lista_contratos'),
    path('contratos-list/new', views.crear_contrato, name='create_new'),
    path('verificar-expediente/<str:nro>/', views.verificar_expediente, name='verificar_expediente'),
    path('contratos/serch', views.consultar_contratos_por_expediente, name='serch'),
     path('consulta-expediente/', views.consulta_expediente_view, name='consulta_expediente'),

    path('administration/', views.admin_home, name='administration'),
    path('ajax/check-username/', views.check_username, name='check_username'),
    path('administrations/users/create',views.crear_usuario,name='crear_usuario'),
    path('usuarios/<int:user_id>/data/', views.get_usuario_data, name='usuario_data'),
    path('usuarios/<int:user_id>/activar-deshabilitar/', views.toggle_usuario_activo, name='usuario_toggle_activo'),
    path('usuarios/<int:user_id>/blanquear/', views.blanquear_contraseña, name='usuario_blanquear_password'),
    path('usuarios/<int:user_id>/editar/', views.editar_usuario_view, name='usuario_editar'),

    path("verificar-proveedores/", views.verificar_proveedores, name="verificar_proveedores"),
    path("verificar-proveedores-excel/", views.comparar_proveedores_excel, name="verificar_proveedores_excel"),
    path('proveedores/',views.proveedores_view, name='proveedores'),
    path('proveedores/activos',views.proveedores_activos_view, name='proveedores_activos'),
    path('proveedores_list/',views.proveedores_list, name='proveedores_list'),
    path("proveedor/<int:pk>/", views.detalle_proveedor, name="detalle_proveedor"),
    path('proveedores_edit/<int:pk>', views.editar_proveedor, name='editar_proveedor'),
    path('inspecciones/', views.listado_inspecciones_view, name='listado_inspecciones'),
    path('inspecciones/<int:inspeccion_id>/', views.detalle_inspeccion, name='detalle_inspeccion'),
    path('proveedores/actualizar_proveedores',views.actualizar_proveedores,name='actualizar_proveedores'),
    
    path('users_simsa',views.usuarios_simsa , name='simsa_users'),
    path('reportes/', views.reportes_home, name='reportes_home'),
    path('tableros/', views.tablero_home, name='tablero_home'),
    path("deudas-expedientes/", views.deudas_expedientes, name="deudas_expedientes"),
    path("consulta-deudas-expedientes/", views.consulta_deuda_expediente, name="consulta_deudas_expedientes"),
    path('expediente/deuda/', views.consulta_deuda_datos, name='consulta_deuda_datos'),
    path('expediente/otros/',views.expedientes_concesionario, name='exp_conc'),

    # Usuarios Admin
    path('reportes/usuarios/pdf/', views.usuarios_pdf, name='usuarios_pdf'),
    path('reportes/usuarios/excel/', views.usuarios_excel, name='usuarios_excel'),

    # Empresas sin Usuario
    path('reportes/empresas-sin-usuario/pdf/', views.empresas_sin_usuario_pdf, name='empresas_sin_usuario_pdf'),
    path('reportes/empresas-sin-usuario/excel/', views.empresas_sin_usuario_excel, name='empresas_sin_usuario_excel'),
    
    path("reportes/empresas-sin-proyecto/pdf/", views.reporte_empresas_sin_proyecto_pdf, name="reporte_empresas_sin_proyecto_pdf"),
    path("reportes/empresas-sin-proyecto/excel/", views.reporte_empresas_sin_proyecto_excel, name="reporte_empresas_sin_proyecto_excel"),
    path('reportes/empresas-sin-presentacion-excel/',views.reporte_empresas_sin_presentacion_excel,name='reporte_empresas_sin_presentacion_excel'),
    path('reportes/empresas-sin-presentacion-pdf/',views.reporte_empresas_sin_presentacion_pdf ,name='reporte_empresas_sin_presentacion_pdf'),
    path('api/proyectos_por_concesionario/', views.api_proyectos_por_concesionario, name='api_proyectos_por_concesionario'),
    path('api/periodos_por_proyecto/', views.api_periodos_por_proyecto, name='api_periodos_por_proyecto'),
    path('reportes/generar_proveedores/', views.generar_informe_proveedores, name='generar_informe_proveedores'),


    #######################################################PGYPM##########################################################
    path('pgypm/',views.pgypm,name='pgypm'),
    ###################################################expedientes##########################################################
    path('expedientes/',views.expedientes,name='buscar_expediente'),


    path('sirgen/',views.sirgen_view,name='sirgen'),
    path('sirgen/new',views.nuevo_pase,name='nuevo_pase'),
    path('sirgen/expediente/<int:expediente_id>/', views.detalle_expediente, name='detalle_expediente'),
    path('buscar-expediente', views.buscar_expediente, name='buscar_expediente'),
    path('sirgen/bandeja_entrada', views.bandeja_entrada_view,name='bandeja_entrada'),
    path('recibir-pase/<int:pase_id>/', views.recibir_pase, name='recibir_pase'),
    path('recibir-pases-masivo/', views.recibir_pases_masivo, name='recibir_pases_masivo'),

]