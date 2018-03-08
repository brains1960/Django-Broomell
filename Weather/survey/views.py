# -*- coding: utf-8 -*-
from __future__ import unicode_literals


import csv, os
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django import forms
from .forms import SurveyForm, ExampleForm
from .models import GlobalData, Trial, Response, Participants
from django.core.exceptions import ObjectDoesNotExist

from random import *

# Create your views here.


def index(request, participant_id):

	colours = ["red", "orange","yellow","green","blue", "indigo","violet"]
	if (request.method == 'POST'):

		return HttpResponseRedirect('/survey/%s/example' % (str(participant_id)))
			# return HttpResponseRedirect('/sudkvkg/%s' % (str(participant_id)))
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

		if global_data.unit == "0":
			temperature = 17
			unit = "Celcius"
			deviation = 5

		elif global_data.unit == "1":
			temperature = 63
			unit = "Fahrenheit"
			deviation = 8

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
			a mean temperature of " + str(temperature) +" degrees " + str(unit) +" and a standard deviation of 8 degrees, or if the machine has \
			  malfunctioned, and is running with an average that is 10 degrees warmer than normal. This figure shows 1000 \
			  daily temperatures recorded for a properly function machine next to 1000 daily temperatures recorded for a \
			  malfunctioning injection molding machine."

		# Render the HTML template index.html with the data in the context variable
		return render(request,'instructions.html', {'page_name' : participant_id, 'colour' : colour, 
						'condition_text_1' : first_condition_text, 'condition_text_2' : second_condition_text,
						 'unit' : unit, 'temperature':temperature, 'deviation' : deviation})

   
def example(request, participant_id):

	participant = Participants.objects.get(participant_id=participant_id)
	global_data = GlobalData.objects.get(participant_id=participant_id)
	form1 = SurveyForm()
	form2 = ExampleForm()

	if global_data.unit == "0":
		example1 = "18"
		example2 = "17"
		example3 = "16"
		example4 = "20"
		example5 = "12"
		example6 = "21"
		example7 = "23"
		number = 6.5
		unit = "Celcius"

	elif global_data.unit == "1":
		example1 = "64"
		example2 = "62"
		example3 = "61"
		example4 = "68"
		example5 = "54"
		example6 = "69"
		example7 = "74"
		number = 10
		unit = "Fahrenheit"


	if (request.method == 'POST'):

		return HttpResponseRedirect('/survey/%s/trial' % (str(participant_id)))

	else:
		if participant.condition == 1:
			condition_img = "<img src='../static/img/condition1_example.jpg'>"

		elif participant.condition == 2:
			condition_img = "<img src='../static/img/condition1_example.jpg'>"

		return render(request, 'example.html', {'page_name' : participant_id, 'colour' : "gray", 'example1' : example1,
												'example2' : example2, 'example3' : example3, 'example4' : example4,
												'example5' : example5, 'example6' : example6, 'example7' : example7,
												"number_on_average_in_units" : number, 'unit' : unit, 'form1': form1,
													'form2': form2})

def makeCSV(datarow):
	with open('results.csv', 'w+') as resultFile:
		wr = csv.writer(resultFile, dialect='excel')
		wr.writerow(['ID', 'Week', 'Machine', 'confidence'])
		wr.writerow(datarow)

