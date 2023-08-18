from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Event(models.Model):
    title = models.CharField(max_length=200)
    creator = models.ForeignKey(User,on_delete=models.CASCADE,related_name='created_events')
    collaborators = models.ManyToManyField(User,through='Collaboration')

    def __str__(self):
        return self.title

class Collaboration(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    accepted = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user} collaborating on {self.event}"

# Create your models here.
from django.db import models

# Create your models here.
