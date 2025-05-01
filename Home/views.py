from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .forms import CreacionZapatos
from .models import Zapato

class InicioView(TemplateView):
    template_name = 'Home/inicio.html'

class ListaZapatosView(ListView):
    model = Zapato
    template_name = 'Home/lista_zapatos.html'
    context_object_name = 'zapatos'
    ordering = ['fecha_creacion']

class CrearZapatosView(LoginRequiredMixin, CreateView):
    model = Zapato
    form_class = CreacionZapatos
    template_name = 'Home/crear_zapatos.html'
    success_url = reverse_lazy('lista_zapatos')

    def form_valid(self, form):
        response = super().form_valid(form)
        return redirect(reverse_lazy('lista_zapatos') + '?creado=True')

class DetallesZapatosView(DetailView):
    model = Zapato
    template_name = 'Home/detalles_zapatos.html'
    context_object_name = 'zapato'

class ModificarZapatosView(LoginRequiredMixin, UpdateView):
    model = Zapato
    form_class = CreacionZapatos
    template_name = 'Home/modificar_zapatos.html'
    success_url = reverse_lazy('lista_zapatos')

    def form_valid(self, form):
        # Eliminar imagen anterior si se sube una nueva
        if 'imagen' in self.request.FILES and self.object.imagen:
            self.object.imagen.delete(save=False)
        return super().form_valid(form)

class EliminarZapatosView(LoginRequiredMixin, DeleteView):
    model = Zapato
    template_name = 'Home/eliminar_zapatos.html'
    success_url = reverse_lazy('lista_zapatos')

    def delete(self, request, *args, **kwargs):
        # Eliminar la imagen asociada al zapato
        self.object = self.get_object()
        if self.object.imagen:
            self.object.imagen.delete(save=False)
        return super().delete(request, *args, **kwargs)