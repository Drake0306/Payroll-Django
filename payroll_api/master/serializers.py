from .models import site
from .models import department
from .models import designation
from .models import bank
from .models import state
# initilise 
from rest_framework import serializers

class siteSerializer(serializers.ModelSerializer):
    class Meta:
        model = site
        fields = '__all__'

class departmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = department
        fields = '__all__'

class designationSerializer(serializers.ModelSerializer):
    class Meta:
        model = designation
        fields = '__all__'

class bankSerializer(serializers.ModelSerializer):
    class Meta:
        model = bank
        fields = '__all__'

class stateSerializer(serializers.ModelSerializer):
    class Meta:
        model = state
        fields = '__all__'
