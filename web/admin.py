from django.contrib import admin

from web.models import Customers, Feature, Subscribe


admin.site.register(Subscribe)
admin.site.register(Customers)

class FeatureAdmin(admin.ModelAdmin):
    list_display = ["id", "title","testimonial_author", "author_designation" ]

admin.site.register(Feature, FeatureAdmin)