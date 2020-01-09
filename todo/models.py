from django.db import models

# Create your models here.
# Each model is represented by a class
class Item(models.Model):
    # Each database field is represented by a class variable
    name = models.CharField(max_length=30, blank=False)
    done = models.BooleanField(blank=False, default=False)

    def __str__(self):
        return self.name