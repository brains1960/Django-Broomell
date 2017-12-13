from django import forms

class LocationForm(forms.Form):
	unit_choices = (('0', 'Celcius',), ('1', 'Fahrenheit',))
	unit = forms.ChoiceField(required=True,
									label="Select a unit of Measurement", 
									widget=forms.RadioSelect, choices=unit_choices,
									error_messages={'required':"Please Select a Unit of Measurement"})
	

	city_choices = (('0', 'Pittsburgh',), ('1', 'New York',), ('51', 'Other'))
	city = forms.ChoiceField(required=True,
									label="Please select the most appropriate city",
									choices=city_choices,
									error_messages={'required':"Please Select a City"})
	