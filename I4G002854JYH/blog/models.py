from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Post(models.Model):
    Title = models.CharField(max_length=200)
    Text = models.TextField('Any amount of text')
    Author = models.ForeignKey('Post', on_delete = get_user_model())
    Created_date = models.DateTimeField('A date-time column')
    Published_date = models.DateTimeField('A date-time column')
