from django.shortcuts import render, redirect
from .models import Gender, Year, Course, Student, Section
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.core.paginator import Paginator


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
    messages.success(request,'Successfully Saved!')
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


def index_section(request):
    sections = Section.objects.all()

    context = {
        'sections': sections
    }

    return render(request, 'section/index.html', context)

def create_section(request):
    return render(request, 'section/create.html')

def store_section(request):
    section = request.POST.get('section')
    Section.objects.create(section=section)
    messages.success(request, 'Section succesfully saved.')
    return redirect('/sections')
    
def show_section(request, section_id):
    section = Section.objects.get(pk=section_id) 

    context = {
        'section': section,
    }

    return render(request, 'section/show.html', context)

def edit_section(request, section_id):
    section = Section.objects.get(pk=section_id) 

    context = {
        'section': section,
    }

    return render(request, 'section/edit.html', context)

def update_section(request, section_id):
    section = request.POST.get('section')
    Section.objects.filter(pk=section_id).update(section=section)
    messages.success(request, 'Section successfully updated.')

    return redirect('/sections')

def delete_section(request, section_id):
    section = Section.objects.get(pk=section_id) 

    context = {
        'section': section,
    }

    return render(request, 'section/delete.html', context)

def destroy_section(request, section_id):
    Section.objects.filter(pk=section_id).delete()
    messages.success(request, 'Section successfully deleted.')

    return redirect('/sections')

def index_year(request):
    query = request.GET.get('year_list')
    if query:
        years = Year.objects.filter(year__icontains=query)
    else:
        years = Year.objects.all()

    paginator = Paginator(years, 10) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'years': page_obj,
        'query': query

    }
    
    return render(request, 'year/index.html', context)

def create_year(request):
    return render(request, 'year/create.html')

def store_year(request):
    year = request.POST.get('year')
    Year.objects.create(year=year) 
    messages.success(request, 'Year Level succesfully saved.')
    return redirect('/years')
    
def show_year(request, year_id):
    year = Year.objects.get(pk=year_id)

    context = {
        'year': year,
    }

    return render(request, 'year/show.html', context)

def edit_year(request, year_id):
    year = Year.objects.get(pk=year_id)

    context = {
        'year': year,
    }

    return render(request, 'year/edit.html', context)

def update_year(request, year_id):
    year = request.POST.get('year')

    Year.objects.filter(pk=year_id).update(year=year)
    messages.success(request, 'Year Level successfully updated.')

    return redirect('/years')

def delete_year(request, year_id):
    year = Year.objects.get(pk=year_id)

    context = {
        'year': year,
    }

    return render(request, 'year/delete.html', context)

def destroy_year(request, year_id):
    Year.objects.filter(pk=year_id).delete()
    messages.success(request, 'Year Level successfully deleted.')

    return redirect('/years')

def index_course(request):
    courses = Course.objects.all()
    
    context = {
        'courses': courses
    }
    
    return render(request, 'course/index.html', context)

def create_course(request):
    return render(request, 'course/create.html')

def store_course(request):
    course = request.POST.get('course')
    Course.objects.create(course=course)
    messages.success(request, 'Course succesfully saved.')
    return redirect('/courses')
    
def show_course(request, course_id):
    course = Course.objects.get(pk=course_id) 

    context = {
        'course': course,
    }

    return render(request, 'course/show.html', context)

def edit_course(request, course_id):
    course = Course.objects.get(pk=course_id)

    context = {
        'course': course,
    }

    return render(request, 'course/edit.html', context)

def update_course(request, course_id):
    course = request.POST.get('course')

    Course.objects.filter(pk=course_id).update(course=course)
    messages.success(request, 'Course successfully updated.')

    return redirect('/courses')

def delete_course(request, course_id):
    course = Course.objects.get(pk=course_id)

    context = {
        'course': course,
    }

    return render(request, 'course/delete.html', context)

def destroy_course(request, course_id):
    Course.objects.filter(pk=course_id).delete()
    messages.success(request, 'Course successfully deleted.')

    return redirect('/courses')

def index_student(request):
    students = Student.objects.select_related('gender', 'course', 'year', 'section')
    query = request.GET.get('students')
    if query:
        students = Student.objects.filter(first_name__icontains=query)
    else:
        students = Student.objects.all()

    paginator = Paginator(students, 10)  
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'students': page_obj,
        'query' : query,
    }

    return render(request, 'student/index.html', context)

def create_student(request):
    genders = Gender.objects.all()
    sections = Section.objects.all()
    courses = Course.objects.all()
    years = Year.objects.all()

    context = {
    'genders': genders,
    'sections': sections,
    'courses': courses,
    'years': years,
    
    }

    return render(request, 'student/create.html', context)

def store_student(request):
    firstName = request.POST.get('first_name')
    middleName = request.POST.get('middle_name')
    lastName = request.POST.get('last_name')
    age = request.POST.get('age')
    genderid = request.POST.get('gender_id')
    sectionid = request.POST.get('section_id')
    courseid = request.POST.get('course_id')
    yearid = request.POST.get('year_id')
    address = request.POST.get('address')

    Student.objects.create(
        first_name = firstName,
        middle_name = middleName,
        last_name = lastName,
        age = age,
        gender_id = genderid,
        section_id = sectionid,
        course_id = courseid,
        year_id = yearid,
        address= address
    )

    messages.success(request, 'Profile succesfully saved.')

    return redirect('/students')

def show_student(request, student_id):
    gender = Gender.objects.all()
    section= Section.objects.all()
    course = Course.objects.all()
    year = Year.objects.all()
    student = Student.objects.get(pk=student_id)

    context = {
        'student': student,
        'gender' : gender,
        'course' : course,
        'year' : year,
        'section': section,  
    }

    return render(request, 'student/show.html', context)

def edit_student(request, student_id):
    genders = Gender.objects.all()
    courses = Course.objects.all()
    years = Year.objects.all()
    sections = Section.objects.all()
    student = Student.objects.get(pk=student_id)

    context = {
        'student': student,
        'genders' : genders,
        'courses' : courses,
        'years' : years,
        'sections': sections,
    }

    return render(request, 'student/edit.html', context)

def update_student(request, student_id):
    firstName = request.POST.get('first_name')
    middleName = request.POST.get('middle_name')
    lastName = request.POST.get('last_name')
    age = request.POST.get('age')
    genderid = request.POST.get('gender_id')
    sectionid = request.POST.get('section_id')
    courseid = request.POST.get('course_id')
    yearid = request.POST.get('year_id')
    address = request.POST.get('address')
    
    Student.objects.filter(pk=student_id).update(
        first_name = firstName,
        middle_name = middleName,
        last_name = lastName,
        age = age,
        gender_id = genderid,
        section_id = sectionid,
        course_id = courseid,
        year_id = yearid,
        address= address
    )

    messages.success(request, 'Profile successfully updated.')
    return redirect('/students')

def delete_student(request, student_id):
    student = Student.objects.get(pk=student_id) 

    context = {
        'student': student,
    }

    return render(request, 'student/delete.html', context)

def destroy_student(request, student_id):
    Student.objects.filter(pk=student_id).delete()
    messages.success(request, 'Profile successfully deleted.')

    return redirect('/students')