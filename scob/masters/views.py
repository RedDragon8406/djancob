from django.shortcuts import render
from django.views.generic import DetailView
from .models import Master

# Create your views here.

def master_list_view(request):
    products = Master.objects.all()

    title = "اساتید"
    context = {
        "object_list": products,
        "title": title,
    }

    return render(request, "masters/masters_list.html", context)



class MasterDetailView(DetailView):
    queryset = Master.objects.all()
    template_name = "masters/master.html"

    def get_context_data(self, *args, object_list=None, **kwargs):
        context = super(MasterDetailView, self).get_context_data(*args, **kwargs)
        return context
