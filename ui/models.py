from __future__ import unicode_literals

from django.db import models

class User(models.Model):
	Email = models.CharField(max_length=50)
	Password = models.CharField(max_length=50)

class Cevent(models.Model):
	GpsLat = models.FloatField()
	GpsLng = models.FloatField()
	GpsPositionRawData = models.CharField(max_length=50)
	Owner = models.ForeignKey(User)
	Title = models.CharField(max_length=50)
	CreatedOn = models.DateField()
	ModifiedOn = models.DateField()
	StartOfEvent = models.DateField()
	EndOfEvent = models.DateField()
	Adress = models.CharField(max_length=50)
	AdressComplement = models.CharField(max_length=50)
	Price = models.FloatField()
	Description = models.TextField()
	Picture = models.ImageField()
	ChurchLink = models.CharField(max_length=50)
	YoutubeLink = models.CharField(max_length=50)
	KeyWord = models.CharField(max_length=50)
