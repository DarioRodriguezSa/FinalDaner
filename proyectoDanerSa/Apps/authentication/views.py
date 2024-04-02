# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from django.urls import reverse
from django.contrib.auth.views import PasswordResetConfirmView

def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == "POST":
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/")
            else:
                msg = '¡Usuario o contraseña invalido!'
        else:
            msg = '¡Ha ocurrido un error!'
    return render(request, "accounts/login.html", {"form": form, "msg": msg})


def forgot_password(request):
    return render(request, "accounts/recuperacion_de_contra.html")  




def custom_password_reset_confirm(request, uidb64=None, token=None, *args, **kwargs):
    return PasswordResetConfirmView.as_view(
        template_name='accounts/password_reset_email.html',
        success_url='/accounts/reset/done/'
    )(request, uidb64=uidb64, token=token, *args, **kwargs)


    #return render(request, "accounts/recuperacion_de_contra.html")
    #return render(request, "accounts/confirmar_cambio_contra.html")
