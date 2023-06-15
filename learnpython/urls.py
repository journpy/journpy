"""Defines URL patterns for the app journpys."""

from django.urls import path

from . import views

app_name = 'learnpython'
urlpatterns = [
	# Home page
	path('lessons', views.lessons, name='lessons'),
	# Page for a lesson
	path('lessons/<int:title_id>/', views.lesson, name='lesson')
]