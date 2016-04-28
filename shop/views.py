from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Category, Product

def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    # With QuerySet available=True to retrieve only available products
    products = Product.objects.filter(available=True)
    # category_slug parameter to optionally filter products by a given category
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category)
    return render(request, 'shop/product/list.html',
                  { 'category' : category,
                    'categories' : categories,
                    'products' : products
                })


# Create your views here.
def product_detail(request, id, slug):
    """
    The prodcut_detail view expects id and slug parameters in order to
    retrieve the Product instance.
    :param request:
    :param id:
    :param slug:
    :return:
    """
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    return render(request, 'shop/product/detail.html', {'product': product})














