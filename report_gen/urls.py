from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('genprotocolreport', views.genprotocolreport),
    path('reportgeneration', views.reportgeneration),
]