from django import forms

class SurveyForm(forms.Form):
	normal_choices = (('0', 'Normal',), ('1', 'Abnormal',))
	normal = forms.ChoiceField(label="Do you think the temparatures above are 'normal' or 'abnormal'?",
								widget=forms.RadioSelect, choices=normal_choices)

	confidence_choices = (('0', 'Low',), ('1', 'Medium',), ('2', 'High',))
	confidence = forms.ChoiceField(label="Rate your confidence in your answer", 
									widget=forms.RadioSelect, choices=confidence_choices)