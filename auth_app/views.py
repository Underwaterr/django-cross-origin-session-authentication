import json

from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.http import require_POST

from rest_framework import permissions
from rest_framework.authentication import SessionAuthentication
from rest_framework.views import APIView


@ensure_csrf_cookie
def set_csrf_token(request):
    return JsonResponse({"ok": True})


def get_csrf(request):
    response = JsonResponse({'detail': 'CSRF cookie set'})
    response['X-CSRFToken'] = get_token(request)
    return response


@require_POST
def login_view(request):
    data = json.loads(request.body)
    username = data.get('username')
    password = data.get('password')
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return JsonResponse({"ok":True})
    else:
        return JsonResponse({"ok": False})


class CheckAuth(APIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        return JsonResponse({"ok": True})
