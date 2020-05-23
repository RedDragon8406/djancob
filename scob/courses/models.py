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


class CourseManager(models.Manager):
    def get_by_id(self, courseId):
        qs = self.get_queryset().filter(id=courseId)
        if qs.count() == 1:
            return qs.first()
        return None


class Course(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    # conditions
    price = models.IntegerField(default=0)
    condition = models.CharField(max_length=20)
    master = models.CharField(max_length=20)
    pqs = models.TextField(null=True, blank=True)
    level = models.CharField(max_length=20,choices=[
        ('مقدماتی', 'مقدماتی'), ('متوسط', 'متوسط'), ('پیشرفته', 'پیشرفته'), ('فوق پیشرفته', 'فوق پیشرفته')
    ], default='مقدماتی')
    # end conditions
    image = models.ImageField(upload_to='courses/', null=True, blank=True)
    trailer = models.TextField(default='')
    topic = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.title

    objects = CourseManager()
