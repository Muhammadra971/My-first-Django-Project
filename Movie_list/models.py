from django.db import models

# Create your models here.
class Moviedata(models.Model):
    title=models.CharField(max_length=250)
    year=models.IntegerField(max_length=200)
    discription=models.TextField(null=True)
    images=models.ImageField(upload_to='media/',null=True)