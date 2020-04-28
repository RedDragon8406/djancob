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
    return f"courses/{final_name}"

class Course(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    #conditions
    price = models.IntegerField(max_length=10,default=0)
    condition = models.CharField(max_length=20)
    master = models.CharField(max_length=20)
    master_img = models.ImageField(upload_to='courses/',null=True,blank=True)
    master_des = models.TextField(null=True,blank=True)
    pqs = models.TextField(null=True,blank=True)
    level = models.CharField(max_length=10)
    #end conditions
    image = models.ImageField(upload_to='courses/',null=True,blank=True)
    topic = models.CharField(max_length=50,null=True,blank=True)

    def __str__(self):
        return self.title