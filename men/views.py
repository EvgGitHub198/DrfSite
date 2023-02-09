from _ast import Is

from django.forms import model_to_dict
from django.shortcuts import render
from django.views import generic
from rest_framework import generics, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

from rest_framework.response import Response
from rest_framework.views import APIView

from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from .serializers import MenSerializer
from .models import Men, Category


# class MenViewSet(viewsets.ModelViewSet):
#      queryset = Men.objects.all()
#      serializer_class = MenSerializer
#
#      def get_queryset(self):
#           pk = self.kwargs.get('pk')
#           if not pk:
#                return Men.objects.all()[:3]
#           return Men.objects.filter(pk=pk)
#
#
#      @action(methods=['get'], detail=True)
#      def category(self, request, pk=None):
#           cats = Category.objects.get(pk=pk)
#           return Response({'cats': cats.name})


class MenAPIList(generics.ListCreateAPIView):
     queryset = Men.objects.all()
     serializer_class = MenSerializer
     permission_classes = (IsAuthenticatedOrReadOnly, )


class MenAPIUpdate(generics.UpdateAPIView):
     queryset = Men.objects.all()
     serializer_class = MenSerializer
     permission_classes = (IsAuthenticated, )
     # authentication_classes = (TokenAuthentication, )

class MenAPIDestroy(generics.RetrieveDestroyAPIView):
     queryset = Men.objects.all()
     serializer_class = MenSerializer
     permission_classes = (IsAdminOrReadOnly, )



