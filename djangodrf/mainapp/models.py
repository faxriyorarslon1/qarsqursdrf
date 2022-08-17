from distutils.command.upload import upload
from turtle import title
from django.db import models

class AboutUs(models.Model):
    title = models.CharField(max_length=30)
    text = models.TextField(max_length=500)
    image = models.ImageField(upload_to = 'media/about/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Biz haqimizda"