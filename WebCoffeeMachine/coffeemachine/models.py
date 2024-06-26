from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField(default=0.0)
    description = models.TextField()
    image = models.CharField(max_length=200)
    slug = models.SlugField(max_length=50, default='')

    def __str__(self):
        return self.name
