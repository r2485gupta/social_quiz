from django.db import models
from social import settings

# Create your models here.
class user(models.Model):
	username = models.CharField(max_length=30) 
	phone = models.CharField(max_length=12, blank=True)
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	email = models.EmailField()
	gender = models.CharField(max_length=10)
	dob = models.DateField(default='1995-05-21')
	state = models.CharField(max_length=20)
	country = models.CharField(max_length=20)
	native_l = models.CharField(max_length=20)
	profile_pic = models.ImageField(upload_to='photos', default='settings.MEDIA_ROOT/photos/default_profile.jpg')

	def __str__(self):
		return self.first_name

class friends(models.Model):
	username = models.ForeignKey(user)
	f_username = models.CharField(max_length=30)

class status(models.Model):
	username = models.ForeignKey(user)
	status_text = models.CharField(max_length=150)

class questions(models.Model):
	username = models.ForeignKey(user)
	q_title = models.CharField(max_length=500)
	q_desc = models.CharField(max_length=500)

	def __str__(self):        
   		return self.q_title

class answers(models.Model):
	username = models.ForeignKey(user)
	q_id = models.ForeignKey(questions)
	a_text = models.CharField(max_length=1000)

class followers(models.Model):
	username = models.ForeignKey(user)
	fl_username = models.CharField(max_length=30)

class following(models.Model):
	username = models.ForeignKey(user)
	fn_username = models.CharField(max_length=30)

class education(models.Model):
	username = models.ForeignKey(user)
	institute = models.CharField(max_length=30)
	e_type = models.CharField(max_length=50)
	grad_year = models.CharField(max_length=4)

class job(models.Model):
	username = models.ForeignKey(user)
	company = models.CharField(max_length=30)
	designation = models.CharField(max_length=30)

class quizzes(models.Model):
	username = models.ForeignKey(user)
	quiz_name = models.CharField(max_length=30)
	position = models.CharField(max_length=20, default="Participation")

class books(models.Model):
	username = models.ForeignKey(user)
	b_name = models.CharField(max_length=30)
	author = models.CharField(max_length=30)

class sites(models.Model):
	username = models.ForeignKey(user)
	s_name = models.CharField(max_length=30)
	s_url = models.URLField()
