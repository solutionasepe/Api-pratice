from django.shortcuts import render
from django.http import JsonResponse
import json
from django.forms.models import model_to_dict 
from product.models import product
from rest_framework.response import Response
from rest_framework.decorators import api_view   
from .serializers import ProductSerializer
# Create your views here.


@api_view(['GET'])
def api_view(request, *args, **kwargs):
    instance = product.objects.all().order_by("?").first()
    data = {}

    if instance:
        data = ProductSerializer(instance).data
    return Response(data)
