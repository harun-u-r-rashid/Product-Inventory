from django.shortcuts import render
from . import serializers
from . import models

from rest_framework import generics
from rest_framework import permissions


class ProductView(generics.ListAPIView):
        queryset = models.Product.objects.all()
        serializer_class = serializers.ProductSerializer
        permission_classes = [permissions.AllowAny]


class ProductCreateView(generics.CreateAPIView):
        serializer_class = serializers.ProductSerializer
        permission_classes = [permissions.AllowAny]

        def perform_create(self, serializer):
                new_product = serializer.save()
                new_product.save()

class ProductDetailsView(generics.RetrieveAPIView):
        queryset = models.Product.objects.all()
        serializer_class = serializers.ProductSerializer
        permission_classes = [permissions.AllowAny]

        def get_object(self):
                id = self.kwargs["id"]
                product = models.Product.objects.get(id=id)
                return product
        


class ProductUpdateView(generics.UpdateAPIView):
        queryset = models.Product.objects.all()
        serializer_class = serializers.ProductSerializer
        permission_classes = [permissions.AllowAny]

        def perform_update(self, serializer):
                update_course = serializer.save()



class ProductDeleteView(generics.DestroyAPIView):
        queryset = models.Product.objects.all()
        serializer_class = serializers.ProductSerializer
        permission_classes = [permissions.AllowAny]
        


class SearchProductView(generics.ListAPIView):
        serializer_class = serializers.ProductSerializer
        permission_classes = [permissions.AllowAny]


        def get_queryset(self):
                query = self.request.GET.get("query")
                return models.Product.objects.filter(
                        name__icontains=query,

                )
        

           

