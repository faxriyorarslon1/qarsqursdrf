from django.urls import path

from .views import AboutUsDelete, ListCreateAboutUs, AboutRetrieveAPIView

urlpatterns = [ 
    path('', ListCreateAboutUs.as_view()),
    path('get/<int:pk>', AboutRetrieveAPIView.as_view()),
    path('delete/<int:pk>', AboutUsDelete.as_view()),
]