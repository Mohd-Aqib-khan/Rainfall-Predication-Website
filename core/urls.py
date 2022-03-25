from django.urls import path, include

# drf
from rest_framework.urlpatterns import format_suffix_patterns

from core import views

urlpatterns = [
    path("", views.index, name="home"),
    path("contact/", views.contact, name="contact"),
    path("about/", views.about, name="about"),
    path("dataset",views.show_dataset,name="dataset"),
    # drf
    path('basic/',views.API_objects.as_view(),name="basic"),
    path('basic/<int:pk>/',views.API_objects_details.as_view(),name="basic_id"),
    path("getdata/",views.getdata),
    path("adddata/",views.adddata),
]

urlpatterns = format_suffix_patterns(urlpatterns)