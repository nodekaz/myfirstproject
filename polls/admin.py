# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Question ,Choice

# Register your models here.

def make_reviewed(ModelAdmin, request, queryset):
    queryset.update (is_reviewed = True)
make_reviewed.short_description = " تغيير حالة المراجعة"


class QuestionAdmin(admin.ModelAdmin):
    list_display=['title', 'author', 'pub_date', 'is_reviewed']
    list_filter= [ 'author', 'is_reviewed']
    search_fields= [ 'author', 'title', 'body']
    actions=[make_reviewed]


admin.site.register(Question)
admin.site.register(Choice)

