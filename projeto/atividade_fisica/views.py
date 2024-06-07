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

from .models import AtividadeFisica


class AtividadeFisicaListView(LoginRequiredMixin, StaffRequiredMixin, ListView):
    model = AtividadeFisica
    template_name = 'atividade_fisica/atividade_fisica_list.html'

class AtividadeFisicaCreateView(LoginRequiredMixin, StaffRequiredMixin, CreateView):
	model = AtividadeFisica
	template_name = 'atividade_fisica/atividade_fisica_form.html'
	fields = ['nome', 'descricao', 'tipo']
	success_url = 'atividade_fisica_list'

	def get_success_url(self):
		messages.success(self.request, 'Atividade física cadastrada com sucesso!!')
		return reverse(self.success_url)

class AtividadeFisicaUpdateView(LoginRequiredMixin, StaffRequiredMixin, UpdateView):
	model = AtividadeFisica
	template_name = 'atividade_fisica/atividade_fisica_form.html'
	fields = ['nome', 'descricao', 'tipo']
	success_url = 'atividade_fisica_list'
 
	def get_success_url(self):
		messages.success(self.request, 'Atividade física atualizada com sucesso!!')
		return reverse(self.success_url)


class AtividadeFisicaDeleteView(LoginRequiredMixin, StaffRequiredMixin, DeleteView):
    model = AtividadeFisica
    template_name = 'atividade_fisica/atividade_fisica_confirm_delete.html'
    success_url = 'atividade_fisica_list'
    
    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()		
        success_url = self.get_success_url()
        try:
            self.object.delete()
            messages.success(request, 'Atividade física excluída com sucesso!') 
        except Exception as e:
            messages.error(request, 'Há dependências ligadas à essa atividade física, permissão negada!')
        return redirect(self.success_url)