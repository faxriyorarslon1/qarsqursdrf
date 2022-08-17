from django.urls import path

from .views import ListCreateAboutUs

urlpatterns = [ 
    path('', ListCreateAboutUs.as_view())
]