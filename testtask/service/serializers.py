from os import path

from django.db.models import fields
from rest_framework import serializers
from .models import album

class album_seial(serializers.Serializer):
    userId = serializers.IntegerField()
    id  = serializers.IntegerField()
    title = serializers.CharField(max_length=100)
    
    
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.userid = validated_data.get('userid', instance.id)
        instance.id = validated_data.get('id', instance.id)
        instance.save()
        return instance

class album_detail(serializers.Serializer):
    id1 = serializers.IntegerField()
    albumId  = serializers.IntegerField()
    title = serializers.CharField(max_length=100)
    path = serializers.CharField(max_length=100)
    thumbnailUrl = serializers.CharField(max_length=100)
    

class update_serial(serializers.ModelSerializer):
    class Meta:
        model = album
        fields = "__all__"
