from django.db import models
from django.utils.text import slugify

# Create your models here.
# save a shortende link - name , url , slug , # of clicks

class Link(models.Model):
    name = models.CharField(max_length=100 , unique=True)
    url = models.URLField(max_length=225)
    slug = models.SlugField(unique=True , blank=True)
    clicks = models.PositiveBigIntegerField(default=0)

    def __str__(self):
        return f"{self.name} | {self.clicks}"
    
    # To automatically increment click instead of manual
    def click(self):
        self.clicks += 1
        self.save()

    # To make slug auto generated from the name filed
    def save(self , *args , **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args , **kwargs)

