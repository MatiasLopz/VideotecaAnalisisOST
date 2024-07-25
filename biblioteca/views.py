from django.shortcuts import render

def index(request):
    template_name = 'index.html'
    context = {'nombre':'biblioteca'}
    return render(request, template_name, context )

