from django.db import models

class Tweet(models.Model):
	text = models.CharField(max_length=150)
	location = models.CharField(max_length=50)
	user = models.CharField(max_length=50)
	date = models.DateTimeField()
	sentiment = models.DecimalField(max_digits=4, decimal_places=1, null=True)
	
	def __unicode__(self):
		return self.text

class State(models.Model):
	name = models.CharField(max_length=15)
	abbrev = models.CharField(max_length=2)
	sentiment = models.DecimalField(max_digits=4, decimal_places=1, null=True)

	def __unicode__(self):
		return (self.name + ' : ' + str(self.sentiment))
