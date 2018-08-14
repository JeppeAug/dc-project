from django.urls import path

from . import views

urlpatterns = [
    path('', views.Beregning1, name='Beregning1'),
]
