from logging.config import valid_ident
from typing import Protocol
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate, get_user_model
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import EmailMessage
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.db.models.query_utils import Q

from .forms import UserRegistrationForm, UserLoginForm, UserUpdateForm, SetPasswordForm, PasswordResetForm
from .decorators import user_not_authenticated
from .tokens import account_activation_token
from .models import SubscribedUsers, CustomUser

from django.http import JsonResponse
from .models import CustomUser
import json

from siteapp.models import Book


def activate(request, uidb64, token):
    User = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except:
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()

        messages.success(request, "Gracias por confirmar tu correo electrónico. Ahora puedes iniciar sesión en tu cuenta.")
        return redirect('login')
    else:
        messages.error(request, "El enlace de activación es inválido")

    return redirect('login')

def activateEmail(request, user, to_email):
    mail_subject = "Activa tu cuenta de usuario."
    message = render_to_string("template_activate_account.html", {
        'user': user.username,
        'domain': get_current_site(request).domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': account_activation_token.make_token(user),
        "protocol": 'https' if request.is_secure() else 'http'
    })
    email = EmailMessage(mail_subject, message, to=[to_email])
    if email.send():
        messages.success(request, f'Querido <b>{user}</b>, Por favor, ve a tu correo electrónico. <b>{to_email}</b> bandeja de entrada y haz clic en \
                recibiste un enlace de activación para confirmar y completar tu registro <b>Note:</b> Verifica tu carpeta de correo no deseado (spam).')
    else:
        messages.error(request, f'Problema al enviar correo electrónico a {to_email}, verifica si lo escribiste correctamente')


@user_not_authenticated
def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active=False
            user.save()
            activateEmail(request, user, form.cleaned_data.get('email'))
            return redirect('login')

        else:
            for error in list(form.errors.values()):
                messages.error(request, error)

    else:
        form = UserRegistrationForm()

    return render(
        request=request,
        template_name="users/register.html",
        context={"form": form}
        )

@login_required
def custom_logout(request):
    logout(request)
    return redirect(f"http://localhost:3000/?authenticated=false&username=null")

@user_not_authenticated
def custom_login(request):
    if request.method == "POST":
        form = UserLoginForm(request=request, data=request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password"],
            )
            if user is not None:
                login(request, user)
                return redirect(f"http://localhost:3000/?authenticated=true&username={user.username}")

        else:
            for key, error in list(form.errors.items()):
                if key == 'captcha' and error[0] == 'Este campo es obligatorio':
                    messages.error(request, "Debes pasar la prueba reCAPTCHA")
                    continue
                
                messages.error(request, error) 

    form = UserLoginForm()

    return render(
        request=request,
        template_name="users/login.html",
        context={"form": form}
        )


def profile(request, username):
    if request.method == "POST":
        user = request.user
        form = UserUpdateForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            user_form = form.save()
            messages.success(request, f'{user_form.username}, Tu perfil ha sido actualizado')
            return redirect("profile", user_form.username)

        for error in list(form.errors.values()):
            messages.error(request, error)

    user = get_user_model().objects.filter(username=username).first()
    if user:
        form = UserUpdateForm(instance=user)
        form.fields['description'].widget.attrs = {'rows': 1}
        return render(
            request=request,
            template_name="users/profile.html",
            context={"form": form}
            )
    
    return redirect("http://localhost:3000/")

@login_required
def password_change(request):
    user = request.user
    if request.method == 'POST':
        form = SetPasswordForm(user, request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Tu contraseña ha sido actualizada")
            return redirect('login')
        else:
            for error in list(form.errors.values()):
                messages.error(request, error)

    form = SetPasswordForm(user)
    return render(request, 'password_reset_confirm.html', {'form': form})

@user_not_authenticated
def password_reset_request(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            user_email = form.cleaned_data['email']
            associated_user = get_user_model().objects.filter(Q(email=user_email)).first()
            if associated_user:
                subject = "Solicitud de restablecimiento de contraseña"
                message = render_to_string("template_reset_password.html", {
                    'user': associated_user,
                    'domain': get_current_site(request).domain,
                    'uid': urlsafe_base64_encode(force_bytes(associated_user.pk)),
                    'token': account_activation_token.make_token(associated_user),
                    "protocol": 'https' if request.is_secure() else 'http'
                })
                email = EmailMessage(subject, message, to=[associated_user.email])
                if email.send():
                    messages.success(request,
                        """
                        <h2>Se ha enviado el restablecimiento de contraseña</h2><hr>
                        <p>
                            Hemos enviado instrucciones por correo electrónico para configurar tu contraseña, si existe una cuenta con el correo electrónico que ingresaste.
                            Deberías recibirlos en breve.<br>Si no recibes un correo electrónico, por favor asegúrate de haber ingresado la dirección con la que te registraste 
                            y verifica tu carpeta de correo no deseado (spam).
                        </p>
                        """
                    )
                else:
                    messages.error(request, "Problema al enviar el correo electrónico para restablecer la contraseña, <b>SERVER PROBLEM</b>")

            return redirect('login')

        for key, error in list(form.errors.items()):
            if key == 'captcha' and error[0] == 'Este campo es obligatorio.':
                messages.error(request, "Debes pasar la prueba reCAPTCHA")
                continue

    form = PasswordResetForm()
    return render(
        request=request, 
        template_name="password_reset.html", 
        context={"form": form}
        )

def passwordResetConfirm(request, uidb64, token):
    User = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except:
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        if request.method == 'POST':
            form = SetPasswordForm(user, request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Tu contraseña ha sido configurada. Puedes continuar e <b>iniciar sesión </b> ahora.")
                return redirect('login')
            else:
                for error in list(form.errors.values()):
                    messages.error(request, error)

        form = SetPasswordForm(user)
        return render(request, 'password_reset_confirm.html', {'form': form})
    else:
        messages.error(request, "El link ha expirado")

    messages.error(request, 'Hubo un problema, redirigiendo de vuelta a la página de inicio')
    return redirect("login")


def subscribe(request):
    if request.method == 'POST':
        name = request.POST.get('name', None)
        email = request.POST.get('email', None)

        if not name or not email:
            messages.error(request, "Debes ingresar un nombre y un correo electrónico legítimos para suscribirte al boletín informativo")
            return redirect("login")

        if get_user_model().objects.filter(email=email).first():
            messages.error(request, f"Se encontró un usuario registrado con el correo electrónico {email} asociado. Debes iniciar sesión para suscribirte o cancelar la suscripción")
            return redirect(request.META.get("HTTP_REFERER", "/")) 

        subscribe_user = SubscribedUsers.objects.filter(email=email).first()
        if subscribe_user:
            messages.error(request, f"{email} correo electrónico ya está suscrito")
            return redirect(request.META.get("HTTP_REFERER", "/"))  

        try:
            validate_email(email)
        except ValidationError as e:
            messages.error(request, e.messages[0])
            return redirect("/")

        subscribe_model_instance = SubscribedUsers()
        subscribe_model_instance.name = name
        subscribe_model_instance.email = email
        subscribe_model_instance.save()
        messages.success(request, f'{email} el correo electrónico fue suscrito satisfactoriamente')
        return redirect(request.META.get("HTTP_REFERER", "/"))  
    
