from rest_framework import serializers

class ParsingSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=500)
    location = serializers.CharField(max_length=300)
    price = serializers.CharField(max_length=500)
    description = serializers.CharField(max_length=1000)
    
          