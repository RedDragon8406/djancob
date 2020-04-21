from django.shortcuts import render,get_object_or_404
from .models import Product
from django.http import Http404
# Create your views here.

def product_list_view(request):
    products = Product.objects.all()
    title = "محصولات"
    context = {
        "object_list": products,
        "title": title,
    }

    return render(request, "products/products_list.html", context)





def product_detail_view(request, productId=None, *args, **kwargs):
    product = Product.objects.get_by_id(productId)
    if product is None:
        raise Http404("چنین صفحه ای وجود ندارد.")
    context = {
        "object": product
    }

    return render(request, "products/product.html", context)