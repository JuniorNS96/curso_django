from django.shortcuts import render

# Create your views here.


def home(response):
    return render(response, 'recipes/pages/home.html', context={
        'name': 'Junior'
    })


def recipes(response, id):
    return render(response, 'recipes/pages/recipe-view.html', context={
        'name': 'Junior'
    })
