from rest_framework import serializers
 
from .models import data

class dataSerilizer(serializers.ModelSerializer):
    class Meta:
        model = data
        fields = ('status',)