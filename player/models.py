from django.db import models

# Create your models here.

class Club(models.Model):
	name = models.CharField("Player name",max_length=100)
	slug = models.SlugField("*",max_length=100, unique=True)

	def __str__(self):
		return self.name

class Player(models.Model):
	name = models.CharField("Player name",max_length=100)
	slug = models.SlugField("*",max_length=100, unique=True)
	image = models.ImageField('Rasmi', upload_to='players/')
	club = models.ForeignKey(Club, on_delete=models.CASCADE)
	age = models.PositiveIntegerField('Yoshi', default=0)
	height = models.CharField('Boyi', max_length=100)
	weight = models.CharField('Vazni', max_length=50)
	salary = models.PositiveIntegerField('Maoshi',default=0)


	def __str__(self):
		return self.name