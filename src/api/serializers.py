from rest_framework import serializers
from .models import Subscriber

class HelloWorldSerializer(serializers.Serializer):
    name = serializers.CharField(required=True, max_length=10)
    age = serializers.IntegerField(required=False, min_value=10, default=10)


class SubscriberSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    email = serializers.EmailField()
    age = serializers.IntegerField()


class SubscriberModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscriber
        fields = ("name", "email", "age")