from rest_framework import serializers
from . models import companies,blog

class companyserializer(serializers.ModelSerializer):
    class Meta:
        model = companies
        fields ='__all__'

class blogserializer(serializers.ModelSerializer):
    class Meta:
        model = blog
        fields = '__all__'