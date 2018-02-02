# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django import forms
from .forms import ConsentForm


# Create your views here.


def index(request):

	if (request.method == 'POST'):

		form = ConsentForm(request.POST)

		if form.is_valid():
			return HttpResponseRedirect('/location')

	else:

		form = ConsentForm()
		# Render the HTML template index.html with the data in the context variable
		return render(request,'informed_consent.html', {'form' : form, 'page_name' : '- Consent'})
   
