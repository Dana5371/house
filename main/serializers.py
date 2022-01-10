from rest_framework import serializers

from main.models import Ad

class ParsingSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=500)
    location = serializers.CharField(max_length=300)
    price = serializers.CharField(max_length=500)
    description = serializers.CharField(max_length=1000)


class AdSerializer(serializers.ModelSerializer):
    created = serializers.DateTimeField(format='%d/%m/%Y %H:%M:%S', read_only=True)
    
    class Meta:
        model = Ad
        exclude = ('author',)


    def create(self, validated_data):
        request = self.context.get('request')
        user_id = request.user.id
        validated_data['author_id'] = user_id
        ad = Ad.objects.create(**validated_data)
        return ad


    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['author'] = instance.author.email
        return representation
      
    
          