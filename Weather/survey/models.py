# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

#Create your models here.
class GlobalData(models.Model):
	city = models.IntegerField(default=0)
	unit = models.CharField(max_length=5)
	trialsLeft = models.CommaSeparatedIntegerField(max_length=200)


class Trial(models.Model):
	idNo = models.IntegerField(default=0)
	week = models.IntegerField(default=0)
	dates = models.CommaSeparatedIntegerField(max_length=200)
	highs = models.CommaSeparatedIntegerField(max_length=200)
	lows = models.CommaSeparatedIntegerField(max_length=200)
	colour = models.CharField(max_length=8)



class Response(models.Model):
	week = models.IntegerField(default=0)
	normal = models.IntegerField(default=0)
	confidence = models.IntegerField(default=0)


class Participants(models.Model):
	participant_id = models.IntegerField(default=0)
	last_trial = models.IntegerField(default=0)