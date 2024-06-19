from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

# Below is aclass called 'Question'
# This Python class represents a model for a question with text and publication date attributes.
# This Python class defines a model for a question with text and publication date attributes.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

# Below is aclass called 'Choice'
# This class represents a choice for a question in a Python Django model, with attributes for the
# choice text and number of votes.
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
