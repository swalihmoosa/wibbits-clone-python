from django.contrib import admin

from web.models import Customers, Feature, Marketing, Product, Review, Subscribe, Testimonial


admin.site.register(Subscribe)
admin.site.register(Customers)



class FeatureAdmin(admin.ModelAdmin):
    list_display = ["id", "title","testimonial_author", "author_designation" ]

admin.site.register(Feature, FeatureAdmin)



class ReviewAdmin(admin.ModelAdmin):
    list_display = ["id", "title" ]

admin.site.register(Review, ReviewAdmin)


class TestimonialAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "role", "company_name", "is_featured"]

admin.site.register(Testimonial, TestimonialAdmin)



class MarketingAdmin(admin.ModelAdmin):
    list_display = ["id", "image", "title", "description"]

admin.site.register(Marketing, MarketingAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "description", "image", "logo"]

admin.site.register(Product, ProductAdmin)