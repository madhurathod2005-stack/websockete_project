from django.contrib import admin
from django.urls import path, include  # include needed for app URLs
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('chat/', include('chat.urls')),  # include chat app URLs
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),  # optional
    path('', views.chat_home, name='chat_home'),
    path("", views.index),
]
