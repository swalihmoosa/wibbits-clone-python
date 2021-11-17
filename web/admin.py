from django.contrib import admin

from web.models import Customers, Feature, Subscribe


admin.site.register(Subscribe)
admin.site.register(Customers)
admin.site.register(Feature)