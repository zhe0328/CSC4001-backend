"""FlippedWebsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login', views.login),
    path('homepage', views.index),
    path('register', views.register),
    path('community', views.community),
    path('community_video', views.community_video),
    path('trade_platform', views.trading),
    path('trade_video', views.trading_video),
    path('upload_video', views.upload_video),
    path('personal_homepage', views.single_channel_home),
    path('login_validation/', views.login_validation),  # post
    path('create_user/', views.create_user),  # post
    path('upload_video_info/', views.upload_video_info),  # post
    path('add_transaction/', views.add_transaction),  # post
    path('show_trade_platform', views.show_trade_platform),
    path('show_trade_video/', views.show_trade_video),  # post
    path('show_todo_list/', views.show_todo_list),  # post
    path('update_todo_list/', views.update_todo_list),  # post
]

