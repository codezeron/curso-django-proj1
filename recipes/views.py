from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'recipes/pages/home.html', status=201) 

def recipe(request, id):
    return render(request, 'recipes/pages/recipe-view.html', context={
        'name': 'Enzo', 
}) 

# its calling by namespace's folder called recipes in 'templates'
# now have to specify where the html's arq is


def contato(request):
    return render(request, 'recipes/contato.html')


def sobre(request):
    return HttpResponse('SOBRE')    