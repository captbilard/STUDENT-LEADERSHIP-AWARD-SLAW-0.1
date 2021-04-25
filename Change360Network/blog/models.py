from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField
# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    # content=models.TextField()
    content=RichTextField(blank=True, null = True)
    image = models.ImageField(upload_to='blog_images/', blank=True)
    author = models.CharField(max_length=255)
    date_posted = models.DateField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Blog"
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])


class Comment(models.Model):
    blog = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name='comments')
    comment = models.CharField(max_length=255)

    def __str__(self):
        return self.comment