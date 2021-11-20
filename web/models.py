from os import name
from django.db import models
from django.db.models.base import Model


CONTENT_TYPE = (
    ("blog_post", "Blog Post"),
    ("webinar", "Webinar"),
    ("report", "Report")
) 

COMPANY_SIZE = (
    ("1", "1-10"),
    ("2", "11-50"),
    ("3", "51-200"),
    ("4", "201-500"),
)

INDUSTRY = (
    ("agriculture", "Agriculture"),
    ("banking_&_finance", "Banking & Finance"),
    ("business_services_&_software", "Business Services & Software"),
)

JOB_ROLE = (
    ("c_suite", "C-Suite"),
    ("vp", "VP")
)

COUNTRY = (
    ("united_states", "United States"),
    ("afghanistan", "Afghanistan"),
    ("albania", "Albania"),
    ("algeria", "Algeria"),
    ("american_samoa", "American Samoa")
)


class Subscribe(models.Model):
    email = models.EmailField(max_length=25)

    def __str__(self):
        return self.email


class Customers(models.Model):
    image = models.FileField(upload_to="customers")
    white_image = models.FileField(upload_to="customers",blank=True,null=True)

    def __str__(self):
        return str(self.id)



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


class Testimonial(models.Model):
    image = models.ImageField(upload_to="testimonials")
    logo = models.FileField(upload_to="testimonials\logo",blank=True,null=True)
    description = models.TextField(max_length=255)
    name = models.CharField(max_length=125)
    role = models.CharField(max_length=125)
    company_name = models.CharField(max_length=125)
    is_featured = models.BooleanField()

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ["id"]


class Marketing(models.Model):
    image = models.FileField(upload_to="marketing")
    title = models.CharField(max_length=155)
    description = models.TextField(max_length=255)

    def __str__(self):
        return str(self.title)

    class Meta:
        ordering = ["id"]
    


class Product(models.Model):
    image = models.FileField(upload_to="product")
    title = models.CharField(max_length=155)
    logo = models.FileField(upload_to="product/logo")
    description = models.TextField(max_length=255)
    bg_color = models.CharField(max_length=10, default="#fff")
    button_bg_color = models.CharField(max_length=10, default="#fff")

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["id"]



class Blog(models.Model):
    image = models.FileField(upload_to="blog")
    title = models.CharField(max_length=155)
    content_type = models.TextField(max_length=125, choices=CONTENT_TYPE)
    next = models.CharField(max_length=125, default="Read blog")

    def __str__(self):
        return self.title
    
    class Meta :
        ordering = ["id"]


class Contact(models.Model):
    email = models.EmailField()
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    company = models.CharField(max_length=128)
    company_size = models.CharField(max_length=128,choices=COMPANY_SIZE)
    industry = models.CharField(max_length=128,choices=INDUSTRY)
    jobe_role = models.CharField(max_length=128,choices=JOB_ROLE)
    country = models.CharField(max_length=128,choices=COUNTRY)
    user_agreement = models.BooleanField(default=False)

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return self.first_name