# from django.test import TestCase

# # Create your tests here.
from core.models import State
s = State.objects.all()
print(s)
