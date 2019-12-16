from django.db import models

# Create your models here.
class childrens(models.Model):
	children = models.CharField(max_length=60)

	def __str__(self):
		return self.children

class game_playing(models.Model):
	game_child = models.ForeignKey(childrens, on_delete=models.CASCADE)
	game_play = models.CharField(max_length=60)

	def __str__(self):
		return self.game_play


class parents(models.Model):
	childs = models.ManyToManyField(childrens)
	parent = models.CharField(max_length=30)

	def __str__(self):
		return self.parent