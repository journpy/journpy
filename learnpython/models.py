from django.db import models
from django.contrib.auth.models import User


class Title(models.Model):
	"""Title of the lesson."""
	text = models.CharField(max_length=255)
	date_added = models.DateTimeField(auto_now_add=True)


	def __str__(self):
		"""Return a string representation of the model."""
		return self.text


class Body(models.Model):
	"""Journal entry about a particular topic."""
	title = models.ForeignKey(Title, on_delete=models.CASCADE)
	text = models.TextField()
	date_added = models.DateTimeField(auto_now_add=True)
	image1 = models.ImageField(upload_to='images/', blank=True)
	image2 = models.ImageField(upload_to='images/', blank=True)


	class Meta:
		verbose_name_plural = 'bodies'


	def __str__(self):
		"""Return a string representation of the model."""
		# Add ellipsis only if a body is longer than 70 characters
		if len(self.text) > 70:
			return f"{self.text[:70]}..."

		else:
			return self.text
			
