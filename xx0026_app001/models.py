from django.db import models

# Create your models here.
class Topic(models.Model):
	top_name= models.CharField(max_length= 100, unique= True)

	def __str__(self):
		return self.top_name

        
class Webpage(models.Model):
	xtopic= models.ForeignKey(Topic, on_delete= models.CASCADE,)	
	name= models.CharField(max_length= 200, unique= True)
	url= models.URLField(unique= True)

	def __str__(self):
		return self.name


class AccessRecord(models.Model):
	name= models.ForeignKey(Webpage, on_delete= models.CASCADE,)
	date= models.DateField()

	def __str__(self):
		return str(self.date)	
	