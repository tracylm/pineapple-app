from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    context_dict = {'boldmessage': "Yummy, broccoli, arugula, brussel sprouts, salmon!"}
    return render(request, 'pineapple/index.html', context=context_dict)

def about(request):
    # return HttpResponse("Learn about Pineapple here.")
    context_dict = {'boldmessage2': "Good with oranges, bananas, strawberries and perfect in smoothies!"}
    return render(request, 'pineapple/about.html', context=context_dict)

def happy(request):
    # return HttpResponse("Happiness is just around the corner.")
    html = "<html><body><h1>Be happy!</h1><p>You are awesome!</p></body></html>"
    return HttpResponse(html)
