from django.db import models
import os
import random


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    new_name = random.randint(1, 27634723542)
    name, ext = get_filename_ext(filename)
    # final_name = f"{new_name}{ext}"
    final_name = f"{instance.id}-{instance.title}{ext}"
    return f"masters/{final_name}"

class Master(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    image = models.ImageField(upload_to='masters/',null=True,blank=True)

    def __str__(self):
        return self.title