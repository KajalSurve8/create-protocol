from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('protocol', views.page_1),
    path('protocol_page2', views.page_2),
    path('protocol_page3', views.page_3),
    path('schedule', views.schedule),
    path('login', views.login),
    path('dashboard', views.dashboard),
    path('updatesample', views.updatesample),
]