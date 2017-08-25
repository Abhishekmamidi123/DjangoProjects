# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class User(models.Model):
    FirstName = models.CharField(max_length=128)
    LastName = models.CharField(max_length=128)
    Email = models.EmailField(max_length=254,unique=True)

    def __str__(self):
        return self.FirstName+" "+self.LastName
