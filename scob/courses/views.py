from django.shortcuts import render, get_object_or_404
from .models import Course
from masters.models import Master
from django.http import Http404

# Create your views here.

def courses_list_view(request):
    products = Course.objects.all()
    title = "دوره ها"
    context = {
        "object_list": products,
        "title": title,
    }

    return render(request, "courses/courses_list.html", context)


def course_detail_view(request, courseId=None, *args, **kwargs):
    course = Course.objects.get_by_id(courseId)
    if course is None:
        raise Http404("چنین صفحه ای وجود ندارد.")
    qs = Master.objects.filter(title=course.master)
    if qs.exists() and qs.count() == 1:
        master = qs.first()
    master_des = master.description
    master_img = master.image
    master_id = master.id
    context = {
        "object": course,
        "master_img": master_img,
        "master_des": master_des,
        "master_id": master_id,
    }

    return render(request, "courses/course.html", context)
