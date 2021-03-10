from django.db import models

class Movie(models.Model):
    movie_name = models.CharField(max_length=100)
    movie_category = models.CharField(max_length=100)
    movie_duration = models.CharField(max_length=100)
    movie_country = models.CharField(max_length=100)
    producer_name = models.CharField(max_length=100)
    description = models.TextField()
    movie_image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.movie_name
