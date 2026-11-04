from django.db import models

# Create your models here.

class Hall(models.Model):
    name = models.CharField(max_length=50) # e.g. LT1, Twin LT
    capacity = models.IntegerField()
    def __str__(self): return f"{self.name} – {self.capacity} seats"

class Student(models.Model):
    mat_no = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=50) # e.g. ND Computer Science
    level = models.CharField(max_length=10) # ND1, HND2
    
    def __str__(self): return self.mat_no

class SeatAllocation(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE)
    seat_no = models.IntegerField()
    exam_date = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['hall__name', 'seat_no']
