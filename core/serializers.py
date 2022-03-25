from pyexpat import model
from rest_framework import serializers
from core.models import Contact, Dataset

# class DrfPostSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=DrfPost
#         fields="__all__"
        
class DatasetSerializer(serializers.ModelSerializer):
    class Meta:
        model=Dataset
        fields="__all__"
        
class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model=Contact
        fields="__all__"
        
        