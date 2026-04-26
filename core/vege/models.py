from django.db import models

# Create your models here.

class Recipe(models.Model):
    recipe_name = models.CharField(max_length=50)
    desc = models.TextField()
    image = models.ImageField(upload_to='recipe')

