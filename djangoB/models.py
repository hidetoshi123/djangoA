from django.db import models

class Gender(models.Model):
    gender_id = models.BigAutoField(primary_key=True)
    # gender_id BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY - SQL EQUIVALENT
    gender = models.CharField(max_length=55) #gender VARCHAR(55) NOT NULL - sql equivalent
    created_at = models.DateTimeField(auto_now_add=True) # TIMESTAMP DEFAULT CURRENT TIMESTAMP
    updated_at = models.DateTimeField(auto_now=True) # TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
    class Meta:
        db_table = 'genders'
    
    def __str__(self):
        return self.gender
    
   
class User (models.Model):
    user_id = models.BigAutoField(primary_key=True, blank=False)
    first_name = models.CharField(max_length=55, blank=False)
    middle_name = models.CharField(max_length=55, blank=True)
    last_name = models.CharField(max_length=55, blank=False)  
    age = models.IntegerField(blank=False)
    birth_date = models.DateField(blank=False)
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE)
    username = models.CharField(max_length=55, blank=False)
    password = models.CharField(max_length=255, blank=False)
    created_at = models.DateTimeField(auto_now_add=True) # TIMESTAMP DEFAULT CURRENT TIMESTAMP
    updated_at = models.DateTimeField(auto_now=True) # TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
    class Meta:
        db_table = 'users'
