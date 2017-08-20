# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

TYPE_OF_BIKES_CHOICES = (
    ('Cruiser','Cruiser'),
    ('Supersport','Supersport'),
    ('Standard','Standard')
)

COLOR_CHOICES = (
    ('White','White'),
    ('Black','Black'),
    ('Red','Red'),
    ('Yellow','Yellow'),
    ('Blue','Blue'),
    ('Silver','Silver'),
    ('Grey','Grey'),
    ('Orange','Orange'),
    ('Green','Green')
)

def content_file_name(instance,filename):
    return ''.join(['marketplace/static/marketplace/pics/', str(instance.pk), '/', filename])
# Create your models here.
class Motorcycle(models.Model):
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    color = models.CharField(choices=COLOR_CHOICES,default='Black',max_length=50)
    year = models.IntegerField(default=2017)
    mileage = models.IntegerField(default=20)
    price = models.IntegerField(default=20000)
    engineSize = models.CharField(max_length=50)
    typeOfBike = models.CharField(choices=TYPE_OF_BIKES_CHOICES,default='Standard',max_length=50)
    antiLockBrakes = models.BooleanField(default=True)
    sold = models.BooleanField(default=False)
    pics = models.FileField(upload_to=content_file_name)
    pic_1 = models.FileField(upload_to=content_file_name)
    pic_2 = models.FileField(upload_to=content_file_name)
    pic_3 = models.FileField(upload_to=content_file_name)
    pic_4 = models.FileField(upload_to=content_file_name)
    pic_5 = models.FileField(upload_to=content_file_name)
    report = models.FileField(upload_to='uploads/reports')

    def __str__(self):
        return str(self.year) + " " + self.make + " " + self.model + " (ID=" + str(self.id) + ")"