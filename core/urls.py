from unicodedata import name
from django.urls import path, include

from core.views import *

urlpatterns = [
    path("", index, name="home"),
    path("contact/", contact, name="contact"),
    path("about/", about, name="about"),
    # path("validate/",views.validate_email,name="validate_email"),
    path('newsletter/',email,name='email'),
    path('predict/',predictions,name="predict")
]
