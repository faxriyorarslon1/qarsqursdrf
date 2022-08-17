from django.shortcuts import render

from mainapp.serializers import AboutUsSerializer
from .models import AboutUs
from rest_framework.generics import ListCreateAPIView
from .models import AboutUs
from rest_framework.permissions import AllowAny

class ListCreateAboutUs(ListCreateAPIView):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializer
    permission_classes = [AllowAny,]
