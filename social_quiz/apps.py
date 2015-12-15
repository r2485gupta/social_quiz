from django.apps import AppConfig
from actstream import registry
from django.contrib.auth.models import User

class MyAppConfig(AppConfig):
    name = 'social_quiz'

    def ready(self):
        registry.register(User,
            self.get_model('user'), 
        	self.get_model('friends'),
        	self.get_model('status'),
        	self.get_model('questions'),
        	self.get_model('answers'),
        	self.get_model('education'),
        	self.get_model('job'),
        	self.get_model('quizzes'),
        	self.get_model('books'),
        	self.get_model('sites'),
        	)

# myapp/__init__.py
default_app_config = 'myapp.apps.MyAppConfig'