from django.urls import path
from .views import set_csrf_token, login_view, CheckAuth

urlpatterns = [
  path('set/', set_csrf_token),
  path('login/', login_view),
  path('test/', CheckAuth.as_view())
]
