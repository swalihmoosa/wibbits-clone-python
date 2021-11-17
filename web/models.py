from django.db import models


class Subscribe(models.Model):
    email = models.EmailField(max_length=25)

    def __str__(self):
        return self.email


class Customers(models.Model):
    image = models.FileField(upload_to="customers")

    def __str__(self):
        return self.id



class Feature(models.Model):
    image = models.ImageField(upload_to="features")
    icon = models.FileField(upload_to="features")
    icon_background = models.CharField(max_length=25)
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    testimonial_description = models.TextField(max_length=255)
    testimonial_author = models.CharField(max_length=255)
    author_designation = models.CharField(max_length=255)
    testimonial_logo = models.FileField(upload_to="features")

    def __str__(self):
        return self.testimonial_author


class Review(models.Model):
    title = models.CharField(max_length=155)
    image = models.FileField(upload_to="reviews")
    play = models.FileField(upload_to="reviews")
    logo = models.FileField(upload_to="reviews/logo")

    def __str__(self):
        return str(self.id)

