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

from .models import HistoricoPeso
from .forms import BuscaHistoricoPesoForm
from .forms import HistoricoPesoForm


class HistoricoPesoListView(LoginRequiredMixin, ListView):
    model = HistoricoPeso
    template_name = 'historico_peso/historico_peso_list.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.GET:
            #quando ja tem dado filtrando
            context['form'] = BuscaHistoricoPesoForm(data=self.request.GET)
        else:
            #quando acessa sem dado filtrando
            context['form'] = BuscaHistoricoPesoForm()
        return context

    def get_queryset(self):
        qs = HistoricoPeso.objects.all()

        if self.request.GET:
            #quando ja tem dado filtrando
            form = BuscaHistoricoPesoForm(data=self.request.GET)
        else:
            #quando acessa sem dado filtrando
            form = BuscaHistoricoPesoForm()

        if form.is_valid():
            # cliente = form.cleaned_data.get('cliente')
            data = form.cleaned_data.get('data')

            # if cliente:
            #     qs = qs.filter(cliente__nome__icontains=cliente)

            if data:
                qs = qs.filter(data__icontains=data)
        return qs

class HistoricoPesoCreateView(LoginRequiredMixin, CreateView):
    model = HistoricoPeso
    template_name = 'historico_peso/historico_peso_form.html'
    form_class = HistoricoPesoForm
    success_url = 'historico_peso_list'
    
    def form_valid(self, form):
        hp = form.save(commit=False)
        
        try:
            hp.cliente = self.request.user 
            hp.imc = hp.peso / (hp.cliente.altura * hp.cliente.altura)
            hp.tmb = 0
            hp.save()
            return super().form_valid(form)
        except Exception as e:
            # messages.error(self.request, e)
            messages.error(self.request, 'Problemas para calcular IMC (Índice de Massa Corpórea) e TMB (Taxa Metabólica Basal). Há campos vazios ou nulos.')
            return super().form_invalid(form)
    
    def get_success_url(self):
        messages.success(self.request, 'Registro de atualização de peso realizado com sucesso!!')
        return reverse(self.success_url)

class HistoricoPesoUpdateView(LoginRequiredMixin, UpdateView):
    model = HistoricoPeso
    template_name = 'historico_peso/historico_peso_form.html'
    form_class = orm_class = HistoricoPesoForm
    success_url = 'historico_peso_list'
    
    def form_valid(self, form):
        hp = form.save(commit=False)
        hp.imc = hp.peso / (hp.cliente.altura * hp.cliente.altura)
        hp.tmb = 0
        
        try:
            hp.save()
            return super().form_valid(form)
        except Exception as e:
            messages.error(self.request, 'Problemas para calcular IMC (Índice de Massa Corpórea) e TMB (Taxa Metabólica Basal). Há campos vazios ou nulos.')
            return super().form_invalid(form)
    
    def get_success_url(self):
        messages.success(self.request, 'Registro de atualização de peso realizado com sucesso!!')
        return reverse(self.success_url)


class HistoricoPesoDeleteView(LoginRequiredMixin, DeleteView):
    model = HistoricoPeso
    template_name = 'historico_peso/historico_peso_confirm_delete.html'
    success_url = 'historico_peso_list'
    
    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()		
        success_url = self.get_success_url()
        try:
            self.object.delete()
            messages.success(request, 'Registro de histórico de pso excluído com sucesso!') 
        except Exception as e:
            messages.error(request, 'Há dependências ligadas a esse registro, permissão negada!')
        return redirect(self.success_url)