from django.contrib import admin
# A single dot means that the module or package referenced is in the same directory as the current location. 
from .models import Item

# Register your models here.
admin.site.register(Item)
