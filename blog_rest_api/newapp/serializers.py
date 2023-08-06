# serializers.py

from rest_framework import serializers
from .models import YourModel

class YourModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = YourModel
        fields = '__all__'  # You can specify specific fields instead of '__all__'
