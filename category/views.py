from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Category
from .serializers import CategorySerializer


class CategoryListApiView(APIView):
    def get(self, request):
        products = Category.objects.all()
        serializers = CategorySerializer(products, many=True)
        return Response(serializers.data)



class CategoryCreateApiView(APIView):

    def post(self, request):
        serializers = CategorySerializer(data=request.data)
        if serializers.is_valid():
           serializers.save()
           return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)