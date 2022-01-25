from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import DateTimeField
from django.urls import reverse
from django.utils import timezone

# Create your models here.
class Student_info(models.Model):
    subject= models.CharField(max_length=255)
    topic = models.CharField(max_length=255)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, related_name='quiz')
    def __str__(self):
        return self.topic


class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='questions')
    text=models.CharField('Question', max_length=255)

    def __str__(self):
        return self.text

class Answer(models.Model):
    
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    text= models.CharField('Answer', max_length=255)
    is_correct = models.BooleanField('Correct answer', default=False)

    def __str__(self):
        return self.text

class Polls(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='polls')
    text= models.CharField('Answer', max_length=255)

class ZoomLinks(models.Model):
    subject=models.CharField(max_length=255)
    meeting_id= models.CharField('Meeting ID', max_length=255)
    DateTimeField= models.DateTimeField(auto_now_add=True)
    teacher= models.ForeignKey(User, on_delete=models.CASCADE)
    