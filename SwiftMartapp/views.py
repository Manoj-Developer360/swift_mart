from django.shortcuts import render

def home(request):
    return render(request, "home.html")

def store(request):
    return render(request, "store.html")

def cart(request):
    return render(request, "cart.html")

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")