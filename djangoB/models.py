from django.db import models

class Gender(models.Model):
    gender_id = models.BigAutoField(primary_key=True)
    gender = models.CharField(max_length=55) 
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True) 
    class Meta:
        db_table = 'genders'
    
    def __str__(self):
        return self.gender
    
class Year(models.Model):
    year_id = models.BigAutoField(primary_key=True, blank=False) 
    year = models.CharField(max_length=55, blank=False) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 

    class Meta:
        db_table = 'years'

    def __str__(self):
        return self.year

class Course(models.Model):
    course_id = models.BigAutoField(primary_key=True, blank=False) 
    course = models.CharField(max_length=55, blank=False) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 

    class Meta:
        db_table = 'courses'

    def __str__(self):
        return self.course
    
class Section(models.Model):
    section_id = models.BigAutoField(primary_key=True, blank=False) 
    section = models.CharField(max_length=55, blank=False) 
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True) 

    class Meta:
        db_table = 'sections'

    def __str__(self):
        return self.section
    
class Student(models.Model):
    student_id = models.BigAutoField(primary_key=True, blank=False)  
    first_name = models.CharField(max_length=55, blank=False)  
    middle_name = models.CharField(max_length=55, blank=False) 
    last_name = models.CharField(max_length=55, blank=False)  
    address = models.CharField(max_length=55, blank=False)  
    age = models.IntegerField(blank=False)
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE)
    year = models.ForeignKey(Year, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)  
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'students'