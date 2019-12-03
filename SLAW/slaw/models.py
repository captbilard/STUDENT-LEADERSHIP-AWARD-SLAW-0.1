from django.db import models

# Create your models here.
class awardCategories(models.Model):
    Award_Category_Choices = [
        ('CLLA', 'Campus Life and Leadership Award'),
        ('MOSULA', 'Most Outstanding Student Union Leader Award'),
        ('UONLA', 'University Outstanding New Leader Award'),
        ('MONLA', 'Most Outstanding NGO Leadership Award'),
        ('AAA', 'The Alumni Association Award'),
        ('NRA', 'Next Rated Award'),
        ('UHA', 'Unsung Hero Award'),
        ('BBA', 'Bridge Builder Award'),
        ('VCVSA', 'Vice Chancellor’s Volunteer Service Award'),
        ('HA', 'Humanitarian Award'),
        ('ALE', 'Award of Literary Excellence'),
        ('SMPA', 'Student Media Personality Award'),
        ('EMA', 'Entrepreneurial Merit Award')

    ]

    Category_of_award = models.CharField(max_length=10, choices=Award_Category_Choices)

    class Meta:
        verbose_name_plural = "award Categories"

    def __str__(self):
        return f'{self.Category_of_award}'
    

class Nominees(models.Model):
    year_in_school = [
        ('100L', '100'),
        ('200L', '200'),
        ('300L', '300'),
        ('400L', '400'),
        ('500L', '500'),
        ('600L', '600'),
        ('700L', '700')
    ]
    Award_Category = models.ForeignKey(awardCategories, on_delete=models.CASCADE)
    Full_Name = models.CharField(max_length=100)
    Course_Of_Study = models.CharField(max_length=200)
    Level = models.IntegerField(choices= year_in_school, default='100L')
    Institution = models.CharField(max_length=200)
    Reason_for_nomination = models.TextField()
    CGPA = models.FloatField(max_length=4, null=True, blank=True)


    class Meta:
        verbose_name_plural = "nominees"



    # def awardCategoryRequiresGP(self):
    #     if self.Award_Category is "MOSULA":
    #         CGPA = models.FloatField()

    def __str__(self):
        return f'{self.Full_Name}'


class Votes(models.Model):
    nominees = models.ForeignKey(Nominees, on_delete=models.CASCADE)
    number_of_votes = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = "votes"
    
    def __str__(self):
        return f'{self.nominees}'
