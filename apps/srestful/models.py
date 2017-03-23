from __future__ import unicode_literals

from django.db import models

# Create your models here.
class ProductManager(models.Manager):
    def add_product(self, postData):
        errors = []
        if len(postData["name"]) < 1:
            errors.append("Name cannot be blank!")
        if len(postData["description"]) < 1:
            errors.append("Description cannot be blank")
        if len(postData["price"]) < 1:
            errors.append("Price cannot be blank")

        try:
            float(postData["price"])
        except ValueError:
            errors.append("Price must be a number")

        if not errors:
            self.create(name=postData["name"], description=postData["description"], price=postData["price"])
            return (True, "The product has been added.")
        else:
            return (False, errors)

    def edit_product(self, postData, product_id):
        errors = []
        if len(postData["name"]) < 1:
            errors.append("Name cannot be blank!")
        if len(postData["description"]) < 1:
            errors.append("Description cannot be blank")
        if len(postData["price"]) < 1:
            errors.append("Price cannot be blank")

        try:
            float(postData["price"])
        except ValueError:
            errors.append("Price must be a number")

        if not errors:
            this_product = self.get(id=product_id)
            this_product.name=postData["name"]
            this_product.description=postData["description"]
            this_product.price=postData["price"]
            this_product.save()
            return (True, "The product has been updated.")
        else:
            return (False, errors)

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=20, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = ProductManager()
