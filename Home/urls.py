from django.urls import path
from Home.views import (InicioView, ListaZapatosView,CrearZapatosView, DetallesZapatosView, ModificarZapatosView, EliminarZapatosView)

urlpatterns = [
    path('', InicioView.as_view(), name='inicio'),
    path('zapatos/', ListaZapatosView.as_view(), name='lista_zapatos'),
    path('zapatos/crear/', CrearZapatosView.as_view(), name='crear_zapatos'),
    path('zapatos/<int:pk>/', DetallesZapatosView.as_view(), name='detalles_zapatos'),
    path('zapatos/<int:pk>/modificar/', ModificarZapatosView.as_view(), name='modificar_zapatos'),
    path('zapatos/<int:pk>/eliminar/', EliminarZapatosView.as_view(), name='eliminar_zapatos')
]