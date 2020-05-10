from django.shortcuts import render

# Create your views here.
def cart_page(request):
    name = ""
    if request.method == 'GET':
        name = request.GET.get("add-cart")
    qs = name
    print(name)
    return render(request,'./cart.html')