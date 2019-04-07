from django.db import models

# Create your models here.



class Sepsis(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    data = models.CharField(max_length=100,default="Enter Patient's data in format - glucose,Hemoglobin,capillary_ph,color_score or upload it in file format")
    file = models.FileField(default='', blank=True)



class Query(models.Model):

    full_name= models.CharField(max_length=50, default="",blank= False)
    contact_no = models.IntegerField(blank=True)
    email = models.CharField(max_length=50, default="",blank= False)
    detail = models.CharField(max_length=100)
