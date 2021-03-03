from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Developer

# Create your views here.
def index(request):
    devs = Developer.objects.all()
    context = {
        'devs' : devs
    }
    return render(request, 'ninjas/index.html', context)

def details(request, dev_id):
    dev = get_object_or_404(Developer, pk=dev_id)
    context = {
        'dev' : dev
    }
    return render(request, 'ninjas/details.html', context)

