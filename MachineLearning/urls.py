from django.urls import path

from MachineLearning import views

urlpatterns = [
    path('statecmp/', views.stateComparsion, name='statecmp'),
]
