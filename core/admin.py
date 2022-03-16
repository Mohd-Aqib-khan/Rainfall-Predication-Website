from django.contrib import admin
from core.models import Destination, State, Slider
# Register your models here.


@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'img', 'desc', 'price')


@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ('id', 'img')
