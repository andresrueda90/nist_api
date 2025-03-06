from rest_framework import serializers
from .models import VulnerabilityStatus, VulnerabilityModel


class VulnerabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = VulnerabilityModel
        fields = '__all__'


class VulnerabilityStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = VulnerabilityStatus
        fields = '__all__'
