from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name

class Movie(models.Model):
    movie_name = models.CharField(max_length=100)
    movie_category = models.ManyToManyField('Category', related_name='movies')
    movie_duration = models.CharField(max_length=100)
    movie_country = models.CharField(max_length=100)
    producer_name = models.CharField(max_length=100)
    description = models.TextField()
    movie_image = models.ImageField(upload_to='images/')
    created_on = models.DateTimeField()
    last_modified = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.movie_name
