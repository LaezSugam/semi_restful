from django.shortcuts import render, redirect
from django.contrib import messages
from models import Product

# Create your views here.
def index(request):

    context = {
    "products" : Product.objects.all()
    }

    return render(request, "srestful/index.html", context)

def show(request, product_id):

    context = {
    "product" : Product.objects.get(id = product_id)
    }
    return render(request, "srestful/show.html", context)

def new(request):

    return render(request, "srestful/new.html")

def edit(request, product_id):
    context = {
    "product" : Product.objects.get(id = product_id)
    }

    return render(request, "srestful/edit.html", context)

def create(request):

    add = Product.objects.add_product(request.POST)

    if not add[0]:
        for mes in add[1]:
            messages.error(request, mes)
        return redirect("srestful:new")

    return redirect("srestful:index")

def update(request, product_id):

    update = Product.objects.edit_product(request.POST, product_id)

    if not update[0]:
        for mes in update[1]:
            messages.error(request, mes)
        return redirect("srestful:edit")

    return redirect("srestful:index")

def destroy(request, product_id):

    Product.objects.get(id=product_id).delete()

    return redirect("srestful:index")
