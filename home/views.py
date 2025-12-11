from django.shortcuts import render # pyright: ignore[reportMissingModuleSource]

from django.http import HttpResponse # type: ignore
# Create your views here.

def home(request):
    peoples = [
        {'name': 'Anuj Acharya', 'age' : '20'},
        {'name': 'Arzun Malla', 'age' : '15'},
        {'name': 'Manish Thakur', 'age' : '19'},
        {'name': 'Krizol Thapa', 'age' : '22'},
        {'name': 'Bipul Acharya', 'age' : '23'}
    ]
    vege= ['pumpkin', 'tomato', 'potato']

    return render(request, 'index.html', context={'peoples' : peoples})

def success_page(request):
    return HttpResponse("Hello ,  This is a success page for dantadan tadan tadan.")

def about_page(request):
    return render(request, 'about.html')

def contact_page(request):
    return render(request, 'contact.html')