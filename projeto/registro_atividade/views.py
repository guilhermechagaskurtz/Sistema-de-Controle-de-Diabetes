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

from .models import RegistroAtividade
from .forms import BuscaAtividadeForm
from .forms import ClienteForm


class RegistroAtividadeListView(LoginRequiredMixin, StaffRequiredMixin, ListView):
    model = RegistroAtividade
    template_name = 'registro_atividade/registro_atividade_list.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.GET:
            #quando ja tem dado filtrando
            context['form'] = BuscaAtividadeForm(data=self.request.GET)
        else:
            #quando acessa sem dado filtrando
            context['form'] = BuscaAtividadeForm()
        return context

    def get_queryset(self):
        qs = RegistroAtividade.objects.all()

        if self.request.GET:
            #quando ja tem dado filtrando
            form = BuscaAtividadeForm(data=self.request.GET)
        else:
            #quando acessa sem dado filtrando
            form = BuscaAtividadeForm()

        if form.is_valid():
            cliente = form.cleaned_data.get('cliente')
            atividade = form.cleaned_data.get('atividade')
            data = form.cleaned_data.get('data')

            if cliente:
                qs = qs.filter(cliente__nome__icontains=cliente)
            
            if atividade:
                qs = qs.filter(atividade__nome__icontains=atividade)

            if data:
                qs = qs.filter(data__icontains=data)
        return qs

class RegistroAtividadeCreateView(LoginRequiredMixin, StaffRequiredMixin, CreateView):
    model = RegistroAtividade
    template_name = 'registro_atividade/registro_atividade_form.html'
    form_class = ClienteForm
    success_url = 'registro_atividade_list'
    
    def form_valid(self, form):
        atividade = form.save(commit=False)
        atividade.total_calorias = 0 
        
        try:
            atividade.save()
            return super().form_valid(form)
        except Exception as e:
            messages.error(self.request, 'Problemas para calcular quantidade de calorias da atividade')
            return super().form_invalid(form)
    
    def get_success_url(self):
        messages.success(self.request, 'Registro da atividade cadastrado com sucesso!!')
        return reverse(self.success_url)

class RegistroAtividadeUpdateView(LoginRequiredMixin, StaffRequiredMixin, UpdateView):
    model = RegistroAtividade
    template_name = 'registro_atividade/registro_atividade_form.html'
    form_class = ClienteForm    
    success_url = 'registro_atividade_list'
    
    def form_valid(self, form):
        atividade = form.save(commit=False)
        atividade.total_calorias = 0
        
        try:
            atividade.save()
            return super().form_valid(form)
        except Exception as e:
            messages.error(self.request, 'Problemas para calcular quantidade de calorias da atividade')
            print(e)
            return super().form_invalid(form)

    def get_success_url(self):
        messages.success(self.request, 'Registro da atividade atualizado com sucesso!!')
        return reverse(self.success_url)


class RegistroAtividadeDeleteView(LoginRequiredMixin, StaffRequiredMixin, DeleteView):
    model = RegistroAtividade
    template_name = 'registro_atividade/registro_atividade_confirm_delete.html'
    success_url = 'registro_atividade_list'
    
    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()		
        success_url = self.get_success_url()
        try:
            self.object.delete()
            messages.success(request, 'Registro de atividade física excluído com sucesso!') 
        except Exception as e:
            messages.error(request, 'Há dependências ligadas a esse registro, permissão negada!')
        return redirect(self.success_url)