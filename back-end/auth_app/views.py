import json

from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.http import require_POST

from rest_framework import permissions
from rest_framework.authentication import SessionAuthentication
from rest_framework.views import APIView


@ensure_csrf_cookie
def get_csrf_token(request):
    return JsonResponse({"message":"got CSRF token"})


@require_POST
def login_view(request):
    data = json.loads(request.body)
    username = data.get('username')
    password = data.get('password')
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return JsonResponse({"message":'You are logged in'})
    else:
        return JsonResponse({"message":'Login failed'}, status=500)


class CheckAuth(APIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        return JsonResponse({"message": "You did it!"})
