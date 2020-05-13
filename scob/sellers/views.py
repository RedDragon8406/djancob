from django.shortcuts import render
from .models import Seller
from products.models import Product
from django.http import Http404
# Create your views here.

def seller_list_view(request):
    sellers = Seller.objects.all()

    title = "اساتید"
    context = {
        "object_list": sellers,
        "title": title,
    }

    return render(request, "sellers/sellers_list.html", context)


def seller_detail_view(request, sellerId=None, *args, **kwargs):
    seller = Seller.objects.get_by_id(sellerId)
    if seller is None:
        raise Http404("چنین صفحه ای وجود ندارد.")
    qs = Product.objects.filter(seller__icontains=seller.name)
    qs_count = qs.count()
    print(qs)
    context = {
        "object": seller,
        "products": qs,
        "products_length": qs_count,
    }

    return render(request, "sellers/seller.html", context)