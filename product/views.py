from django.shortcuts import render
from .models import Product, ProductImages
from django.core.paginator import Paginator

# Create your views here.

def productlist(request):
    productlist = Product.objects.all()

    paginator = Paginator(productlist, 5) # Show 5 product per page
    page = request.GET.get('page')
    productlist = paginator.get_page(page)

    context = {'product_list': productlist}

    return render(request, 'product/product_list.html', context)


def productdetail(request, product_slug):
    productdetail = Product.objects.get(slug=product_slug)
    productimages = ProductImages.objects.filter(product=productdetail)

    context = {'product_detail': productdetail, 'product_images':productimages}
    return render(request, 'product/product_detail.html', context)
