from django.db import models
from django.contrib.auth.models import User

# Alumni model
class Alumni(models.Model):
    alumni_id = models.AutoField(primary_key=True)  # Auto-incrementing ID for alumni tracking
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="alumni_profile")  # Link to Django User model
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    graduation_year = models.IntegerField()
    location = models.CharField(max_length=255)
    profile_picture = models.ImageField(upload_to='photos/', blank=True, null=True, default='default.png')
    batch = models.CharField(max_length=10)
    usn = models.CharField(max_length=20, unique=True)
    linkedin_url = models.URLField(max_length=255, blank=True)
    current_position = models.CharField(max_length=255)
    branch = models.CharField(max_length=100)
    company_name = models.CharField(max_length=255)
    bio = models.TextField(blank=True, null=True)
    achievements = models.TextField(blank=True, null=True)
    dob = models.DateField()
    is_alumni = models.BooleanField(default=True)  # Boolean field to check if the user is an alumni

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

# Student model
'''Students details'''
class Student(models.Model):
    student_id = models.AutoField(primary_key=True)  # Auto-incrementing ID for student tracking
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="student_profile")  # Link to Django User model
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    batch = models.CharField(max_length=10)  # Example: "2021-2025"
    email = models.EmailField(unique=True)
    usn = models.CharField(max_length=20, unique=True)  # Format: 4CB21AI031

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.usn})"
