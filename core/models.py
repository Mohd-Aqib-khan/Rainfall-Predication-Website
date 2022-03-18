from distutils.command.upload import upload
from pyexpat import model
from django.db import models

# Create your models here.


class Destination:
    id: int
    name: str
    img: str
    desc: str
    price: int


class State(models.Model):
    name = models.CharField(max_length=150)
    img = models.ImageField(upload_to="myimage", default="")
    desc = models.CharField(max_length=200)
    price = models.IntegerField()


class Slider(models.Model):
    img = models.ImageField(upload_to='slider', default="")


st = State.objects.all()
l = []
for state in st:
    l.append(state.name)
print(l)
