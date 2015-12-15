"""social URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from social import settings
from django.conf.urls import include, url
from django.contrib import admin
from social_quiz.views import *
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^activity/', include('actstream.urls')),
    url(r'^user/(\w+)/', profile_page),
    url(r'^home/', news_feeds),
    url(r'^ask/', ask_question),
    url(r'^register/', registration_page),
    url(r'^login/', login_page),
    url(r'^logout/', logout_page),
    url(r'^profile/personal/', personal_info),
    url(r'^profile/education/', education_info),
    url(r'^profile/jobs/', job_info),
    url(r'^profile/quizzes/', quiz_info),
    url(r'^profile/books/', books_info),
    url(r'^profile/sites/', sites_info),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
