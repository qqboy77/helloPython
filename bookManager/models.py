from django.db import models
# -*- coding: utf-8 -*-
# from __future__ import unicode_literals

# Create your models here.
class Book(models.Model):
    book_name = models.CharField(max_length=64)
    book_author = models.CharField(max_length=64)
    add_time = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.book_name
