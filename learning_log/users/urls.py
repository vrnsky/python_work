from django.contrib import admin
from django.urls import path, re_path
from django.contrib.auth.views import login

from . import views

urlpatterns = [
	re_path(r'^login/$', login, {'template_name':'users/login.html'}, name='login'),
	path('logout/', views.logout_view, name='logout'),
	re_path(r'^register/$', views.register, name='register')
]