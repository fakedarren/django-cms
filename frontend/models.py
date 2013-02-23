from django.db import models


class Page(models.Model):
    url = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    created = models.DateTimeField('date published')


class Module(models.Model):
	page = models.ForeignKey(Page)
	name = models.CharField(max_length=50)
	content = models.TextField()
	status = models.BooleanField()