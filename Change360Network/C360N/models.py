from django.db import models

# Create your models here.
class Volunteers(models.Model):
    YES='YES'
    NO='NO'
    YES_NO_BUTTON_QUESTIONS =[
        (YES, 'YES'),
        (NO, 'NO')
    ]
    Full_Name = models.CharField(max_length=50)
    Email_Address = models.EmailField()
    Phone_Number = models.CharField(max_length=15)
    Country = models.CharField(max_length=60)
    State = models.CharField(max_length=50)
    University = models.CharField(max_length=100)
    Previous_volunteering_experience = models.CharField(max_length=3, choices=YES_NO_BUTTON_QUESTIONS, default=YES)
    Are_you_currently_volunteering_for_an_NGO = models.CharField(max_length=3, choices=YES_NO_BUTTON_QUESTIONS, default=YES)

    class Meta:
        verbose_name_plural = "Volunteers"
    
    def __str__(self):
        return self.Full_Name

    
    

