from django.urls import path
from .views import get_csrf_token, login_view, CheckAuth

urlpatterns = [
  path('get-csrf-token/', get_csrf_token),
  path('login/', login_view),
  path('test/', CheckAuth.as_view())
]
