from rest_framework import serializers


class HelloSerializer(serializers.Serializer):
    """Serializes the name field"""
    name = serializers.CharField(max_length=15)