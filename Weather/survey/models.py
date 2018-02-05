# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.validators import validate_comma_separated_integer_list

#Create your models here.
class GlobalData(models.Model):
	participant_id = models.IntegerField(default=0)
	unit = models.CharField(max_length=5)
	#trialsLeft = models.CommaSeparatedIntegerField(max_length=200)
	trialsLeft = models.CharField(validators=[validate_comma_separated_integer_list],max_length=200)

	def __str__(self):
		return str(self.participant_id)


class Trial(models.Model):
	participant_id = models.IntegerField(default=0)
	week = models.IntegerField(default=0)
	dates = models.CharField(validators=[validate_comma_separated_integer_list],max_length=200)
	highs = models.CharField(validators=[validate_comma_separated_integer_list],max_length=200)
	lows = models.CharField(validators=[validate_comma_separated_integer_list],max_length=200)
	colour = models.CharField(max_length=8)

	def __str__(self):
		return str(self.participant_id)



class Response(models.Model):
	participant_id = models.IntegerField(default=0)
	week = models.IntegerField(default=0)
	normal = models.IntegerField(default=0)
	confidence = models.IntegerField(default=0)

	def __str__(self):
		return str(self.participant_id)


class Participants(models.Model):
	participant_id = models.IntegerField(default=0)
	last_trial = models.IntegerField(default=0)
	condition = models.IntegerField(default=0)

	def __str__(self):
		return str(self.participant_id)