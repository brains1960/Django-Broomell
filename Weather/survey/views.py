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

			colour = colours[participant.last_trial // 8]

			url = '/survey/'+str(participant_id)

			if participant.condition == 1:
				first_condition_text = "A malfunctioning machine has an identically shaped distribution of internal temperatures as a \
				 properly function machine, but produces daily temperature readings that are on average 10 degrees Fahrenheit warmer\
				  than a properly functioning machine."

				second_condition_text = "From a week’s worth of data, they need to decide if the machine is running properly (with a \
				mean temperature of 63 degrees Fahrenheit and a standard deviation of 8 degrees, or if the machine has malfunctioned, \
				and is running with an average that is 10 degrees warmer than normal."

			elif participant.condition == 2:
				first_condition_text = "A malfunctioning machine looks the same as a properly function machine, but produces daily\
				 temperature readings that are on average 10 degrees Fahrenheit warmer than a properly functioning machine. This \
				 figure shows 1000 daily temperatures recorded for a malfunctioning injection molding machine."

				second_condition_text = "From a week’s worth of data, they need to decide if the machine is running properly (with \
				a mean temperature of 63 degrees Fahrenheit and a standard deviation of 8 degrees, or if the machine has \
				  malfunctioned, and is running with an average that is 10 degrees warmer than normal. This figure shows 1000 \
				  daily temperatures recorded for a properly function machine next to 1000 daily temperatures recorded for a \
				  malfunctioning injection molding machine."

			return HttpResponseRedirect('/sudkvkg/%s' % (str(participant_id)))
	else:

		trial_data = Trial.objects.all()

		try:
			global_data = GlobalData.objects.get(participant_id=participant_id)
			new_participant = Participants.objects.get(participant_id=participant_id)
			condition = new_participant.condition

		except ObjectDoesNotExist:
	
			new_participant = Participants()

			new_participant.participant_id = participant_id
			new_participant.last_trial = 1
			new_participant.condition = randint(1,2)
			new_participant.save()

		colour = colours[new_participant.last_trial // 8]

		if new_participant.condition == 1:
			first_condition_text = "A malfunctioning machine has an identically shaped distribution of internal temperatures as a \
			 properly function machine, but produces daily temperature readings that are on average 10 degrees Fahrenheit warmer\
			  than a properly functioning machine."

			second_condition_text = "From a week’s worth of data, they need to decide if the machine is running properly (with a \
			mean temperature of 63 degrees Fahrenheit and a standard deviation of 8 degrees, or if the machine has malfunctioned, \
			and is running with an average that is 10 degrees warmer than normal."

		elif new_participant.condition == 2:
			first_condition_text = "A malfunctioning machine looks the same as a properly function machine, but produces daily\
			 temperature readings that are on average 10 degrees Fahrenheit warmer than a properly functioning machine. This \
			 figure shows 1000 daily temperatures recorded for a malfunctioning injection molding machine."

			second_condition_text = "From a week’s worth of data, they need to decide if the machine is running properly (with \
			a mean temperature of 63 degrees Fahrenheit and a standard deviation of 8 degrees, or if the machine has \
			  malfunctioned, and is running with an average that is 10 degrees warmer than normal. This figure shows 1000 \
			  daily temperatures recorded for a properly function machine next to 1000 daily temperatures recorded for a \
			  malfunctioning injection molding machine."

		form = SurveyForm()
		# Render the HTML template index.html with the data in the context variable
		return render(request,'instructions.html', {'page_name' : participant_id, 'colour' : colour, 
						'condition_text_1' : first_condition_text, 'condition_text_2' : second_condition_text})
   
def example(request, participant_id):

	participant = Participants.objects.get(participant_id=participant_id)
	global_data = GlobalData.objects.get(participant_id=participant_id)

	if global_data.unit == "C":
		example1 = "18"
		example2 = "17"
		example3 = "16"
		example4 = "20"
		example5 = "12"
		example6 = "21"
		example7 = "23"

	elif global_data.unit == "F":
		example1 = "64"
		example2 = "62"
		example3 = "61"
		example4 = "68"
		example5 = "54"
		example6 = "69"
		example7 = "74"

	if (request.method == 'POST'):

		return render(request, 'example.html', {'page_name' : participant_id, 'colour' : colour, 'example1' : example1,
												'example2' : example2, 'example3' : example3, 'example4' : example4,
												'example5' : example5, 'example6' : example6, 'example7' : example7})

	else: 


		if participant.condition == 1:
			condition_img = "<img src='../static/img/condition1_example.jpg'>"

		elif participant.condition == 2:
			condition_img = "<img src='../static/img/condition1_example.jpg'>"

		return render(request, 'example.html', {'page_name' : participant_id, 'colour' : colour, 'example1' : example1,
												'example2' : example2, 'example3' : example3, 'example4' : example4,
												'example5' : example5, 'example6' : example6, 'example7' : example7})