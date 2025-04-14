from django.urls import path
from Home.views import inicio, crear_zapatos, lista_zapatos


urlpatterns = [
    path('', inicio, name='inicio'),
    path('zapatos/', lista_zapatos, name='lista_zapatos'),
    path('zapatos/crear/', crear_zapatos, name='crear_zapatos'),
]