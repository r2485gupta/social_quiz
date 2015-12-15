# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='answers',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('a_text', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='books',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('b_name', models.CharField(max_length=30)),
                ('author', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='education',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('institute', models.CharField(max_length=30)),
                ('e_type', models.CharField(max_length=50)),
                ('grad_year', models.CharField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='followers',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('fl_username', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='following',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('fn_username', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='friends',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('f_username', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='job',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('company', models.CharField(max_length=30)),
                ('designation', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='questions',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('q_title', models.CharField(max_length=500)),
                ('q_desc', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='quizzes',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('quiz_name', models.CharField(max_length=30)),
                ('position', models.CharField(default='Participation', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='sites',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('s_name', models.CharField(max_length=30)),
                ('s_url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='status',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('status_text', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('phone', models.CharField(blank=True, max_length=12)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('gender', models.CharField(max_length=10)),
                ('dob', models.DateField(default='1995-05-21')),
                ('state', models.CharField(max_length=20)),
                ('country', models.CharField(max_length=20)),
                ('native_l', models.CharField(max_length=20)),
                ('profile_pic', models.ImageField(upload_to='photos', default='settings.MEDIA_ROOT/photos/default_profile.jpg')),
            ],
        ),
        migrations.AddField(
            model_name='status',
            name='username',
            field=models.ForeignKey(to='social_quiz.user'),
        ),
        migrations.AddField(
            model_name='sites',
            name='username',
            field=models.ForeignKey(to='social_quiz.user'),
        ),
        migrations.AddField(
            model_name='quizzes',
            name='username',
            field=models.ForeignKey(to='social_quiz.user'),
        ),
        migrations.AddField(
            model_name='questions',
            name='username',
            field=models.ForeignKey(to='social_quiz.user'),
        ),
        migrations.AddField(
            model_name='job',
            name='username',
            field=models.ForeignKey(to='social_quiz.user'),
        ),
        migrations.AddField(
            model_name='friends',
            name='username',
            field=models.ForeignKey(to='social_quiz.user'),
        ),
        migrations.AddField(
            model_name='following',
            name='username',
            field=models.ForeignKey(to='social_quiz.user'),
        ),
        migrations.AddField(
            model_name='followers',
            name='username',
            field=models.ForeignKey(to='social_quiz.user'),
        ),
        migrations.AddField(
            model_name='education',
            name='username',
            field=models.ForeignKey(to='social_quiz.user'),
        ),
        migrations.AddField(
            model_name='books',
            name='username',
            field=models.ForeignKey(to='social_quiz.user'),
        ),
        migrations.AddField(
            model_name='answers',
            name='q_id',
            field=models.ForeignKey(to='social_quiz.questions'),
        ),
        migrations.AddField(
            model_name='answers',
            name='username',
            field=models.ForeignKey(to='social_quiz.user'),
        ),
    ]
