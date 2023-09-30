from django.shortcuts import render
from rest_framework import generics, status
from .models import product
from .serializers import ProductSerializer 
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.


class ProductDetailViews(generics.RetrieveAPIView):
    queryset = product.objects.all()
    serializer_class = ProductSerializer


class ProductCreateViews(generics.ListCreateAPIView):
    queryset = product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content')
        # or None
        if content is None:
            content = title
        serializer.save(content=content)

@api_view(['GET', 'POST'])
def product_alt_view( request, pk=None, *args, **kwargs):

    method = request.method

    if method == 'GET':

        if pk is not None:
            obj = product.objects.get(id=pk)
            serializer = ProductSerializer(obj)
            return Response (serializer.data)
        queryset = product.objects.all()
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)

    if method == "POST":
        queryset = product.objects.all()
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            title = serializer.validated_data.get('title')
            content = serializer.validated_data.get('content')
            # or None
            if content is None:
                content = title
            serializer.save(content=content)
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response({"invalid":"not good data"}, status=status.HTTP_400_BAD_REQUEST)

class ProductUpdate(generics.UpdateAPIView):
    queryset = product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance:
            instance.content = instance.title

class ProductDelete(generics.DestroyAPIView):
    queryset = product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    