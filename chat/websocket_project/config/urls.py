from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
]
from django.urls import path
from . import views

urlpatterns = [
    path("register/", views.register, name="register"),
]