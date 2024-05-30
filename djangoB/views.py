from django.shortcuts import render, redirect
from .models import Gender, User
from django.contrib import messages
from django.contrib.auth.hashers import make_password


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

def showgender(request, gender_id):
    gender = Gender.objects.get(pk=gender_id)

    context = {
        'gender' : gender,
    }

    return render(request, 'gender/show.html', context)

def editgender(request, gender_id):
    gender = Gender.objects.get(pk=gender_id)

    context = {
        'gender' : gender,
    }

    return render(request, 'gender/edit.html', context)

def updategender(request, gender_id):
    
    gender = request.POST.get('gender')
    Gender.objects.filter(pk=gender_id).update(gender=gender)
    messages.success(request, 'Gender Successfully Updated')
    return redirect('/genders')


def deletegender(request, gender_id):
    gender = Gender.objects.get(pk=gender_id)

    context = {
        'gender' : gender,
    }

    return render(request, 'gender/delete.html', context)

def destroygender(request, gender_id):
    Gender.objects.filter(pk=gender_id).delete()
    messages.success(request,'Successfully Deleted.')
    return redirect('/genders')


def index_user(request):
    users = User.objects.select_related('gender')

    context={
        'users': users,
    }
    return render(request, 'user/index.html', context)

def create_user(request):
    genders = Gender.objects.all()

    context = {
        'genders':genders
    }
    return render(request, 'user/create.html', context)

def store_user(request):
    firstName = request.POST.get('first_name')
    middleName = request.POST.get('middle_name')
    lastName = request.POST.get('last_name')
    age = request.POST.get('age')
    birthDate = request.POST.get('birth_date')
    genderId = request.POST.get('gender_id')
    username = request.POST.get('username')
    password = request.POST.get('password')
    confirmPassword = request.POST.get('confirm_password')

   
    if password == confirmPassword:
        encryptedPassword = make_password(password)

        User.objects.create(
            first_name=firstName,
            middle_name=middleName,
            last_name=lastName,
            age=age,
            birth_date=birthDate,
            gender_id=genderId,
            username=username,
            password= encryptedPassword
            )
        messages.success(request, 'success')

        return redirect('/user')
    else:
        messages.error(request, 'error')
        return redirect('/create')

def show_user(request, user_id):
    user = User.objects.get(pk=user_id) #select from mysql

    context = {
        'user': user,
        'first_name':user,
    }
    return render(request, 'user/show.html', context)

def edit_user(request, user_id):
    genders = Gender.objects.all()
    user = User.objects.get(pk=user_id) #select a specfic object from mysql
    context = {
        'user': user,
        'genders':genders,
    }

    return render(request, 'user/edit.html', context)

def update_user(request, user_id):
    firstName = request.POST.get('first_name')
    middleName = request.POST.get('middle_name')
    lastName = request.POST.get('last_name')
    age = request.POST.get('age')
    birthDate = request.POST.get('birth_date')
    genderId = request.POST.get('gender_id')
    username = request.POST.get('username')

    User.objects.filter(pk=user_id).update(
        first_name=firstName,
        middle_name=middleName,
        last_name=lastName,
        age=age,
        birth_date=birthDate,
        gender_id=genderId,
        username=username,
        )
    messages.success(request, 'success')

    return redirect('/user')
def delete_user(request, user_id):
    user = User.objects.get(pk=user_id)  #select for mysql
    context = {
        'users': user,
    }
    
    return render(request, 'user/delete.html', context)

def destroy_user(request, user_id):
    User.objects.filter(pk=user_id).delete() #delete from mysql
    messages.success(request, 'user successfully Deleted')

    return redirect('/user')

def main_page(request):
    return render(request, 'interface/mainPage.html')