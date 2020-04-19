from django.shortcuts import render
from django.views.generic import DetailView
from .models import Product

# Create your views here.

def product_list_view(request):
    products = Product.objects.all()
    title = "محصولات"
    context = {
        "object_list": products,
        "title": title,
    }

    return render(request, "products/products_list.html", context)



class ProductDetailView(DetailView):
    queryset = Product.objects.all()
    template_name = "products/product.html"

    def get_context_data(self, *args, object_list=None, **kwargs):
        context = super(ProductDetailView, self).get_context_data(*args, **kwargs)
        print(context)
        return context
