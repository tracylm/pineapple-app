from django.shortcuts import render
from django.http import HttpResponse
from pineapple.models import Category
from pineapple.models import Page


def index(request):
    # context_dict = {'boldmessage': "Yummy, broccoli, arugula, brussel sprouts, salmon!"}
    # return render(request, 'pineapple/index.html', context=context_dict)
    category_list = Category.objects.order_by('-likes')[:5]

    context_dict = {'categories': category_list}
    return render(request, 'pineapple/index.html', context_dict)

def about(request):
    # return HttpResponse("Learn about Pineapple here.")
    context_dict = {'boldmessage2': "Good with oranges, bananas, strawberries and perfect in smoothies!"}
    return render(request, 'pineapple/about.html', context=context_dict)

def happy(request):
    # return HttpResponse("Happiness is just around the corner.")
    html = "<html><body><h1>Be happy!</h1><p>You are awesome!</p></body></html>"
    return HttpResponse(html)

def show_category(request, category_name_slug):
    #
    #
    context_dict = {}
    try:
        #
        #
        #
        category = Category.objects.get(slug=category_name_slug)
        #
        #
        pages = Page.objects.filter(category=category)
        #
        context_dict['pages'] = pages
        #
        #
        #
        context_dict['category'] = category
    except Category.DoesNotExist:
        #
        #
        context_dict['category'] = None
        context_dict['pages'] = None
        #
    return render(request, 'pineapple/category.html', context_dict)
