import json
from django.http.response import HttpResponse
from django.shortcuts import render, redirect

from web.models import Feature, Marketing, Product, Review, Subscribe, Customers, Testimonial


def index(request):
    customers = Customers.objects.all()
    features = Feature.objects.all()
    reviews = Review.objects.all()
    true_testimonials = Testimonial.objects.filter(is_featured=True)
    false_testimonials = Testimonial.objects.filter(is_featured=False)
    marketings = Marketing.objects.all()
    products = Product.objects.all()

    context = {
        "customers" : customers,
        "features" : features,
        "reviews" : reviews,
        "true_testimonials" : true_testimonials,
        "false_testimonials" : false_testimonials,
        "marketings" : marketings,
        "products" : products
    }
    
    return render(request,"index.html",context=context)



def subscribe(request):
    email = request.POST.get("email")
    if not Subscribe.objects.filter(email=email).exists() and email:
        Subscribe.objects.create(
            email = email
        )

        response_data = {
            "status" : "success",
            "title" : "Successfully Registered",
            "message" : "You are Subscribed to the News Letter"
        }
    elif not email:
        response_data = {
            "status" : "error",
            "title" : "Enter a Valid Email",
            "message" : "You Enter a Invalid Email,Check the Email"
        }
    else:
        response_data = {
            "status" : "error",
            "title" : "Already Registered",
            "message" : "You are Already Subscribed to the News Letter,no need to Subscribe again"
        }

    return HttpResponse(json.dumps(response_data),content_type="application/javascript")
