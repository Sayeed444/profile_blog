from django.db import models

# Create your models here.
class Portraits(models.Model):
    title = models.CharField(max_length=121)
    slug = models.SlugField(max_length=66,default=False)
    descriptinos = models.TextField(blank=True, null=True)
    datetime=models.DateTimeField(auto_now=False, auto_now_add=False)
    img=models.ImageField()

    def __str__(self):
        return self.title

    def textfild(self):
        return self.descriptinos[:250] + '... ... ... !'

    class Meta:
        ordering = ['-datetime']

class Cityseapes(models.Model):
    title = models.CharField(max_length=121)
    slug = models.SlugField(max_length=66,default=False)
    descriptinos = models.TextField(blank=True, null=True)
    datetime=models.DateTimeField(auto_now=False, auto_now_add=False)
    img=models.ImageField()

    def __str__(self):
        return self.title

    def textfild(self):
        return self.descriptinos[:250] + '... ... ... !'

    class Meta:
        ordering = ['-datetime']

class Nature(models.Model):
    title = models.CharField(max_length=121)
    slug = models.SlugField(max_length=66,default=False)
    descriptinos = models.TextField(blank=True, null=True)
    datetime=models.DateTimeField(auto_now=False, auto_now_add=False)
    img=models.ImageField()

    def __str__(self):
        return self.title

    def textfild(self):
        return self.descriptinos[:400] + '... ... ... !'

    class Meta:
        ordering = ['-datetime']
