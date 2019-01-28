# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Post(models.Model):
    '''
    SQLite Table for News
    '''
    title = models.TextField()  # Post title
    link = models.TextField()   # Post link

    def __str__(self):
        return self.title
