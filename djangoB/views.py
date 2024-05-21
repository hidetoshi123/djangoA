from django.shortcuts import render, redirect
from .models import Gender
from django.contrib import messages


# Create your views here.

def indexgender(request):
    genders = Gender.objects.all()

    context = {
        'genders': genders
    }

    return render(request, 'gender/index.html', context)

def creategender(request):
    return render(request, 'gender/create.html')

def storegender(request):
    gender = request.POST.get('gender')
    Gender.objects.create(gender=gender)
    messages.success(request,'Successfully Save!')
    return redirect('/genders')
    