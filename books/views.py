from django.shortcuts import render
from . import models


# Create your views here.

def site_view(request):
    if request.method == 'GET':
        books = models.Books.objects.all()
        return render(request, template_name='Library.html',
                      context={'books': books})
