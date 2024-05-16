from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField(default=0.0)
    description = models.TextField()
    image = models.URLField()

    def __str__(self):
        return self.name
