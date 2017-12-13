# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django import forms
from .forms import LocationForm

# Create your views here.

def index(request):

	if (request.method == 'POST'):

		form = LocationForm(request.POST)

		if form.is_valid():
			return HttpResponseRedirect('/survey')

	else:

		form = LocationForm()
		return render(request,'location.html', {'form' : form, 'page_name' : '- Location'})