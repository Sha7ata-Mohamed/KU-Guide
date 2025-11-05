from django.shortcuts import render
# Create your views here.

def index(request):
    return render(request, 'index.html')


def faq(request):
    return render(request, 'faq.html')

def career(request):
    return render(request, 'career.html')

def profile(request):
    return render(request, 'profile.html')
def contact(request):
    return render(request, 'contact.html')

def signin(request):
    return render(request, 'signin.html')