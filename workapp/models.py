from django.db import models


# Create your models here.
class Place(models.Model):
    image = models.ImageField(upload_to="pics")
    name = models.CharField(max_length=250)
    desc = models.TextField()

    def __str__(self):
        return self.name


class Movie:
    pass