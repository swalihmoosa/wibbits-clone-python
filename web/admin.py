from django.contrib import admin

from web.models import Customers, Feature, Review, Subscribe


admin.site.register(Subscribe)
admin.site.register(Customers)

class FeatureAdmin(admin.ModelAdmin):
    list_display = ["id", "title","testimonial_author", "author_designation" ]

admin.site.register(Feature, FeatureAdmin)

class ReviewAdmin(admin.ModelAdmin):
    list_display = ["id", "title" ]

admin.site.register(Review, ReviewAdmin)