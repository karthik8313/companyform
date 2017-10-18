from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from .forms import cform
from django.core.mail import send_mail,EmailMessage

def get_details(request):
	form = cform(request.POST or None)
	if form.is_valid():
		company_name = form.cleaned_data['company_name']
		company_website = form.cleaned_data['company_website']
		job_description = form.cleaned_data['job_description']
		key_skills = form.cleaned_data['key_skills']
		location = form.cleaned_data['location']
		salary_range = form.cleaned_data['salary_range']
		job_type = form.cleaned_data['job_type']
		date_of_joining = form.cleaned_data['date_of_joining']
		interview_location = form.cleaned_data['interview_location']
		recruiter_email = form.cleaned_data['recruiter_email']
		
	return render(request, 'form.html', {'form': form})

def mailsend(request):
	company_name = request.GET.get("company_name")
	job_description = request.GET.get("job_description")
	recruiter_email = request.GET.get("recruiter_email")
	send_mail(company_name, job_description, recruiter_email,['karthik.m8313@gmail.com'])
	email = EmailMessage('Thank You-DevU', 'Thank You For Posting Job on DevU',to=[recruiter_email])
	email.send()
	return HttpResponseRedirect("/form")
