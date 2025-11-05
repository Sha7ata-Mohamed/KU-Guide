from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'index.html')


def faq(request):
    return render(request, 'faq.html')

def career(request):
    return render(request, 'career.html')

def contact(request):
    return render(request, 'contact.html')