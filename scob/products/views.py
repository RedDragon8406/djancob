from django.shortcuts import render,get_object_or_404
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





def product_detail_view(request, productId=None, *args, **kwargs):
    # product = Product.objects.get(id=productId)
    product = get_object_or_404(Product, id=productId)
    context = {
        "object": product
    }

    return render(request, "products/product.html", context)