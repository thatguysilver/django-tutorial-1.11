import datetime
from django.db import models
from django.utils import timezone


class Question(models.Model):
    '''The question for our poll; also includes date published.'''

    def __str__(self):
        return self.question_text
    
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days = 1) <= self.pub_date <= now
    
    question_text = models.CharField(max_length = 200)
    pub_date = models.DateTimeField('date published')

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'



class Choice(models.Model):
    '''ForeignKey tells dj that each choice is related to a single q.
       choice_text creates a character field.
       votes is a running tally.'''

    
    def __str__(self):
        return self.choice_text

    
    question = models.ForeignKey(Question, on_delete = models.CASCADE)
    choice_text = models.CharField(max_length = 200)
    votes = models.IntegerField(default = 0)
