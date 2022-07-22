from django.shortcuts import render
from .models import about

# Create your views here.
def aboutus(request):
    aboutdata = about.objects.all()[0]

    context = {
        'about': aboutdata,
    }
    return render(request, 'about.html', context)