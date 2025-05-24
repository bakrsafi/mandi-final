from django.shortcuts import render
from django.db.models import Q
from .models import Category ,Product
# Create your views here.

def home(request):
    context = {}
    return render(request,'products/home.html',context)

def menu(request):
    meat_only = request.GET.get("meat_only")
    chicken_only = request.GET.get("chicken_only")

    if meat_only:
        product_obj = Product.objects.filter(
            Q(name__icontains="لحم") |
            Q(category__name__in=["Cold Appetizers", "Hot Appetizers"])
        ).order_by('?')
    elif chicken_only:
        product_obj = Product.objects.filter(
            Q(name__icontains="دجاج") |
            Q(category__name__in=["Cold Appetizers", "Hot Appetizers"])
        ).order_by('?')
    else:
        product_obj = Product.objects.all().order_by('?')

    category_obj = Category.objects.all()

    context = {
        'product': product_obj,
        'category': category_obj
    }
    return render(request, 'products/menu.html', context) 



def about(request):
    context = {}
    return render(request,'products/about.html',context)
    
def contact(request):
    context = {}
    return render(request,'products/contact.html',context)
