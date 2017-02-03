from django.db import models

class Group(models.Model):
	name=models.CharField(max_length=20)
	file=models.FileField(upload_to='groups/')
	created=models.DateTimeField(auto_now_add=True)