
from django.db import models
from django.core.validators import MinValueValidator

class Paper(models.Model):
    # id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200, 
        null=True, 
        blank=True, 
        default="Add name to paper here")

    id_number = models.PositiveSmallIntegerField(default=0)
    num_questions = models.PositiveSmallIntegerField(default=50)

    p_type = models.CharField(
        max_length=1,
        choices=[("A", "A"), ("B", "B"), ("C", "C"),("D", "D"), ("E", "E"), ("", "")],
        null=True, 
        default="",
        blank=True)
    
    def __str__(self):
        return f'{self.name}, {self.id_number}'   

class PQuestion(models.Model):
    paper = models.ForeignKey(Paper,
        null=True,
        blank=True,
        on_delete=models.CASCADE)
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
    
    class Meta:
        verbose_name_plural = "questions"
        ordering = ['q_number']

    def __str__(self):
        return f"{self.q_number}, {self.answer}, mark:{self.mark}"
    