def trial(request, participant_id):

	THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))

	participant = Participants.objects.get(participant_id=participant_id)
	global_data = GlobalData.objects.get(participant_id=participant_id)

	file = os.path.join(THIS_FOLDER, 'data.csv')

	data = list(csv.reader(open(file)))

	response_data = Response()
	trial_data = Trial()

	if (request.method == 'POST'):

		form = SurveyForm(request.POST)

		last_trial_data = Trial.objects.filter(participant_id=participant_id).order_by('-id')[0]

		response_data.participant_id = participant_id
		response_data.week = last_trial_data.week

		if form.is_valid():

			response_data.machine = form.cleaned_data['machine']
			response_data.confidence = form.cleaned_data['confidence']
			
			response_data.save()


		if (int(participant.last_trial) == 52):

			return HttpResponseRedirect('/')

		else:

			#Converting between string comma seperated list and actual lists
			# if len(participant.trialsLeft) <= 2:
			# 	trialsLeft = []
			# else:
			trialsLeft = participant.trialsLeft[1:-1]
			trialsLeft = [int(x) for x in trialsLeft.split(',')]

			rowNum = int(choice(trialsLeft))

			datarow = [response_data.participant_id, rowNum, response_data.machine,response_data.confidence]
			# makeCSV([response_data.participant_id, response_data.week,response_data.machine,response_data.confidence])
			with open(os.path.join(THIS_FOLDER, 'results.csv'), 'a') as resultFile:
				wr = csv.writer(resultFile, dialect='excel')
				wr.writerow(datarow)

			trialsPassed = participant.trialsPassed
			if len(trialsPassed) <= 2:
				trialsPassed = []
			else:
				trialsPassed = trialsPassed[1:-1]
				trialsPassed = [int(x) for x in trialsPassed.split(',')]
			trialsPassed.append(rowNum)
			participant.trialsPassed = trialsPassed
			
		
			trialsLeft.remove(rowNum)
			participant.trialsLeft = trialsLeft


			temps = data[rowNum]
			trial_data.temps = temps
			trial_data.week = rowNum

			if (global_data.unit == '0'):
				temps = [int((int(x)-32)*(5.0/9)) for x in temps]

			if (participant.condition == '2'):
				temps = [int(x) + 10 for x in temps]

			participant.last_trial = int(len(trialsPassed))

			participant.save()
			trial_data.save()

			trialsNum = participant.last_trial

			colours = ["red", "orange","yellow","green","blue", "indigo","violet"]


			return render(request, 'trials.html', {

			'page_name' : participant_id,  
			'temp1' : temps[0],
			'temp2' : temps[1],
			'temp3' : temps[2], 
			'temp4' : temps[3],
			'temp5' : temps[4], 
			'temp6' : temps[5], 
			'temp7' : temps[6],
			"colour": colours[trialsNum//8],
			"page_name":"Trials",
			"current_trial" : trialsNum,
			'form1' : SurveyForm()

		})

	#GET Method
	elif (request.method == 'GET'):
		#Getting Files
		file = os.path.join(THIS_FOLDER, 'data.csv')

		#Begin Results file
		with open(os.path.join(THIS_FOLDER, 'results.csv'), 'r') as resultFile:
			rd = csv.reader(resultFile, dialect='excel')

			with open(os.path.join(THIS_FOLDER, 'results.csv'), 'a') as resultFile:
				wr = csv.writer(resultFile, dialect='excel')
				if (len(list(rd)) == 0):
					wr.writerow(['Id', 'Week', 'Machine', 'confidence'])

		#Picking Condition
		participant.condition = choice([1,2])
		
		#Global Data stuff
		unit = global_data.unit
		data = list(csv.reader(open(file)))


		#Participant Stuff
		trialsLeft = [int(x) for x in range(len(data))]
		participant.trialsLeft = trialsLeft
		participant.last_trial = 52-len(trialsLeft)
		
		rowNum = choice(trialsLeft)

		#Converting between String comma seperated lists and lists
		# trialsPassed = participant.trialsPassed
		trialsPassed = []
		trialsPassed.append(rowNum)
		participant.trialsPassed = trialsPassed

		trialsLeft.remove(rowNum)
		participant.trialsLeft = trialsLeft

		#Trial Stuff
		trialsNum = participant.last_trial + 1
		trial_data.participant_id = participant_id
		trial_data.week = rowNum
		temps = data[rowNum]
		trial_data.temps = temps

		if (unit == '0'):
			temps = [int((int(x)-32)*(5.0/9)) for x in temps]

		if (participant.condition == '2'):
			temps = [int(x) + 10 for x in temps]

		

		colours = ["red", "orange","yellow","green","blue", "indigo","violet"]

		#saves
		participant.save()
		trial_data.save()


		return render(request, 'trials.html', {

			'page_name' : participant_id, 
			'colour' : "gray", 
			'temp1' : temps[0],
			'temp2' : temps[1],
			'temp3' : temps[2], 
			'temp4' : temps[3],
			'temp5' : temps[4], 
			'temp6' : temps[5], 
			'temp7' : temps[6],
			"colour": colours[trialsNum//8],
			"page_name":"Trials",
			"current_trial" : trialsNum,
			'form1' : SurveyForm()

		})