from pineapple.forms import CategoryForm, PageForm
from django.shortcuts import render
from django.http import HttpResponse
from pineapple.models import Category, Page
#from pineapple.models import Page


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
    context_dict = {}
    try:
        category = Category.objects.get(slug=category_name_slug)
        pages = Page.objects.filter(category=category)
        context_dict['pages'] = pages
        context_dict['category'] = category
    except Category.DoesNotExist:
        context_dict['category'] = None
        context_dict['pages'] = None
    return render(request, 'pineapple/category.html', context_dict)

def add_category(request):
    form = CategoryForm()
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            #cat = form.save(commit=True)
            # print(cat, cat.slug)
            return index(request)
        else:
            print(form.errors)
    return render(request, 'pineapple/add_category.html', {'form': form})

def add_page(request, category_name_slug):

    try:
        category = Category.objects.get(slug=category_name_slug)
    except Category.DoesNotExist:
        category = None

    form = PageForm()
    if request.method == 'POST':
        form = PageForm(request.POST)
        if form.is_valid():
            if category:
                page = form.save(commit=False)
                page.category = category
                page.views = 0
                page.save()
                return show_category(request, category_name_slug)
        else:
            print(form.errors)
    context_dict = {'form':form, 'category':category}
    return render(request, 'pineapple/add_page.html', context_dict)
