# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import datetime
from django.utils import timezone


# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    is_reviewd=models.BooleanField(verbose_name= "هل تمت المراجعة",default=False)
    pub_date = models.DateTimeField("تاريخ النشر", auto_now_add=True)
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    class Meta:
        verbose_name= "مقالة"
        verbose_name_plural= "مقالات"

    def __unicode__(self):
        return self.title
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text
