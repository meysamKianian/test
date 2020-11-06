from django.db import models
from django.urls import reverse


# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    summary = models.TextField(default='سلام وقت بخیر')
    price = models.TextField(default='nui')

    def get_absolute_url(self):
        return reverse("products:product-detail", kwargs={"id": self.id})  # f"/products/{self.id}/"
