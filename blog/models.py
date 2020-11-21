from django.db import models
from django.urls import reverse

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100, blank=False)
    description = models.TextField(blank=False)
    image = models.ImageField(upload_to="blogImages/")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', args=[str(self.id)])

