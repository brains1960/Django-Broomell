# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django import forms
from .forms import SurveyForm
from .models import GlobalData, Trial, Response, Participants


# Create your views here.


def index(request):

	colours = ["red", "orange","yellow","green","blue", "indigo","violet"]
	if (request.method == 'POST'):

		global_data = GlobalData.object.all()
		trial_data = Trial.objects.all()
		

		form = SurveyForm(request.POST)

		if form.is_valid():


			render(request,'trials.html', {'form' : form, 'page_name' : '- Trials'})

	else:

		form = SurveyForm()
		# Render the HTML template index.html with the data in the context variable
	 	return render(request,'trials.html', {'form' : form, 'page_name' : '- Trials'})
   