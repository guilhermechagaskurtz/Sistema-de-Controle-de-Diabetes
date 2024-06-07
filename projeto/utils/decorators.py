from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.utils.decorators import method_decorator

class LoginRequiredMixin(object):
    @classmethod
    def as_view(self, **initkwargs):
        view = super(LoginRequiredMixin, self).as_view(**initkwargs)
        return login_required(view)


class StaffRequiredMixin(object):
    """
    View mixin which requires that the authenticated user is a staff member
    (i.e. `is_staff` is True).
    """
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        if not request.user.tipo == 'ADMINISTRADOR':
            messages.error(
                request,
                'Você não tem permissão para acessar esta área ou'
                ' realizar esta operação.')
            return redirect('home_redirect')
        return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)



class ClienteRequiredMixin(object):
    """
    View mixin which requires that the authenticated user is a staff member
    (i.e. `is_staff` is True).
    """
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        if not request.user.tipo == 'CLIENTE' and not request.user.tipo == 'ADMINISTRADOR':
            messages.error(
                request,
                ' Você não tem permissão para acessar esta área'
                ' ou realizar esta operação'
            )
            return redirect('cliente_home')
        return super(ClienteRequiredMixin, self).dispatch(request,*args, **kwargs)


class SecretariaCoordenadorAdministradorRequiredMixin(object):
    """
    View mixin which requires that the authenticated user is a staff member
    (i.e. `is_staff` is True).
    """
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        if not request.user.tipo == 'COORDENADOR' and not request.user.tipo == 'ADMINISTRADOR' and not request.user.tipo == 'SECRETÁRIA':
            messages.error(
                request,
                'Você não tem permissão para acessar esta área ou'
                ' realizar esta operação.')
            return redirect('home_redirect')
        return super(SecretariaCoordenadorAdministradorRequiredMixin, self).dispatch(request,*args, **kwargs)

class CoordenadorRequiredMixin(object):
    """
    View mixin which requires that the authenticated user is a staff member
    (i.e. `is_staff` is True).
    """
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        if not request.user.tipo == 'COORDENADOR' and not request.user.tipo == 'ADMINISTRADOR':
            messages.error(
                request,
                'Você não tem permissão para acessar esta área ou'
                ' realizar esta operação.')
            return redirect('home_redirect')
        return super(CoordenadorRequiredMixin, self).dispatch(request,*args, **kwargs)    
    
class ProfessorRequiredMixin(object):
    """
    View mixin which requires that the authenticated user is a staff member
    (i.e. `is_staff` is True).
    """
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        if not request.user.tipo == 'PROFESSOR' and not request.user.tipo == 'ADMINISTRADOR':
            messages.error(
                request,
                ' Você não tem permissão para acessar esta área'
                ' ou realizar esta operação'
            )
            return redirect('appprofessor_home')
        return super(ProfessorRequiredMixin, self).dispatch(request,*args, **kwargs)
    
    
class ProfessorConvidadoRequiredMixin(object):
    """
    View mixin which requires that the authenticated user is a staff member
    (i.e. `is_staff` is True).
    """
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        if not request.user.tipo == 'PROFESSOR' and not request.user.tipo == 'ADMINISTRADOR' and not request.user.tipo == 'AVALIADOR CONVIDADO':
            messages.error(
                request,
                ' Você não tem permissão para acessar esta área'
                ' ou realizar esta operação'
            )
            return redirect('appprofessor_home')
        return super(ProfessorConvidadoRequiredMixin, self).dispatch(request,*args, **kwargs)