import six
from django.conf import settings
from django.contrib.auth.hashers import check_password, make_password
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.translation import gettext_lazy as _
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from user.models import User
from user.serializers import RegisterSerializer, ActivateSerializer, ChangePasswordSerializer


class TokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (
            six.text_type(user.pk) + six.text_type(timestamp) +
            six.text_type(user.is_active)
        )


account_activation_token = TokenGenerator()


class RegisterAPIView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data.pop('password_2')
        user = serializer.save(is_active=False)
        mail_subject = _('Activate your TPL account.')
        try:
            message = render_to_string('acc_active_email_endpoint.html', {
                'email': user.email,
                'fronted_domain': settings.FRONTED_DOMAIN,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            to_email = serializer.validated_data['email']
            email = EmailMessage(
                mail_subject, message, to=[to_email]
            )
            email.send()
        except:
            user.delete()
            return Response(
                {"error_message": _("Error send activation email.")}, status=status.HTTP_503_SERVICE_UNAVAILABLE)
        return Response(status=status.HTTP_201_CREATED)


class ActivateAPIView(APIView):
    def post(self, request):
        serializer = ActivateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            uid = force_text(urlsafe_base64_decode(serializer.validated_data['uid']))
            user = User.objects.get(pk=uid)
            if user.is_active:
                return Response({"error_message": _("User already activated.")}, status=status.HTTP_400_BAD_REQUEST)
        except(TypeError, ValueError, OverflowError, User.DoesNotExist):
            return Response({"error_message": _("This user does not exists.")}, status=status.HTTP_400_BAD_REQUEST)
        if account_activation_token.check_token(user, serializer.validated_data['token']):
            user.is_active = True
            user.save()
        return Response({"message": _("User activated.")}, status=status.HTTP_200_OK)


class ChangePasswordAPIView(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def post(self, request):
        serializer = ChangePasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        if not check_password(serializer.validated_data['old_password'], request.user.password):
            return Response(
                {"old_password": [_("The old_password is not correct.")]}, status=status.HTTP_400_BAD_REQUEST)
        user = self.request.user
        user.password = make_password(serializer.validated_data['new_password'])
        user.save()
        return Response({"message": _("User updated.")}, status=status.HTTP_200_OK)
