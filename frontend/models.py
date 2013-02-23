from django.db import models


class Page(models.Model):
    url = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    template = models.CharField(max_length=50)
    order = models.IntegerField()
    created = models.DateTimeField('date published')
    def __unicode__(self):
        return self.name


class Module(models.Model):
	page = models.ForeignKey(Page)
	name = models.CharField(max_length=50)
	content = models.TextField()
	status = models.BooleanField()