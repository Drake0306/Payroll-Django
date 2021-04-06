from django.shortcuts import render
from django.db import connection


# Create your views here.

# django rest import
from rest_framework import generics, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime, timedelta, date

# serilizer 
from master.serializers import UMOSerializer



from auth_user.serializers import Permission_Serializer
from auth_user.serializers import Usertable_Serializer

# model

from auth_user.models import USERTABLE


from auth_user.models import USERTABLE
from auth_user.models import PERMISSION

# import json
import json


    
