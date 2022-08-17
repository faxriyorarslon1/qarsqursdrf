from xml.parsers.expat import model
from .models import AboutUs
from rest_framework import serializers

class AboutUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUs
        fields = "__all__"