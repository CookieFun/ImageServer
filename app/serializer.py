from models import MyPhoto
from rest_framework import serializers

class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyPhoto
        fields = ('id', 'image', 'name')
        #owner = serializers.Field(source='owner.username')