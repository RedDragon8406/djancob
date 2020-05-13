from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from .models import Course
from masters.models import Master
from .models import Course
from masters.models import Master
from django.http import Http404


# Create your views here.

def main_course(request):
    title = 'دوره های اسکوب'

    tedad_c = Course.objects.count()
    last_courses = Course.objects.all()[tedad_c - 3:]



    number_of_courses = Course.objects.count()
    number_of_users = User.objects.count()
    number_of_masters = Master.objects.count()
    context = {
        'title':title,
        'number_of_courses': number_of_courses,
        'number_of_users' : number_of_users,
        'number_of_masters' : number_of_masters,
        'last_courses':last_courses,
    }
    return render(request,'courses/main-courses.html',context)


def courses_list_view(request):
    products = Course.objects.all()[::-1]
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
    user_fullname = request.user.first_name + " " + request.user.last_name
    context = {
        "object": course,
        "master_img": master_img,
        "master_des": master_des,
        "master_id": master_id,
        "user_fullname": user_fullname,
    }
    print(request.user.last_name)
    return render(request, "courses/course.html", context)
