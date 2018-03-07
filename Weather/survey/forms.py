from django import forms

class SurveyForm(forms.Form):
	machine_choices = (('0', 'A properly functioning machine',), ('1', 'A malfunctioning machine',))
	machine = forms.ChoiceField(label="These daily temperatures readings were generated by:",
								widget=forms.RadioSelect, choices=machine_choices)

	confidence_choices = (('0', 'Low',), ('1', 'Medium',), ('2', 'High',))
	confidence = forms.ChoiceField(label="Rate your confidence in your response", 
									widget=forms.RadioSelect, choices=confidence_choices)

class ExampleForm(forms.Form):
	performance_est = forms.CharField(max_length=2, required=True,
             label="We would like for you to tell us how well you\
	 													think can perform this task. Out of the 52 trials, how many\
									times do you think you can correctly identify which machine generated this data?")