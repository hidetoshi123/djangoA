from django.shortcuts import render

# Create your views here.

def gender(request):
    return render(request, 'gender/index.html')