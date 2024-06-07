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

from .models import RegistroRefeicao
from .forms import BuscaRefeicaoForm
from .forms import ClienteForm


class RegistroRefeicaoListView(LoginRequiredMixin, StaffRequiredMixin, ListView):
    model = RegistroRefeicao
    template_name = 'registro_refeicao/registro_refeicao_list.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.GET:
            #quando ja tem dado filtrando
            context['form'] = BuscaRefeicaoForm(data=self.request.GET)
        else:
            #quando acessa sem dado filtrando
            context['form'] = BuscaRefeicaoForm()
        return context

    def get_queryset(self):
        qs = RegistroRefeicao.objects.all()

        if self.request.GET:
            #quando ja tem dado filtrando
            form = BuscaRefeicaoForm(data=self.request.GET)
        else:
            #quando acessa sem dado filtrando
            form = BuscaRefeicaoForm()

        if form.is_valid():
            cliente = form.cleaned_data.get('cliente')
            alimento = form.cleaned_data.get('alimento')
            data = form.cleaned_data.get('data')

            if cliente:
                qs = qs.filter(cliente__nome__icontains=cliente)

            if alimento:
                qs = qs.filter(alimento__descricao__icontains=alimento)

            if data:
                qs = qs.filter(data__icontains=data)
        return qs

class RegistroRefeicaoCreateView(LoginRequiredMixin, StaffRequiredMixin, CreateView):
    model = RegistroRefeicao
    template_name = 'registro_refeicao/registro_refeicao_form.html'
    form_class = ClienteForm
    success_url = 'registro_refeicao_list'
    
    def form_valid(self, form):
        refeicao = form.save(commit=False)
        refeicao.total_calorias = refeicao.alimento.calorias * refeicao.quantidade
        refeicao.total_carboidratos = refeicao.alimento.carboidratos * refeicao.quantidade
        try:
            refeicao.save()
            return super().form_valid(form)
        except Exception as e:
            messages.error(self.request, 'Problemas para calcular quantidade de calorias e carboidratos dessa refeição')
            return super().form_invalid(form)
    
    def get_success_url(self):
        messages.success(self.request, 'Registro da refeição cadastrado com sucesso!!')
        return reverse(self.success_url)

class RegistroRefeicaoUpdateView(LoginRequiredMixin, StaffRequiredMixin, UpdateView):
    model = RegistroRefeicao
    template_name = 'registro_refeicao/registro_refeicao_form.html'
    form_class = ClienteForm
    success_url = 'registro_refeicao_list'
    
    def form_valid(self, form):
        refeicao = form.save(commit=False)
        refeicao.total_calorias = refeicao.alimento.calorias * refeicao.quantidade
        refeicao.total_carboidratos = refeicao.alimento.carboidratos * refeicao.quantidade
        try:
            refeicao.save()
            return super().form_valid(form)
        except Exception as e:
            messages.error(self.request, 'Problemas para calcular quantidade de calorias e carboidratos dessa refeição ')
            print(e)
            return super().form_invalid(form)

    def get_success_url(self):
        messages.success(self.request, 'Registro da refeição atualizado com sucesso!!')
        return reverse(self.success_url)


class RegistroRefeicaoDeleteView(LoginRequiredMixin, StaffRequiredMixin, DeleteView):
    model = RegistroRefeicao
    template_name = 'registro_refeicao/registro_refeicao_confirm_delete.html'
    success_url = 'registro_refeicao_list'
    
    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()		
        success_url = self.get_success_url()
        try:
            self.object.delete()
            messages.success(request, 'Registro de refeição excluído com sucesso!') 
        except Exception as e:
            messages.error(request, 'Há dependências ligadas a esse registro, permissão negada!')
        return redirect(self.success_url)