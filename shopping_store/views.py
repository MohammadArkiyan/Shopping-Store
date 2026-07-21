from django.shortcuts import render
from product.models import Category, Product


def index(request):


    # Get categories data.
    featured_categories = Category.objects.filter(is_featured=True)[:12]

    # Get products data.
    featured_products = Product.objects.filter(is_featured=True)[:8]

    # Get recent products data.
    recent_products = Product.objects.order_by('-date_added')[:8]

    context = {
        'featured_categories': featured_categories,
        'featured_products': featured_products,
        'recent_products':recent_products
    }
    return render(request, 'shopping_store/index.html', context)
