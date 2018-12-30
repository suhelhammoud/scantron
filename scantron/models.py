from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.


class Faculty(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Department(models.Model):
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)

    def __str__(self):
        return f"Dept. of {self.title}, TFaculty of {self.faculty}"


class Module(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    code = models.CharField(max_length=200)

    def __str__(self):
        return f"Module( {self.title}, {self.department})"


class Student(models.Model):
    std_id = models.IntegerField()
    fname = models.CharField(max_length=200)
    lname = models.CharField(max_length=200)
    father = models.CharField(max_length=200)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    dob = models.DateField()

    def __str__(self):
        return f"Student({self.std_id}, {self.fname} {self.lname}, {self.department})"


class Question(models.Model):
    # constants 
    A = "A"
    B = "B"
    C = "C"
    D = "D"
    E = "E"
    A_CHOICES = [(A, "A"), (B, "B"), (C, "C"), (D, "D"), (E, "E")]
    Q_NUMBERS = zip(range(1, 201), range(1, 201))

    q_number = models.PositiveSmallIntegerField(
        choices=Q_NUMBERS,
        default=1
    )
    answer = models.CharField(
        max_length=1,
        choices=A_CHOICES,
        default= D
    )

    def __str__(self):
        return f"{self.q_number}, {self.answer}"