from os import name

from . import views
from django.urls import path

urlpatterns = [

    path('', views.about, name='about'),
    # path('operations/', views.operations, name='operations')




]
