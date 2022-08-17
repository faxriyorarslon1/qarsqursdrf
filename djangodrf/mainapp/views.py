from django.shortcuts import render

from mainapp.serializers import AboutUsSerializer
from .models import AboutUs
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, DestroyAPIView
from .models import AboutUs
from rest_framework.permissions import IsAdminUser, AllowAny

class ListCreateAboutUs(ListCreateAPIView):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializer
    permission_classes = [IsAdminUser,]


class AboutUsDelete(DestroyAPIView):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializer
    permission_classes = [IsAdminUser,]


class AboutRetrieveAPIView(RetrieveAPIView):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializer
    permission_classes = [AllowAny,]
