from django.shortcuts import render, get_object_or_404
from .models import Master
from courses.models import Course
from django.http import Http404


# Create your views here.

def master_list_view(request):
    products = Master.objects.all()

    title = "اساتید"
    context = {
        "object_list": products,
        "title": title,
    }

    return render(request, "masters/masters_list.html", context)


def master_detail_view(request, masterId=None, *args, **kwargs):
    master = Master.objects.get_by_id(masterId)
    if master is None:
        raise Http404("چنین صفحه ای وجود ندارد.")
    qs = Course.objects.filter(master=master.title)
    qs_count = qs.count()
    print(qs)
    context = {
        "object": master,
        "courses": qs,
        "courses_lenght": qs_count,

    }

    return render(request, "masters/master.html", context)
