from django.shortcuts import render
from .models import Product

# Create your views here.

def productlist(request):
    productlist = Product.objects.all()

    context = {'product_list': productlist}

    return render(request, 'product/product_list.html', context)


def productdetail(request, id):
    productdetail = Product.objects.get(pk=id)

    context = {'product_detail': productdetail}

    return render(request, 'product/product_detail.html', context)
