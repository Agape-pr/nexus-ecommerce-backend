from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        try:
            return Category.objects.all()
        except Exception as e:
            # Log if you have logging configured
            print(f"Error fetching categories: {str(e)}")
            return Category.objects.none()  # return empty queryset instead of crashing

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_fields = ['category', 'price']
    ordering_fields = ['price', 'stock']
    search_fields = ['name', 'description']

    def get_queryset(self):
        try:
            return Product.objects.all()
        except Exception as e:
            print(f"Error fetching products: {str(e)}")
            return Product.objects.none()

    def handle_exception(self, exc):
        response = super().handle_exception(exc)
        if response is None:
            # Unhandled exception, return 500 JSON
            return Response(
                {"success": False, "error": "Internal server error"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
        else:
            # Add consistent structure for known DRF errors
            response.data = {
                "success": False,
                "error": response.data,
                "status_code": response.status_code
            }
            return response