from __future__ import unicode_literals

from django.contrib import messages
from django.http import Http404, JsonResponse
from django.shortcuts import redirect
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView
from django.views.generic.base import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from utils.decorators import LoginRequiredMixin, StaffRequiredMixin

from .models import Alimento


class AlimentoListView(LoginRequiredMixin, StaffRequiredMixin, ListView):
    model = Alimento
    template_name = 'alimento/alimento_list.html'

class AlimentoCreateView(LoginRequiredMixin, StaffRequiredMixin, CreateView):
	model = Alimento
	template_name = 'alimento/alimento_form.html'
	fields = ['descricao', 'unidade', 'calorias', 'carboidratos', 'fonte']
	success_url = 'alimento_list'

	def get_success_url(self):
		messages.success(self.request, 'Alimento cadastrado com sucesso!!')
		return reverse(self.success_url)

class AlimentoUpdateView(LoginRequiredMixin, StaffRequiredMixin, UpdateView):
	model = Alimento
	template_name = 'alimento/alimento_form.html'
	fields = ['descricao', 'unidade', 'calorias', 'carboidratos', 'fonte']
	success_url = 'alimento_list'
 
	def get_success_url(self):
		messages.success(self.request, 'Alimento atualizado com sucesso!!')
		return reverse(self.success_url)


class AlimentoDeleteView(LoginRequiredMixin, StaffRequiredMixin, DeleteView):
    model = Alimento
    template_name = 'alimento/alimento_confirm_delete.html'
    success_url = 'alimento_list'
    
    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()		
        success_url = self.get_success_url()
        try:
            self.object.delete()
            messages.success(request, 'Alimento excluído com sucesso!') 
        except Exception as e:
            messages.error(request, 'Há dependências ligadas a esse alimento, permissão negada!')
        return redirect(self.success_url)