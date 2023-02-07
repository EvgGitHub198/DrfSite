from django.shortcuts import render
from rest_framework import generics
from .serializers import MenSerializer
from .models import Men


class MenAPIView(generics.ListAPIView):
     queryset = Men.objects.all()
     serializer_class = MenSerializer

