# myapp/serializers.py
from rest_framework import serializers
from .models import CRUD


class CRUDSerializer(serializers.ModelSerializer):
    class Meta:
        model = CRUD
        fields = ["id", "name", "age", "designation"]
