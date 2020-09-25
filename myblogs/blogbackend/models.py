from djongo import models

# Create your models here.
class BlogData(models.Model):
    image=models.ImageField()
    author=models.CharField(max_length=25)
    blog_title=models.CharField(max_length=100)
    blog=models.CharField(max_length=5005)
    date=models.DateField()
    tags=models.CharField(max_length=50)


