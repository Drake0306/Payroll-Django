# serializers
from .serializers import Usertable_Serializer
from .serializers import Permission_Serializer
from django.shortcuts import render

# models
from django.contrib.auth.models import User
from .models import USERTABLE, PERMISSION



# django rest import
from rest_framework.decorators import api_view
from rest_framework import generics, permissions
from rest_framework.response import Response
from datetime import datetime



# Create your views here.
@api_view(['GET','POST'])
def login(request):
    if request.method == 'POST':

        # Checking returing query set
        UserAccountData = USERTABLE.objects.filter(user_name= request.data.get("user_name"), password= request.data.get("password"))
        if UserAccountData:
            # get data 
            UserAccountData = USERTABLE.objects.get(user_name= request.data.get("user_name"), password= request.data.get("password"))
            
            # Get current data
            now = datetime.now()
            current_time = now.strftime("%H:%M")

            # Store tn a local json
            UserAccountDataResponse = {
                'id': UserAccountData.id,
                'username': UserAccountData.user_name,
                'name': UserAccountData.name,
                'time': current_time
            }
            
            return Response(UserAccountDataResponse)

        else: 
            # for empty value
            UserAccountData = {
                'status': '400'
            }
        return Response(UserAccountData)
    else:
        UserSerializerData = [{
            'username': request.session.get('username'),
        }]
        return Response(UserSerializerData)
    

