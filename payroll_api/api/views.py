from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
@api_view(['GET'])
def url_data(request):
    data = {
        'login': '/login/<id>/',
        'list': 'data',
    }
    return Response(data)