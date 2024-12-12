from django.core.paginator import Paginator
from django.shortcuts import render
from products.models import Product


def product_list(request):
    products = Product.objects.all()
    
    # Set up pagination
    paginator = Paginator(products, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'products/product_list.html', {'page_obj': page_obj})

