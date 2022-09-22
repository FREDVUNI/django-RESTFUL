from django.shortcuts import render
# Create your views here.
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from . models import companies,blog
from .serializers import companyserializer,blogserializer

class company(APIView):
    def get(self,request):
        content = companies.objects.all()
        serializer = companyserializer(content,many=True)
        return Response(serializer.data)

    def post(self,request): 
        serializer = companies(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

    def details(self,request,id):
        company = companies.objects.get(pk = id)
        serializer =companyserializer(company , many =False)
        return Response(serializer.data)

    def update(self,request,id):
        serializer = companies(instance = id,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

    def delete(self,request,id):
        company = companies.objects.get(pk=id)
        company.delete()
        return Response("The company has been deleted.")                      

class blogpost(APIView):
    def get(self,request):
        content = blog.objects.all()
        serializer = blogserializer(content,many=True)
        return Response(serializer.data)


