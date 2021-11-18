from django.contrib import admin

from web.models import Customers, Feature, Review, Subscribe, Testimonial


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
