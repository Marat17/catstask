from cats.models import Cat
from rest_framework import serializers


class CatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cat
        fields = ('name','age', 'breed', 'hair_color', 'user')
