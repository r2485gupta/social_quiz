from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from social_quiz.models import user
from django.core.exceptions import ObjectDoesNotExist
import re

class RegistrationForm(forms.Form):
	username = forms.CharField(label = 'Username',
			max_length=30,
			widget=forms.TextInput(attrs={'class': 'form-control'})
		)
	email = forms.EmailField(label = 'Email',
			widget=forms.TextInput(attrs={'placeholder': 'xyz@company.com', 'class': 'form-control'})
		)
	password1 = forms.CharField(
			label = 'Password',
			widget = forms.PasswordInput(attrs={'class': 'form-control'}),
		)
	password2 = forms.CharField(
			label = 'Password(again)',
			widget = forms.PasswordInput(attrs={'class': 'form-control'}),
		)

	GENDER = (
			('-----', '-----'),
			('Gentleman', 'Gentleman'),
			('Lady', 'Lady'),
		)

	gender = forms.ChoiceField(label = 'Sex',
			choices = GENDER,
			widget = forms.Select(attrs={'class': 'form-control'})
		)
	dob = forms.DateField(label='Date of Birth',
			widget = forms.TextInput(attrs={'placeholder': 'YYYY-MM-DD', 'class': 'form-control'})
		)
	state = forms.CharField(label='State',
			widget = forms.TextInput(attrs={'class': 'form-control'})
		)
	country = forms.CharField(label='Country',
			widget = forms.TextInput(attrs={'class': 'form-control'})
		)

	def clean_username(self):
		username = self.cleaned_data['username']
		if not re.search(r'^\w+$', username):
		 	raise forms.ValidationError('Username can contain only alphanumeric characters and underscore')

		try:
		 	User.objects.get(username = username)
		 	user.objects.get(username = username)
		except ObjectDoesNotExist:
		 	return username

		raise forms.ValidationError('Username already taken!')

	def clean_password(self):
		if 'password1' in self.cleaned_data:
			password1 = self.cleaned_data['password1']
			password2 = self.cleaned_data['password2']

			if password1 == password2:
				return password2	
		raise forms.ValidationError('Passwords do not match!')

class LoginForm(forms.Form):
	email = forms.CharField(
		label='Email',
		widget=forms.TextInput(attrs={'placeholder': 'Email', 'class': 'form-control'})
	)
	password = forms.CharField(
		label='Password', 
		widget = forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'form-control'}),
	)

	def clean(self):
		user = self.authenticate_via_email()
		if not user:
			raise forms.ValidationError("Sorry, that login was invalid. Please try again.")
		else:
			self.user = user
		return self.cleaned_data

	def authenticate_user(self):
		return authenticate(
			username=self.user.username,
			password=self.cleaned_data['password'])

	def authenticate_via_email(self):

		email = self.cleaned_data['email']
		if email:
			try:
				user = User.objects.get(email__iexact=email)
				if user.check_password(self.cleaned_data['password']):
					return user
			except ObjectDoesNotExist:
				pass
		return None

class Personal_infoForm(forms.Form):
	phone = forms.CharField(label='Phone')
	first_name = forms.CharField(label='First Name')
	last_name = forms.CharField(label='Last Name')
	native_l = forms.CharField(label='Native Language')
	status = forms.CharField(label='Status')

class Education_infoForm(forms.Form):
	institute = forms.CharField(label='Institute',
			widget = forms.TextInput(attrs={'class': 'form-control'}),
		)

	E_TYPE = (
			('-----', '-----'),
			('Primary School', 'Primary School'),
			('High School', 'High School'),
			('College', 'College'),
			('Under Graduate Program', 'Under Graduate Course'),
			('Graduate Program', 'Graduate Course'),
			('Advanced Studies', 'Advanced Studies'),
		)

	e_type = forms.ChoiceField(label='Education Type',
			choices=E_TYPE,
			widget = forms.Select(attrs={'class': 'form-control'}),
		)
	grad_year = forms.CharField(label='Batch of',
			widget = forms.TextInput(attrs={'class': 'form-control'}),
		)

class Job_infoForm(forms.Form):
	company = forms.CharField(label='Company',
			widget = forms.TextInput(attrs={'class': 'form-control'}),
		)
	designation = forms.CharField(label='Designation',
			widget = forms.TextInput(attrs={'class': 'form-control'}),
		)

class Quiz_infoForm(forms.Form):
	quiz_name = forms.CharField(label='Quiz Name',
			widget = forms.TextInput(attrs={'class': 'form-control'}),
		)
	position = forms.CharField(label='Achievement',
			widget = forms.TextInput(attrs={'class': 'form-control'}),
		)

class Books_infoForm(forms.Form):
	b_name = forms.CharField(label='Title',
			widget = forms.TextInput(attrs={'class': 'form-control'}),
		)
	author = forms.CharField(label='Author',
			widget = forms.TextInput(attrs={'class': 'form-control'}),
		)

class Sites_infoForm(forms.Form):
	s_name = forms.CharField(label='Site Name',
			widget = forms.TextInput(attrs={'class': 'form-control'}),
		)
	s_url = forms.CharField(label='URL',
			widget = forms.TextInput(attrs={'class': 'form-control'}),
		)

class Ask_questionForm(forms.Form):
	q_title = forms.CharField(label='Question Title',
			widget = forms.TextInput(attrs={'class': 'form-control'}),
		)
	q_desc = forms.CharField(label='Description',
			widget = forms.TextInput(attrs={'class': 'form-control'}),
		)

class Answer_Form(forms.Form):
	a_text = forms.CharField(label='',
			widget = forms.TextInput(attrs={'placeholder': 'write an answer'}),
		)




