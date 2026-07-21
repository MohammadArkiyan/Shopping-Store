from django.http import JsonResponse
from django.core.paginator import Paginator
from django.db.models import Q
from django.views import View
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Product, Comment
from .forms import CommentForm

def product_list_view(request):
    """ Show all products in different pages """

    min_price = request.GET.get('min')
    max_price = request.GET.get('max')

    product_filter = Q()

    if min_price:
        product_filter &= Q(price__gte=min_price)
    if max_price:
        product_filter &= Q(price__lte=max_price)

    colors = request.GET.getlist('color')
    if colors:
        product_filter &= Q(color__title__in=colors)

    sizes = request.GET.getlist('size')
    if sizes:
        product_filter &= Q(size__title__in=sizes)

    # get all products order by names
    all_products = Product.objects.filter(product_filter).order_by('title')

    # The number of product where we want to show in per page
    per_page = request.GET.get('per_page', 10)

    try:
        per_page = int(per_page)
        if per_page not in [10, 20, 30]:
            per_page = 10
    except (ValueError, TypeError):
        per_page = 10

    # Create an object from Paginator
    paginator = Paginator(all_products, per_page)

    # Get page number from url
    page_number = request.GET.get('page')

    # Get products for special page
    page_obj = paginator.get_page(page_number)

    is_ajax = request.headers.get('x-requested-with') == 'XMLHttpRequest'

    context = {
        'page_obj': page_obj,
        'paginator': paginator,
        'per_page': per_page,
        'min_price': min_price if min_price else '',
        'max_price': max_price if max_price else '',
        'selected_colors': colors,
        'selected_sizes': sizes,
    }

    if is_ajax:
        return render(request, 'product/product_list_partial.html', context)

    return render(request, 'product/shop.html', context)


def product_detail(request, pk):
    product = get_object_or_404(Product, id=pk)



    comments = product.comments.filter(is_active=True)

    latest_comments = Comment.objects.filter(is_active=True).order_by('-created_at')[:3]


    if request.user.is_authenticated:
        initial_data = {

            'name': f"{request.user.first_name} {request.user.last_name}",
            'email': request.user.email,
        }
        form = CommentForm(initial=initial_data)
    else:
        form = CommentForm()


    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():

            new_comment = form.save(commit=False)


            new_comment.product = product

            if request.user.is_authenticated:
                new_comment.user = request.user

                new_comment.name = request.user.get_full_name() or request.user.username
                new_comment.email = request.user.email


            new_comment.save()

            messages.success(request, 'Your comment has been successfully submitted and will be published after approval.')


            return redirect('product:detail', pk=pk)

    context = {
        'product': product,
        'form': form,
        'comments': comments,
        'comments_count': comments.count(),
        'latest_comments': latest_comments,
    }

    return render(request, 'product/detail.html', context)


def live_search_view(request):
    query = request.GET.get('q', None)

    if not query or len(query) < 2:
        return JsonResponse({'results': []})

    products = Product.objects.filter(
        Q(title__icontains=query) | Q(description__icontains=query)
    ).distinct().order_by('title')[:5]

    results = []
    for product in products:
        results.append({
            'name': product.title,

            'image_url': product.get_main_image() if
            getattr(product, 'get_main_image') else '/static/images/default.png',

            'url': product.get_absolute_url() if
            hasattr(product, 'get_absolute_url') else f"product/{product.pk}"

        })
    return JsonResponse({'results': results})


class CommentView(View):
    def get(self, request, *args, **kwargs):
        form = CommentForm()

        initial_data = {
            'name': f"{request.user.first_name} {request.user.last_name}",
            'email': request.user.email,
        }

        if request.user.is_authenticated:
            form = CommentForm(initial=initial_data)


        context = {'form': form}

        return render(request, 'product/detail.html', context)

    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)

        if form.is_valid():
            comment_instance = form.save(commit=False)
            comment_instance.user = request.user
            comment_instance.save()

        context = {'form': form}

        return render(request, 'product/detail.html', context)
