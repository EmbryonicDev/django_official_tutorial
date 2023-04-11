from django.db import models
import datetime
from django.utils import timezone
# time zone support docs:
# https://docs.djangoproject.com/en/4.2/topics/i18n/timezones/


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    # all Field instances has an optional first argument
    # to integrate human readable name.
    # pub_date = machine-readable
    # 'date published' = human-readable

    def was_published_recently(self):
        now = timezone.now()
        # return self.pub_date <= timezone.now() - datetime.timedelta(days=1)
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
