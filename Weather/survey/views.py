# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django import forms
from .forms import SurveyForm


# Create your views here.


def index(request):

	if (request.method == 'POST'):

		form = SurveyForm(request.POST)

		if form.is_valid():

			render(request,'trials.html', {'form' : form, 'page_name' : '- Trials'})

	else:

		form = SurveyForm()
		# Render the HTML template index.html with the data in the context variable
	 	return render(request,'trials.html', {'form' : form, 'page_name' : '- Trials'})
   