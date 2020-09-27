from djongo import models
from PIL import Image
# Create your models here.
class BlogData(models.Model):
    image=models.ImageField(upload_to='images')
    author=models.CharField(max_length=25)
    blog_title=models.CharField(max_length=100)
    blog=models.CharField(max_length=5005)
    date=models.DateField()
    tags=models.CharField(max_length=50)
    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.pk})
    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        super().save(force_insert, force_update, using, update_fields)

        # img = Image.open(self.image.path)

        # if img.height > 300 or img.width > 300:
        #     output_size = (200, 200)
        #     img.thumbnail(output_size)
        #     img.save(self.image.path)


