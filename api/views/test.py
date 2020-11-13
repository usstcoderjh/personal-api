from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from api import models
# Create your views here.
class UserViews(APIView):
   def post(self,request,*args, **kwargs):
      print(request.data)
      models.userModels.objects.create(**request.data)
      return Response({
         "code": 0,
         "msg": "错误",
      })

   def get(self,request,*args, **kwargs):
      query = models.userModels.objects.all().values("username","password")
      return Response(query)
