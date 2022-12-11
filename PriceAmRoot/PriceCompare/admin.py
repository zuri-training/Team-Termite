from django.contrib import admin
from .models import *


# Register your models here.
admin.site.register(user)
admin.site.register(product)
admin.site.register(category)
admin.site.register(Vendor)
admin.site.register(comment)
