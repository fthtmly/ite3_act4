from django.db import models

STUDY_YEAR_CHOICES = [
    (1, "First Year"), 
    (2, "Second Year"), 
    (3, "Third Year"), 
    (4, "Fourth Year")
    ]

GENDER_CHOICES = [
    ("M", "Male"), 
    ("F", "Female"), 
    ("O", "Other")
    ]

class Student(models.Model):
    student_id = models.CharField(max_length=10, unique=True) 
    name = models.CharField(max_length=300, default="Unknown") 
    age = models.IntegerField(default=18)
    email = models.EmailField(unique=True)  
    phone_number = models.CharField(max_length=15, blank=True, null=True, default="")  
    course = models.CharField(max_length=5, default="GEN") 
    year_level = models.IntegerField(choices=STUDY_YEAR_CHOICES, default=1)  
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default="O") 
    address = models.TextField(blank=True, null=True, default="Not Provided")  
    gpa = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True, default=None)  

    def __str__(self):
        return f"{self.name} ({self.student_id})"