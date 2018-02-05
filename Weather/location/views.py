# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django import forms
from .forms import LocationForm
from survey.models import GlobalData, Trial, Response, Participants

from random import *

# Create your views here.

def index(request):

	if (request.method == 'POST'):

		form = LocationForm(request.POST)

		if form.is_valid():

			global_data = GlobalData.objects.all()

			new_g_data = GlobalData()

			new_g_data.participant_id = randint(1,10000)
			new_g_data.unit = form.cleaned_data['unit']
			trials_left = range(1,53)
			new_g_data.trials_left = ",".join([str(x) for x in trials_left])

			new_g_data.save()

			return HttpResponseRedirect('/survey/'+str(new_g_data.participant_id))

	else:

		form = LocationForm()
		return render(request,'location.html', {'form' : form, 'page_name' : '- Location'})