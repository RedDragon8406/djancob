from django.db import models
import os
import random
from .utils import unique_slug_generator
from django.db.models.signals import pre_save

def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    new_name = random.randint(1, 27634723542)
    name, ext = get_filename_ext(filename)
    # final_name = f"{new_name}{ext}"
    final_name = f"{instance.id}-{instance.title}{ext}"
    return f"products/{final_name}"


class ProductManager(models.Manager):
    # =========================builtins=======================
    # ========================= new ==========================
    def get_by_id(self, productId):
        qs = self.get_queryset().filter(id=productId)
        if qs.count() == 1:
            return qs.first()
        return None

    def get_existent(self):
        return self.get_queryset().filter(existent=True)


class Product(models.Model):
    # ========================= columns ==========================
    title = models.CharField(max_length=30)
    slug = models.SlugField(blank=True,unique=True)
    seller = models.CharField(max_length=50, default='اسکوب')
    description = models.TextField()
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to='products/', null=True, blank=True)
    topic = models.CharField(max_length=50)
    existent = models.BooleanField(default=False)

    # ========================= functions ==========================

    def get_absolute_url(self):
        return f"/products/{self.slug}"

    # ========================= configure ==========================
    def __str__(self):
        return self.title

    objects = ProductManager()

def product_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(product_pre_save_receiver, sender=Product)
