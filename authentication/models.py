# authentication/models.py

from django.contrib.auth.models import AbstractUser
from django.db import models

class Student(AbstractUser):
    full_name = models.CharField(max_length=200)
    admission_number = models.CharField(max_length=20, unique=True)
    course = models.CharField(max_length=100)
    year_of_study = models.PositiveIntegerField()
    email = models.EmailField(unique=True)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='student_set',  # Update related_name to avoid clash
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='student_set',  # Update related_name to avoid clash
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

    REQUIRED_FIELDS = ['email', 'full_name', 'admission_number', 'course', 'year_of_study']
    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username




# from django.db import models
# from django.conf import settings

# class Unit(models.Model):
#     student = models.ForeignKey(Student, on_delete=models.CASCADE)
#     unit_name = models.CharField(max_length=100)
#     result = models.CharField(max_length=10)

#     def __str__(self):
#         return f"{self.unit_name} - {self.unit_result} ({self.student.full_name})"

class Unit(models.Model):
    student = models.ForeignKey(Student, related_name='units', on_delete=models.CASCADE)
    unit_name = models.CharField(max_length=200)
    result = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return f"{self.unit_name} ({self.student.full_name})"




# class SchoolFees(models.Model):
#     student = models.ForeignKey(Student,related_name='SchoolFees', on_delete=models.CASCADE)
#     total_amount = models.DecimalField(max_digits=10, decimal_places=2)
#     amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
#     remaining_amount = models.DecimalField(max_digits=10, decimal_places=2, editable=False)

#     def save(self, *args, **kwargs):
#         self.remaining_amount = self.total_amount - self.amount_paid
#         super().save(*args, **kwargs)

#     def __str__(self):
#         return f"{self.student.full_name} - {self.remaining_amount}"



class SchoolFees(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    remaining_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def save(self, *args, **kwargs):
        self.remaining_amount = self.total_amount - self.amount_paid
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.student.full_name} - Fees"
