from django import forms

class LocationForm(forms.Form):
	unit_choices = (('0', 'Celcius',), ('1', 'Fahrenheit',))
	unit = forms.ChoiceField(required=True,
									label="What type of unit of temperature would you like to work with?", 
									widget=forms.RadioSelect, choices=unit_choices,
									error_messages={'required':"Please Select a Unit of Measurement"})
	
	