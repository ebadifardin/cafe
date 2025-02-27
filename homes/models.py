from django.db import models

# Create your models here.
class Catgory(models.Model):
    titel=models.CharField(max_length=250)
    descriptions=models.CharField(max_length=250)
    is_public=models.BooleanField(default=True)
    slug=models.SlugField()

    def __str__(self):
        return f"{self.titel} ,{self.descriptions}"
    