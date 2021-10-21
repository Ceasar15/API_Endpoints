from rest_framework import serializers
from rest_framework.fields import ReadOnlyField
from users.models import Profile


class ProfileSerialzer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    bio = serializers.CharField(required=False, max_length = 100)
    age = serializers.IntegerField(required =False)
    location = serializers.CharField(required=False)

    def create(self, validated_data):
        return Profile.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.bio = validated_data.get('bio', instance.bio)
        instance.age = validated_data.get('age', instance.age)
        instance.location = validated_data.get('location', instance.location)
        instance.save()
        return instance
