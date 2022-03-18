from django.urls import path, include

from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path('stateview/<int:sid>/', views.state_view, name='stateview')
]
