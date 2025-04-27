from django.urls import path
from Home.views import inicio, crear_zapatos, lista_zapatos, detalles_zapatos, VistaDetallesZapatos, VistaModificarZapatos, VistaEliminarZapatos


urlpatterns = [
    path('', inicio, name='inicio'),
    path('zapatos/', lista_zapatos, name='lista_zapatos'),
    path('zapatos/crear/', crear_zapatos, name='crear_zapatos'),
    #path('zapatos/<int:zapato_id>/',detalles_zapatos, name='detalles_zapatos'),
    path ('zapatos/<int:pk>/', VistaDetallesZapatos.as_view(), name='detalles_zapatos'),
    path('zapatos/<int:pk>/modificar/', VistaModificarZapatos.as_view(), name='modificar_zapatos'),
    path('zapatos/<int:pk>/eliminar/', VistaEliminarZapatos.as_view(), name='eliminar_zapatos')
    
    ]