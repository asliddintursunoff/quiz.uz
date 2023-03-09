from rest_framework import routers, serializers, viewsets
from .models import *


class FanlarSerializers(serializers.ModelSerializer):
    class Meta:
        model = Fanlar
        fields = '__all__'


class LevelSerializers(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = '__all__'


class TestSerializers(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = '__all__'









