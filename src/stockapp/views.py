from django.shortcuts import render
from .models import Category, Product

from .serializers import CategorySerializer, ProductSerializer

from rest_framework import viewsets, filters

from rest_framework.permissions import IsAuthenticatedOrReadOnly


from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]



class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_fields = ['category', 'price']
    ordering_fields = ['price', 'stock']
    search_fields = ['name', 'description']

