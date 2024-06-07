from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse
from django.views.generic.base import TemplateView
from django.views.generic import RedirectView

from utils.decorators import LoginRequiredMixin, StaffRequiredMixin, ClienteRequiredMixin

from usuario.models import Usuario


class HomeRedirectView(LoginRequiredMixin, RedirectView):
    def get_redirect_url(self, **kwargs):
        if self.request.user.tipo == 'ADMINISTRADOR':
            return reverse('home')
        elif self.request.user.tipo == 'CLIENTE':
            return reverse('cliente_home')
        # if self.request.user.tipo == 'ADMINISTRADOR':
        #     return reverse('home')
        # elif self.request.user.tipo == 'COORDENADOR':
        #     return reverse('home')
        # elif self.request.user.tipo == 'SECRETÁRIA':
        #     return reverse('home')
        # elif self.request.user.tipo == 'ALUNO':
        #     return reverse('appaluno_home')
        # elif self.request.user.tipo == 'AVALIADOR CONVIDADO':
        #     return reverse('appprofessor_home')
        # elif self.request.user.tipo == 'PROFESSOR':
        #     return reverse('appprofessor_home')

    #def get_expiry_date()
    #Returns the date this session will expire. For sessions with no custom expiration 
    #(or those set to expire at browser close), this will equal the date SESSION_COOKIE_AGE seconds from now.
    #This function accepts the same keyword arguments as get_expiry_age().

    #def logout(request):
    #    try:
    #        del request.session['member_id']
    #    except KeyError:
    #        pass
    #    return HttpResponse("You're logged out.")


class HomeView(LoginRequiredMixin, StaffRequiredMixin, TemplateView):
    template_name = 'core/home.html'


class AboutView(LoginRequiredMixin, TemplateView):
    template_name = 'core/about.html' 
    
# class LandPageView():
#     template_name = 'landpage/templates/index.html'
