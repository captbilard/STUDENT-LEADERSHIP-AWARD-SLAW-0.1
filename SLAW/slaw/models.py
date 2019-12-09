from django.db import models

# Create your models here.
class awardCategories(models.Model):
    Campus_life_and_leadership_award = 'CLLA'
    Most_outstanding_student_union_leader_award = 'MOSULA'
    University_outstanding_new_leader_award = 'UONLA'
    Most_outstanding_ngo_leadership_award = 'MONLA'
    The_alumni_association_award = 'AAA'
    Next_rated_award = 'NRA'
    Unsung_hero_award = 'UHA'
    Bridge_builder_award = 'BBA'
    Vice_chancellor_volunteer_service_award = 'VCVSA'
    Humanitarian_award = 'HA'
    Award_of_literary_excellence = 'ALE'
    Student_media_personality_award = 'SMPA'
    Entrepreneurial_merit_award = 'EMA'
    Award_Category_Choices = [
        (Campus_life_and_leadership_award, 'Campus Life and Leadership Award'),
        (Most_outstanding_student_union_leader_award, 'Most Outstanding Student Union Leader Award'),
        (University_outstanding_new_leader_award, 'University Outstanding New Leader Award'),
        (Most_outstanding_ngo_leadership_award, 'Most Outstanding NGO Leadership Award'),
        (The_alumni_association_award, 'The Alumni Association Award'),
        (Next_rated_award, 'Next Rated Award'),
        (Unsung_hero_award, 'Unsung Hero Award'),
        (Bridge_builder_award, 'Bridge Builder Award'),
        (Vice_chancellor_volunteer_service_award, 'Vice Chancellor’s Volunteer Service Award'),
        (Humanitarian_award, 'Humanitarian Award'),
        (Award_of_literary_excellence, 'Award of Literary Excellence'),
        (Student_media_personality_award, 'Student Media Personality Award'),
        (Entrepreneurial_merit_award, 'Entrepreneurial Merit Award')

    ]

    Category_of_award = models.CharField(max_length=10, choices=Award_Category_Choices)
    award_details = models.TextField(default="Details about the award")

    class Meta:
        verbose_name_plural = "award Categories"

    def __str__(self):
        # readeable_name = self.get
        return f'{self.get_Category_of_award_display()}'
    

class Nominees(models.Model):
    year_in_school = [
        (100, '100'),
        (200, '200'),
        (300, '300'),
        (400, '400'),
        (500, '500'),
        (600, '600'),
        (700, '700')
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
