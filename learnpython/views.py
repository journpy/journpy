from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import Http404
from .models import Title, Body


@login_required
def lessons(request):
	"""Home page for learnpython app."""
	titles = Title.objects.order_by('date_added')
	context = {'titles': titles}
	return render(request, 'learnpython/lessons.html', context)


@login_required
def lesson(request, title_id):
	"""Display an entire lesson."""
	title = get_object_or_404(Title, id=title_id)
	bodies = title.body_set.order_by('-date_added')
	context = {'title': title, 'bodies': bodies}
	return render(request, 'learnpython/lesson.html', context)
