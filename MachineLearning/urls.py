from django.urls import path

from MachineLearning import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('statecomparsion/', views.stateComparsion, name='statecomparsion'),
]
