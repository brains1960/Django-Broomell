from django import forms

class ConsentForm(forms.Form):
	ofAge = forms.BooleanField(required=True, 
								label="I am age 18 or older",
								error_messages={'required':"You must be 18 or Over to Participate in the experiment"})

	hasRead = forms.BooleanField(required=True, 
								label="I have read and understand the information above.",
								error_messages={'required':"Please read the instruction and answer all questions"})

	willParticipate = forms.BooleanField(required=True, 
								label="I want to participate in this research and continue with the survey.",
								error_messages={'required':"You must consent to continue with the survey. Please exit the survey if you do not consent"})
