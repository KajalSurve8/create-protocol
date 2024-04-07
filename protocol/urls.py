from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('formulationpage', views.formulationpage, name="formulationpage"),
    path('tabletspage', views.tabletspage, name="tabletspage"),
    path('frequencypage', views.frequencypage, name="frequencypage"),
    path('hardcapsulespage', views.hardcapsulespage, name="hardcapsulespage"),
    path('softcapsulespage', views.softcapsulespage, name="softcapsulespage"),
]