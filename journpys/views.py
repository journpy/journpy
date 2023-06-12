from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import Http404
from .models import Topic, Entry
from .forms import TopicForm, EntryForm


def index(request):
	"""Home page for journpy app."""
	return render(request, 'journpys/index.html')


# Use the @login_required decorator to ensure that users are logged in before 
# they access the topics page
@login_required
def topics(request):
	"""Show topics in JournPy."""
	topics = Topic.objects.filter(writer=request.user).order_by('date_added')
	context = {'topics' : topics}
	return render(request, 'journpys/topics.html', context)


@login_required
def topic(request, topic_id):
	"""Get a topic and all of its entry."""
	topic = get_object_or_404(Topic, id=topic_id)
	check_topic_writer(request, topic_id)
	entries = topic.entry_set.order_by('-date_added')
	context = {'topic': topic, 'entries': entries}
	return render(request, 'journpys/topic.html', context)


@login_required
def new_topic(request):
	"""Allow users to enter a new topic."""
	if request.method != 'POST':
		# No data submitted therefore create a blank form.
		form = TopicForm()
	else:
		# POST data submitted and process data.
		form = TopicForm(data=request.POST)
		if form.is_valid():
			new_topic = form.save(commit=False)
			new_topic.writer = request.user
			new_topic.save()
			return redirect('journpys:topics')

	# Display a blank or invalid form.
	context = {'form': form}
	return render(request, 'journpys/new_topic.html', context)


@login_required
def new_entry(request, topic_id):
	"""New entry for a topic"""
	topic = get_object_or_404(Topic, id=topic_id)
	check_topic_writer(request, topic_id)
	
	if request.method != 'POST':
		# No data submitted; create a blank form
		form = EntryForm()
	else:
		# POST and process data
		form = EntryForm(data=request.POST)

		if form.is_valid:
			new_entry = form.save(commit=False)
			# Set the topic attribute of new_entry to the topic pulled from
			# the database at the begining of the function
			new_entry.topic = topic
			new_entry.save()
			return redirect('journpys:topic', topic_id=topic_id)

	# Display a blank or invalid form.
	context = {'topic': topic, 'form': form}
	return render(request, 'journpys/new_entry.html', context)


@login_required
def edit_entry(request, entry_id):
	"""Edit an existing entry."""
	entry = get_object_or_404(Entry, id=entry_id)
	topic = entry.topic
	if topic.writer != request.user:
		raise Http404

	if request.method != 'POST':
		# Initial request; pre-fill form with the current entry.
		form = EntryForm(instance=entry)
	else:
		# POST data submitted; process data.
		form = EntryForm(instance=entry, data=request.POST)

		if form.is_valid():
			form.save()
			return redirect('journpys:topic', topic_id=topic.id)
	context = {'entry': entry, 'topic': topic, 'form': form}
	return render(request, 'journpys/edit_entry.html', context)


def check_topic_writer(request, topic_id):
	"""Check whether the writer of the topic matches the currently logged in 
		user. If not, raise an Http404 exception."""
	topic = Topic.objects.get(id=topic_id)
	if topic.writer != request.user:
		raise Http404


@login_required
def delete_topic(request, topic_id):
	"""Delete a topic and all of it's entries."""
	topic = get_object_or_404(Topic, id=topic_id)
	topic.delete()
	return redirect('journpys:topics')
	context = {'topic': topic}
	return render(request, 'journpys/delete_topic.html', context)


@login_required
def delete_entry(request, entry_id):
	"""Delete an existing entry."""
	entry = get_object_or_404(Entry, id=entry_id)
	topic = entry.topic
	entry.delete()
	return redirect('journpys:topic', topic_id=topic.id)
	context = {'entry': entry, 'topic': topic}
	return render(request, 'journpys/delete_entry.html', context)
	

