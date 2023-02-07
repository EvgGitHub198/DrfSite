from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import MenSerializer
from .models import Men


class MenAPIView(APIView):
     def get(self, request):
          lst = Men.objects.all().values()
          return Response({'posts': list(lst)})
     def post(self, request):
          post_new = Men.objects.create(
               title=request.data['title'],
               content=request.data['content'],
               cat_id=request.data['cat_id']
          )
          return Response({'post': model_to_dict(post_new)})


# class MenAPIView(generics.ListAPIView):
#      queryset = Men.objects.all()
#      serializer_class = MenSerializer

