from django.shortcuts import render
from django.views.generic import DetailView
from .models import Course


# Create your views here.

def courses_list_view(request):
    products = Course.objects.all()
    title = "دوره ها"
    context = {
        "object_list": products,
        "title": title,
    }


    return render(request, "courses/courses_list.html", context)


class CoursesDetailView(DetailView):
    queryset = Course.objects.all()
    template_name = "courses/course.html"
    def get_context_data(self, *args, object_list=None, **kwargs):
        context = super(CoursesDetailView, self).get_context_data(*args, **kwargs)
        print(context)
        return context
