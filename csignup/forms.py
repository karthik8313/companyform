from django import forms

class cform(forms.Form):
	company_name = forms.CharField(max_length=100)
	company_website = forms.URLField(max_length=150,initial="http://")
	job_description = forms.CharField(widget=forms.Textarea)
	key_skills = forms.CharField(max_length=30,error_messages={'required': '*'})
	location = forms.CharField(max_length=30)
	salary_range = forms.ChoiceField(choices = (('0.5 - 1.5 Lpa','0.5 - 1.5 Lpa'),
		('1.5 - 3 Lpa','1.5 - 3 Lpa'),
		('3 - 5 Lpa','3 - 5 Lpa'),
		('5 - 7 Lpa','5 - 7 Lpa'),
		('7 Lpa and above','7 Lpa and above'),
			),label="salary_range", initial='1.5 - 3 Lpa', widget=forms.Select(), required=True,error_messages={'required': '*'})
	job_type = forms.ChoiceField(choices = (('Full Time','Full Time'),('Part Time','Part Time'),('Internship','Internship'),
		),label="job_type", initial='Full Time', widget=forms.Select(), required=True,error_messages={'required': '*'})
	date_of_joining = forms.DateField(error_messages={'required': '*'})
	interview_location = forms.CharField(max_length=30,error_messages={'required': '*'})
	recruiter_email = forms.EmailField(max_length=50,error_messages={'required': '*'})
	