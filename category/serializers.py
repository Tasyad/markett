from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']