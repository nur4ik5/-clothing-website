from django.db import models

class Post(models.Model):
	title = models.CharField(max_length = 30)
	text = models.TextField()

	def __str__(self):
		return self.title

class Category(models.Model):
	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name


class Product(models.Model):
	image = models.ImageField()
	brend = models.CharField(max_length=60, null=True)
	title = models.CharField(max_length=100, null=True)
	price = models.CharField(max_length=25, null=True)
	category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)


	def __str__(self):
		return f"{self.brend} {self.title}"
