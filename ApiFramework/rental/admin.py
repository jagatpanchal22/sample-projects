from django.contrib import admin
from .models import Friend, Borrowed, Belonging

# Register your models here.
admin.site.register(Friend)
admin.site.register(Belonging)
admin.site.register(Borrowed)
