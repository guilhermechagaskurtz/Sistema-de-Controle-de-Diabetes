from __future__ import unicode_literals
import os
from datetime import datetime
from django.conf import settings
from django.contrib import messages
from django.db.models import Q
from django.http import Http404
from django.shortcuts import redirect
from django.shortcuts import render
from django.urls import reverse
from django.utils import timezone

from django.views.generic import ListView, RedirectView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.base import TemplateView

from mail_templated import EmailMessage

from utils.decorators import LoginRequiredMixin, ClienteRequiredMixin

from usuario.models import Usuario

class HomeRedirectView(LoginRequiredMixin, RedirectView):
    def get_redirect_url(self, **kwargs):
        if self.request.user.tipo == 'ADMINISTRADOR':
            return reverse('home')
        elif self.request.user.tipo == 'CLIENTE':
            return reverse('cliente_home')
        # elif self.request.user.tipo == 'AVALIADOR CONVIDADO':
        #     return reverse('appprofessor_home')
        # elif self.request.user.tipo == 'COORDENADOR':
        #     return reverse('home')
        # elif self.request.user.tipo == 'PROFESSOR':
        #     return reverse('appprofessor_home')
        # elif self.request.user.tipo == 'SECRETÁRIA':
        #     return reverse('home')


class HomeView(LoginRequiredMixin, ClienteRequiredMixin, TemplateView):
    template_name = 'cliente/home.html'


class AboutView(LoginRequiredMixin, ClienteRequiredMixin, TemplateView):
    template_name = 'cliente/about.html'
    

class DadosClienteUpdateView(LoginRequiredMixin, ClienteRequiredMixin, UpdateView):
    model = Usuario
    template_name = 'cliente/dados_cliente_form.html'
    fields = ['nome','cpf', 'fone', 'data_nascimento', 'sexo', 'altura']
    success_url = 'cliente_home'

    def get_object(self, queryset=None):
        return self.request.user
     
    def get_success_url(self):
        messages.success(self.request, 'Seus dados foram alterados com sucesso!')
        return reverse(self.success_url)