from django.urls import path

from MachineLearning import views

urlpatterns = [
    path('statecomparsion', views.stateComparsion, name='statecomparsion'),
]