from django.shortcuts import render, render_to_response
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.template import RequestContext
from django.template.loader import get_template
from actstream import action
from actstream.models import user_stream, actor_stream, target_stream
from django.contrib.auth.models import User
from social_quiz.forms import *
import csv

# Create your views here. 
def profile_page(request, username):
	try:
		u = User.objects.get(username = username)
	except ObjectDoesNotExist:
		raise Http404('Requested user not found')

	try:
		us = user.objects.get(username = username)
	except ObjectDoesNotExist:
		raise Http404('Requested user not found!')

	if User.is_authenticated:
		a_user = request.user.username
		if (a_user == username):
			follow = 0
		else:
			follow = 1

	if request.POST.get('click'):
		if User.is_authenticated:
			a_user = request.user.username
		a_u = user.objects.get(username = a_user)
		f = a_u.following_set.create(
				fn_username = username
			)
		f.save()

	'''variable declarations for user table'''
	username = us.username
	first_name = us.first_name
	last_name = us.last_name
	gender = us.gender
	dob = us.dob
	native_l = us.native_l
	state = us.state
	country = us.country
	email = us.email
	phone = us.phone

	'''variable declarations for friends table'''
	friends = us.friends_set.all()

	'''variable declarations for status table'''
	status = us.status_set.all()

	'''variable declarations for questions table'''
	questions = us.questions_set.all()

	'''variable declarations for answers table'''
	answers = us.answers_set.all()

	'''variable declarations for books table'''
	books = us.books_set.all()

	'''variable declarations for sites table'''
	sites = us.sites_set.all()

	'''variable declarations for status table'''
	
	if len(status) == 0:
		length = 0
	else:
		s = us.status_set.all()
		length = len(status) - 1
		status = s[length].status_text
	
	'''variable declaration for personal actor stream'''
	personal_stream = actor_stream(us)

	form = Ask_questionForm(request.POST)
	if request.method == 'POST' and form.is_valid():
		q = us.questions_set.create(
				q_title = form.cleaned_data['q_title'],
				q_desc = form.cleaned_data['q_desc'],
			)
		q.save()
		action.send(us, verb='asked a question', action_object=q)
		return HttpResponseRedirect('/user/' + str(username) + '/')

	else:
		form = Ask_questionForm()

	variables = RequestContext(request, {
			'first_name': first_name,
			'last_name': last_name,
			'gender': gender,
			'dob': dob,
			'native_l': native_l,
			'state': state,
			'country': country,
			'email': email,
			'phone': phone,
			'friends': friends,
			'status': status,
			'questions': questions,
			'answers': answers,
			'books': books,
			'sites': sites,
			'personal_stream': personal_stream,
			'follow': follow,
		})

	return render_to_response('profile_page.html', variables)

def registration_page(request):
	template = get_template('registration_page.html')
	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			us = User.objects.create_user(
				username = form.cleaned_data['username'],
				password = form.cleaned_data['password1'],
				email = form.cleaned_data['email']
			)
			u = user(
				username = form.cleaned_data['username'],
				email = form.cleaned_data['email'],
				gender = form.cleaned_data['gender'],
				dob = form.cleaned_data['dob'],
				state = form.cleaned_data['state'],
				country = form.cleaned_data['country']
			)
			u.save()
			return HttpResponseRedirect('/login/')

	else:
		form = RegistrationForm()

	variables = RequestContext(request, {
    		'form': form,
    })

	return render_to_response('registration_page.html', variables)

def login_page(request):
	form = LoginForm(request.POST or None)    
	if request.method == 'POST' and form.is_valid():
		user = form.authenticate_user()
		login(request, user)
		return HttpResponseRedirect('/user/' + str(user.username) +'/')
	else:
		form = LoginForm()

	variables = RequestContext(request, {
    		'form': form 
    })
	return render_to_response('login_page.html', variables)

def personal_info(request):
	if User.is_authenticated:
		username = request.user.username
	else:
		username = None
	try:
		us = user.objects.get(username = username)
	except ObjectDoesNotExist:
		raise Http404('Requested user not found!')
		
	form = Personal_infoForm(request.POST)
	if request.method == 'POST' and form.is_valid():
		us.first_name = form.cleaned_data['first_name']
		us.last_name = form.cleaned_data['last_name']
		us.phone = form.cleaned_data['phone']
		us.native_l = form.cleaned_data['native_l']
		us.save()

		s = us.status_set.create(
				status_text = form.cleaned_data['status']
			)
		s.save() 
		return HttpResponseRedirect('/user/' + str(username) + '/')

	else:
		form = Personal_infoForm()


	'''variable declarations for user table'''
	gender = us.gender
	dob = us.dob
	state = us.state
	country = us.country
	email = us.email

	'''variable declaration for status table'''
	s = us.status_set.all()
	length = len(status) - 1
	status = s[length].status_text

	variables = RequestContext(request, {
			'form': form,
			'gender': gender,
			'dob': dob,
			'state': state,
			'country': country,
			'email': email,
			'status': status,
			'length': length,
		})

	return render_to_response('personal_info.html', variables)

