from django.conf import settings
from django.contrib import messages
from django.contrib.auth import login
from django.shortcuts import redirect
from django.urls import reverse

from django.views.generic import ListView,TemplateView, DetailView, RedirectView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from mail_templated import EmailMessage

from utils.decorators import LoginRequiredMixin, StaffRequiredMixin

from .models import Usuario
from .forms import UsuarioRegisterForm, BuscaUsuarioForm


class UsuarioListView(LoginRequiredMixin, ListView):
    model = Usuario
    template_name = 'usuario/usuario_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.GET:
            #quando ja tem dado filtrando
            context['form'] = BuscaUsuarioForm(data=self.request.GET)
        else:
            #quando acessa sem dado filtrando
            context['form'] = BuscaUsuarioForm()
        return context

    def get_queryset(self):
        qs = Usuario.objects.all()

        if self.request.GET:
            #quando ja tem dado filtrando
            form = BuscaUsuarioForm(data=self.request.GET)
        else:
            #quando acessa sem dado filtrando
            form = BuscaUsuarioForm()

        if form.is_valid():
            nome_usuario = form.cleaned_data.get('nome_usuario')
            tipo = form.cleaned_data.get('tipo')

            if nome_usuario:
                qs = qs.filter(nome__icontains=nome_usuario)

            if tipo:
                qs = qs.filter(tipo__icontains=tipo)
        return qs
    
    
class UsuarioCreateView(LoginRequiredMixin, CreateView):
    model = Usuario
    fields = ['tipo', 'nome', 'email', 'password','cpf' , 'fone', 'is_active', 'data_nascimento', 'sexo']
    success_url = 'usuario_list'
    
    def get_success_url(self):
        messages.success(self.request, 'Usuário cadastrado com sucesso na plataforma!')
        return reverse(self.success_url)


class UsuarioUpdateView(LoginRequiredMixin, UpdateView):
    model = Usuario
    fields = ['tipo', 'nome', 'email', 'cpf', 'fone', 'is_active', 'data_nascimento', 'sexo']
    template_name = 'usuario/usuario_form_update.html'
    success_url = 'usuario_list'
    
    def get_success_url(self):
        messages.success(self.request, 'Dados do usuário atualizados com sucesso na plataforma!')
        return reverse(self.success_url)


class UsuarioDeleteView(LoginRequiredMixin, DeleteView):
    model = Usuario
    success_url = 'usuario_list'

    def delete(self, request, *args, **kwargs):
        """
        Call the delete() method on the fetched object and then redirect to the
        success URL. If the object is protected, send an error message.
        """
        self.object = self.get_object()
        success_url = self.get_success_url()
        try:
            self.object.delete()
        except Exception as e:
            messages.error(request, 'Há dependências ligadas à esse usuário, permissão negada!')
        return redirect(self.success_url)


class UsuarioRegisterView(CreateView):
    model = Usuario
    form_class = UsuarioRegisterForm
    template_name = 'usuario/usuario_register_form.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        return super(UsuarioRegisterView, self).form_valid(form)
    
    def get_success_url(self):
        message = EmailMessage('usuario/email/validacao_email.html', {'usuario': self.object},
                               settings.EMAIL_HOST_USER, to=[self.object.email])
        message.send()     
        return reverse('usuario_register_success')


class UsuarioRegisterSuccessView(TemplateView):
    template_name= 'usuario/usuario_register_success.html'


class UsuarioRegisterActivateView(RedirectView):
    models = Usuario

    def get_redirect_url(self, *args, **kwargs):
        self.object = Usuario.objects.get(slug=kwargs.get('slug'))
        self.object.is_active = True
        self.object.save()
        login(self.request, self.object)
        messages.success(self.request, 'Obrigado por acessar o Sistema Online de Monitoramento de Diabetes. Esta é a sua área restrita de acompanhamento e registros.')
        return reverse('home')