from django.shortcuts import render

INDEX_HTML = 'menu/index.html'


def index(request):
    return render(request, INDEX_HTML)
