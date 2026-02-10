from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.conf import settings

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status

from .serializers import RegisterSerializer


# =========================
# REGISTER USER
# =========================
class RegisterView(APIView):
    """
    POST /api/auth/register/
    {
        "username": "vasu",
        "email": "vasu@test.com",
        "password": "password123"
    }
    """

    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "User registered successfully"},
                status=status.HTTP_201_CREATED,
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )


# =========================
# LOGOUT (JWT – CLIENT SIDE)
# =========================
class LogoutView(APIView):
    """
    POST /api/auth/logout/
    JWT logout is handled on frontend by deleting token
    """

    permission_classes = [IsAuthenticated]

    def post(self, request):
        return Response(
            {"message": "Logged out successfully"},
            status=status.HTTP_200_OK,
        )


# =========================
# PASSWORD RESET REQUEST
# =========================
class PasswordResetRequestView(APIView):
    """
    POST /api/auth/forgot-password/
    {
        "email": "vasu@test.com"
    }
    """

    permission_classes = [AllowAny]

    def post(self, request):
        email = request.data.get("email")

        if not email:
            return Response(
                {"error": "Email is required"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            # 🔒 Security best practice: do not reveal user existence
            return Response(
                {"message": "If this email exists, a reset link has been sent"},
                status=status.HTTP_200_OK,
            )

        token = default_token_generator.make_token(user)
        uid = user.pk

        reset_link = f"http://localhost:5173/reset-password/{uid}/{token}"

        # 🔴 Email sending (safe to fail silently in dev)
        send_mail(
            subject="Password Reset Request",
            message=f"Reset your password using this link:\n{reset_link}",
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[email],
            fail_silently=True,
        )

        return Response(
            {"message": "If this email exists, a reset link has been sent"},
            status=status.HTTP_200_OK,
        )


# =========================
# PASSWORD RESET CONFIRM
# =========================
class PasswordResetConfirmView(APIView):
    """
    POST /api/auth/reset-password/<uid>/<token>/
    {
        "password": "newpassword123"
    }
    """

    permission_classes = [AllowAny]

    def post(self, request, uid, token):
        new_password = request.data.get("password")

        if not new_password or len(new_password) < 8:
            return Response(
                {"error": "Password must be at least 8 characters"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            user = User.objects.get(pk=uid)
        except User.DoesNotExist:
            return Response(
                {"error": "Invalid reset request"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        if not default_token_generator.check_token(user, token):
            return Response(
                {"error": "Invalid or expired token"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        user.set_password(new_password)
        user.save()

        return Response(
            {"message": "Password reset successful"},
            status=status.HTTP_200_OK,
        )