def education_info(request):
	if User.is_authenticated:
		username = request.user.username

	else:
		username = None

	us = user.objects.get(username = username)
	education = us.education_set.all()

	form = Education_infoForm(request.POST)
	if request.method == 'POST' and form.is_valid():
		e = us.education_set.create(
				institute = form.cleaned_data['institute'],
				e_type = form.cleaned_data['e_type'],
				grad_year = form.cleaned_data['grad_year'],
			)
		e.save()
		return HttpResponseRedirect('/user/' + str(username) + '/')

	else:
		form = Education_infoForm()

	variables = RequestContext(request, {
			'form': form,
			'education': education,
		})

	return render_to_response('education_info.html', variables)

def job_info(request):
	if User.is_authenticated:
		username = request.user.username

	else:
		username = None

	us = user.objects.get(username = username)
	jobs = us.job_set.all()

	form = Job_infoForm(request.POST)
	if request.method == 'POST' and form.is_valid():
		j = us.job_set.create(
				company = form.cleaned_data['company'],
				designation = form.cleaned_data['designation'],
			)
		j.save()
		return HttpResponseRedirect('/user/' + str(username) + '/')

	else:
		form = Job_infoForm()

	variables = RequestContext(request, {
			'form': form,
			'jobs': jobs,
		})
			
	return render_to_response('job_info.html', variables)

def quiz_info(request):
	if User.is_authenticated:
		username = request.user.username

	else:
		username = None

	us = user.objects.get(username = username)
	quizzes = us.quizzes_set.all()

	form = Quiz_infoForm(request.POST)
	if request.method == 'POST' and form.is_valid():
		q = us.quizzes_set.create(			
				quiz_name = form.cleaned_data['quiz_name'],
				position = form.cleaned_data['position'],
			)
		q.save()
		return HttpResponseRedirect('/user/' + str(username) + '/')

	else:
		form = Quiz_infoForm()

	variables = RequestContext(request, {
			'form': form,
			'quizzes': quizzes,
		})
			
	return render_to_response('quiz_info.html', variables)

def books_info(request):
	if User.is_authenticated:
		username = request.user.username

	else:
		username = None

	us = user.objects.get(username = username)
	books = us.books_set.all()

	form = Books_infoForm(request.POST)
	if request.method == 'POST' and form.is_valid():
		b = us.books_set.create(			
				b_name = form.cleaned_data['b_name'],
				author = form.cleaned_data['author'],
			)
		b.save()
		return HttpResponseRedirect('/user/' + str(username) + '/')

	else:
		form = Books_infoForm()

	variables = RequestContext(request, {
			'form': form,
			'books': books,
		})
			
	return render_to_response('books_info.html', variables)

def sites_info(request):
	if User.is_authenticated:
		username = request.user.username

	else:
		username = None

	us = user.objects.get(username = username)
	sites = us.sites_set.all()

	form = Sites_infoForm(request.POST)
	if request.method == 'POST' and form.is_valid():
		s = us.sites_set.create(				
				s_name = form.cleaned_data['s_name'],
				s_url = form.cleaned_data['s_url'],
			)
		s.save()
		return HttpResponseRedirect('/user/' + str(username) + '/')

	else:
		form = Sites_infoForm()

	variables = RequestContext(request, {
			'form': form,
			'sites': sites,
		})
			
	return render_to_response('sites_info.html', variables)

def ask_question(request):
	if User.is_authenticated:
		username = request.user.username

	else:
		username = None

	us = user.objects.get(username = username)

	form = Ask_questionForm(request.POST)
	if request.method == 'POST' and form.is_valid():
		q = us.questions_set.create(
				q_title = form.cleaned_data['q_title'],
				q_desc = form.cleaned_data['q_desc'],
			)
		q.save()
		action.send(us, verb='asked a question', action_object=q)
		return HttpResponseRedirect('/user/' + str(username) + '/')

	else:
		form = Ask_questionForm()

	variables = RequestContext(request, {
			'form': form,
		})
	return render_to_response('askquestion.html', variables)

def news_feeds(request):
	if User.is_authenticated:
		username = request.user.username

	else:
		username = None

	us = User.objects.get(username = username)

	feed_stream = user_stream(us, with_user_activity=True)

	variables = RequestContext(request, {
			'feed_stream': feed_stream,
		})

	return render_to_response('home.html', variables)

def logout_page(request):
	logout(request)
	HttpResponseRedirect('/login/')





