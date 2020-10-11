from django.db import models

# Create your models here.
class AwardCategories(models.Model):
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

    Award_Category = models.CharField(max_length=10, choices=Award_Category_Choices)
    Details = models.TextField(default="Details about the award")

    class Meta:
        verbose_name_plural = "award Categories"

    def __str__(self):
        # readeable_name = self.get
        return f'{self.Award_Category}'
    

class Nominees(models.Model):
    year_in_school = [
        (100, 'First Year'),
        (200, 'Second Year'),
        (300, 'Third Year'),
        (400, 'Fourth Year'),
        (500, 'Fifth Year'),
        (600, 'Sixth Year'),
        (700, 'Seventh Year')
    ]
    award_category = models.ForeignKey(AwardCategories, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    course_of_study = models.CharField(max_length=200)
    level = models.IntegerField(choices= year_in_school, default='100L')
    institution = models.CharField(max_length=200)
    reason_for_nomination = models.TextField()
    cumulative_grade_point = models.FloatField(max_length=4, null=True, blank=True)
    is_approved= models.BooleanField(default=False)
    votes = models.IntegerField(default=0)
    date_created = models.DateField(auto_now_add=True)


    class Meta:
        verbose_name_plural = "nominees"

    def __str__(self):
        return f'{self.full_name}'
    
    def get_total_vote(self):
        return self.votes

