from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.translation import gettext_lazy as _
from rest_framework import status
from django.contrib.auth.hashers import check_password, make_password

from user.forms import RegisterForm
from user.views import account_activation_token
from user.models import User


def register(request):
    if request.POST.get('action') == 'post':
        form = RegisterForm(request.POST)
        if not form.is_valid():
            return JsonResponse({"error": form.errors}, status=status.HTTP_400_BAD_REQUEST)
        user = form.save(commit=False)
        user.is_active = False
        user.password = make_password(form.data['password'])
        user.save()
        mail_subject = _('Activate your TPL account.')
        current_site = get_current_site(request)
        try:
            message = render_to_string('acc_active_email.html', {
                'email': user.email,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            to_email = user.email
            email = EmailMessage(
                mail_subject, message, to=[to_email]
            )
            email.send()
        except:
            user.delete()
            return JsonResponse(
                {"error_message": _("Error send activation email.")}, status=status.HTTP_503_SERVICE_UNAVAILABLE)
        return JsonResponse({}, status=status.HTTP_201_CREATED)


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')

