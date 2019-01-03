from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='scantron.index'),
    path('students/csv', views.export_students, name='export_students'),
]
