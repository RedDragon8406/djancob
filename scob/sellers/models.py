from django.db import models
import os
import random
# Create your models here.


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    new_name = random.randint(1, 27634723542)
    name, ext = get_filename_ext(filename)
    # final_name = f"{new_name}{ext}"
    final_name = f"{instance.id}-{instance.title}{ext}"
    return f"sellers/{final_name}"

class SellerManager(models.Manager):
    def get_by_id(self,sellerId):
        qs = self.get_queryset().filter(id=sellerId)
        if qs.count() == 1:
            return qs.first()
        return None

class Seller(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to='sellers/',null=True,blank=True)

    def __str__(self):
        return self.name

    objects = SellerManager()