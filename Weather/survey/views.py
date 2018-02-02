# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django import forms
from .forms import SurveyForm
from .models import GlobalData, Trial, Response, Participants
from django.core.exceptions import ObjectDoesNotExist

from random import *

# Create your views here.


def index(request, participant_id):

	colours = ["red", "orange","yellow","green","blue", "indigo","violet"]
	if (request.method == 'POST'):

		form = SurveyForm(request.POST)

		if form.is_valid():

			participant = Participants.objects.get(participant_id=participant_id)
			participant.last_trial += 1
			participant.save()

			global_data = GlobalData.objects.get(participant_id=participant_id)
			week = choice(global_data.trials_left)
			global_data.trials_left.remove(week)
			global_data.save()

			new_response = Response()
			new_response.participant_id = participant_id
			new_response.confidence = form.cleaned_data['confidence']
			new_response.normal = form.cleaned_data['normal']
			new_response.week = week
			new_response.save()

			colour = colours[new_participant.last_trial/8]

			url = '/survey/'+str(participant_id)

			return HttpResponseRedirect('/sudkvkg/%s' % (str(participant_id)))
	else:

		trial_data = Trial.objects.all()

		try:
			global_data = GlobalData.objects.get(participant_id=participant_id)
			new_participant = Participants.objects.get(participant_id=participant_id)

		except ObjectDoesNotExist:
	
			new_participant = Participants()

			new_participant.participant_id = participant_id
			new_participant.last_trial = 1
			new_participant.save()

		colour = colours[new_participant.last_trial/8]

		form = SurveyForm()
		# Render the HTML template index.html with the data in the context variable
		return render(request,'trials.html', {'form' : form, 'page_name' : participant_id, 'colour' : colour})
   