
import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Question(models.Model):
    question_text= models.CharField( max_length=200)
    publish_date= models.DateTimeField("Date Published")
    
    
    def was_published_recently(self):
        return self.publish_date >= timezone.now() - datetime.timedelta(days=1)
    def __str__(self):
        return self.question_text


class Choice(models.Model):
      question = models.ForeignKey(Question, on_delete=models.CASCADE)
      choice_text = models.CharField(max_length=200)
      votes = models.IntegerField(default=0)
      def __str__(self):
        return self.choice_text