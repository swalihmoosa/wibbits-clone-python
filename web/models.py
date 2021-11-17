from django.db import models


class Subscribe(models.Model):
    email = models.EmailField(max_length=25)

    def __str__(self):
        return self.email


class Customers(models.Model):
    image = models.FileField(upload_to="customers")
