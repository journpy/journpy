from django.db import models
from django.contrib.auth.models import User


class Topic(models.Model):
	"""A topic the user is learning about."""
	text = models.CharField(max_length=255)
	date_added = models.DateTimeField(auto_now_add=True)
	writer = models.ForeignKey(User, on_delete=models.CASCADE)


	def __str__(self):
		"""Return a string representation of the model."""
		return self.text


class Entry(models.Model):
	"""Journal entry about a particular topic."""
	topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
	text = models.TextField()
	date_added = models.DateTimeField(auto_now_add=True)


	class Meta:
		verbose_name_plural = 'entries'


	def __str__(self):
		"""Return a string representation of the model."""
		# Add ellipsis only if an entry is longer than 70 characters
		if len(self.text) > 70:
			return f"{self.text[:70]}..."

		else:
			return self.text
			
