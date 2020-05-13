from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
# from cart.models import Cart
from django.http import Http404
from.models import Product
from sellers.models import Seller
import json
# Create your views here.

def main_product(request):
    title = 'محصولات اسکوب'
    lenght_products = Product.objects.count()
    last_products = Product.objects.all()[lenght_products-3:]
    lenght_sellers = Seller.objects.count()

    with open("categories.json", "r") as file:
        length_ProductCategories = json.load(file)

    length_ProductCategories = len(length_ProductCategories['categories'])


    context = {
        'title':title,
        'last_products':last_products,
        'length_sellers':lenght_sellers,
        'length_ProductCategories':length_ProductCategories,
    }
    return render(request,'products/main-products.html',context)


def product_list_view(request):
    products = Product.objects.all()
    title = "محصولات"
    # if request.method == "POST":
    print(request.REQUEST.get("#cart-adding"))
    context = {
        "object_list": products,
        "title": title,
    }

    return render(request, "products/products_list.html", context)


class ProductListView(ListView):
    queryset = Product.objects.all()
    template_name = "products/products_list.html"
    title = 'محصولات'

    def get_context_data(self, *args, object_list=None, **kwargs):
        context = super(ProductListView, self).get_context_data(*args, **kwargs)
        context['title'] = self.title
        return context


class ProductExistentListView(ListView):
    template_name = "products/products_list.html"
    title = 'محصولات موجود'

    def get_context_data(self, *args, object_list=None, **kwargs):
        context = super(ProductExistentListView, self).get_context_data(*args, **kwargs)
        context['title'] = self.title
        return context

    def get_queryset(self):
        return Product.objects.get_existent()


class ProductDetailSlugView(DetailView):
    template_name = "products/product.html"

    def get_object(self, *args, **kwargs):
        request = self.request
        slug = self.kwargs.get('slug')
        try:
            product = Product.objects.get(slug=slug)
        except Product.DoesNotExist:
            raise Http404("product does not exists")
        except Product.MultipleObjectsReturned:
            qs = Product.objects.filter(slug=slug)
            product = qs.first()
        except:
            raise Http404("not found :|")


        return product
    def get_queryset(self):
        return Product.objects.all()


class ProductDetailView(DetailView):
    template_name = "products/product.html"

    def get_queryset(self):
        return Product.objects.all()

    def get_object(self, *args, **kwargs):
        request = self.request
        productId = self.kwargs.get('pk')
        print(productId)
        product = Product.objects.get_by_id(productId)
        if product is None:
            raise Http404("product does not found from custom model manager")
        return product


def product_detail_view(request, productId=None, *args, **kwargs):
    product = Product.objects.get_by_id(productId)
    if product is None:
        raise Http404("چنین صفحه ای وجود ندارد.")
    context = {
        "object": product
    }

    return render(request, "products/product.html", context)
