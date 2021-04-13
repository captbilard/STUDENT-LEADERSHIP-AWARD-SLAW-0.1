from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    content=models.TextField()
    date_posted = models.DateField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Blog"


class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    comment = models.TextField()