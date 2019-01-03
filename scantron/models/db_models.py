from django.db import models
from django.core.validators import MinValueValidator

class Faculty(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "faculties"
    def __str__(self):
        return self.name


class Department(models.Model):
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

    def __str__(self):
        return f"Dept. of {self.name}, TFaculty of {self.faculty}"


class Module(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=200)

    def __str__(self):
        return f"Module( {self.name}, {self.department})"


class Teacher(models.Model):
    name = models.CharField(max_length=200)
    department = models.ForeignKey(Department, on_delete=models.PROTECT)
    last_logged_in = models.DateTimeField('last logged in', null=True)

    def __str__(self):
        return self.name


class Student(models.Model):
    id = models.PositiveSmallIntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    department = models.ForeignKey(Department, 
        null=True,
        on_delete=models.CASCADE)
    dob = models.DateField(null=True)

    def __str__(self):
        return f"Student({self.id}, {self.name}, {self.department})"


class Question(models.Model):
    #Constants
    A_CHOICES = [("A", "A"), ("B", "B"), ("C", "C"),("D", "D"), ("E", "E"), ("", "")]

    #Number range
    Q_NUMBERS = zip(range(1, 201), range(1, 201)) 

    q_number = models.PositiveSmallIntegerField(
        choices=Q_NUMBERS,
        default=1)
    mark = models.DecimalField(
        decimal_places=4, 
        max_digits=6,
        default=1)
    answer = models.CharField(
        max_length=1,
        choices=A_CHOICES,
        default= "D")

    def __str__(self):
        return f"{self.q_number}, {self.answer}, mark:{self.mark}"
    
   
    

# class Exam(models.Model):
#     module = models.ForeignKey(Module, on_delete=models.PROTECT)
#     teacher = models.ForeignKey(Teacher, on_delete=models.PROTECT)
    # pub_data = models.DateTimeField()

    # user = models.ForeignKey(User)

# class 