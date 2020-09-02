from django.db import models

# Create your models here.
class Bucket(models.Model):
    bucket_name = models.CharField(max_length=50)

class Todolist(models.Model):
    bucket = models.ForeignKey(Bucket, on_delete=models.CASCADE)
    text = models.TextField()
    completed = models.BooleanField(default=False)