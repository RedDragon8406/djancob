from django.contrib.auth import authenticate, login, logout, get_user_model
from django.shortcuts import render
from .forms import Login_form, Register_form, contact_form
from django.db.models import Q

from courses.models import Course
from products.models import Product


def main_page(request):
    print(f"is user logged in : {request.user.is_authenticated}")
    tedad_c = Course.objects.count() - 1
    lastest_c = Course.objects.all()[(tedad_c - 2):]
    tedad_p = Product.objects.count() - 1
    lastest_p = Product.objects.all()[(tedad_p - 2):]

    front_topic = Course.objects.filter(topic__contains="frontend").count()
    back_topic = Course.objects.filter(topic__contains="backend").count()
    python_topic = Course.objects.filter(topic__contains="python").count()
    graphics_topic = Course.objects.filter(topic__contains="graphics").count()

    home_topic = Product.objects.filter(topic__contains="home").count()
    farming_topic = Product.objects.filter(topic__contains="farming").count()
    digital_topic = Product.objects.filter(topic__contains="digital").count()
    book_topic = Product.objects.filter(topic__contains="book").count()

    users = User.objects.all()
    title = "اسکوب |‌صفحه ی اصلی"

    context = {
        "last_courses": lastest_c,
        "last_products": lastest_p,
        "front_topic": front_topic,
        "back_topic": back_topic,
        "python_topic": python_topic,
        "graphics_topic": graphics_topic,
        "home_topic": home_topic,
        "farming_topic": farming_topic,
        "digital_topic": digital_topic,
        "book_topic": book_topic,
        "title": title,
        "users" : users,
    }

    return render(request, "main.html", context)


def contact_page(request):
    form = contact_form(request.POST or None)
    title = "تماس با اسکوب"
    context = {
        "form": form,
        "title": title,
    }
    return render(request, "contact.html", context)


def about_page(request):
    title = "درباره ی اسکوب"
    context = {
        "title": title,
    }
    return render(request, "about.html", context)


def cart_page(request):
    title = "سبد خرید من"
    context = {
        "title": title,
    }
    return render(request, "cart.html", context)


def search_page(request):
    if request.method == "GET":
        print("in post in search")
        name = request.GET.get('searching')
        print(name)

        qs_c = Course.objects.filter(Q(title__contains=name) | Q(description__contains=name) | Q(topic__contains=name))
        qs_p = Product.objects.filter(Q(title__contains=name) | Q(description__contains=name) | Q(topic__contains=name))

        title = f"نتیجه ی {name}"

        context = {
            "course_list": qs_c,
            "product_list": qs_p,
            "title": title,
        }
    return render(request, "Search.html", context)




def login_page(request):
    print(f"is user logged in : {request.user.is_authenticated}")
    form = Login_form(request.POST or None)

    title = "ورود"

    context = {
        "form": form,
        "title": title,
    }
    if form.is_valid():
        username = form.cleaned_data.get("username")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username=username, email=email, password=password)
        if user is not None:
            login(request, user)
            context["form"] = Login_form()
            print("logined successfully")
        else:
            print("Error")

    return render(request, "login.html", context)


User = get_user_model()


def register_page(request):
    print(f"is user logged in : {request.user.is_authenticated}")
    form = Register_form(request.POST or None)

    title = "ثبت نام"

    context = {
        "form": form,
        "title": title,
    }
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get("username")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        first_name = form.cleaned_data.get("first_name")
        last_name = form.cleaned_data.get("last_name")
        new_user = User.objects.create_user(username=username, email=email, password=password, first_name=first_name,last_name=last_name)
        login(request, new_user)
    return render(request, "register.html", context)


def logout_page(request):
    logout(request)

    title = "خارج شدید"
    context = {
        "title": title,
    }
    return render(request, "logout.html",context)
