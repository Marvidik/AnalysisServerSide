from rest_framework import serializers
from .models import GoogleData

class GoogleDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoogleData
        fields = '__all__'
