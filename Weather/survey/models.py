# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
# class GlobalData(models.Model):
# 	city = models.IntegerField(default=0)
# 	unit = models.CharField(max_length=5)
# 	# trialsLeft = models.CharField(max_length=52, validators=[validate_comma_separated_integer_list])
# 	# colours = models.CharField(max_length=7, validators=[validate_comma_separated_integer_list])
# 	trialsLeft = models.CommaSeparatedIntegerField(max_length=200)
# 	# colours = Cha

# class Colour(models.Model):
# 	name = models.ForeignKey()

# class Trial(models.Model):
# 	week = models.IntegerField(default=0)
# 	dates = models.CharField(max_length=7, validators=[validate_comma_separated_integer_list])
# 	highs = models.CommaSeparatedIntegerField(max_length=200)
# 	lows = models.CommaSeparatedIntegerField(max_length=200)
# 	colour = models.CharField(max_length=8)



# class Response(models.Model):
# 	week = models.IntegerField(default=0)
# 	normal = models.IntegerField(default=0)
# 	confidence = models.IntegerField(default=0)