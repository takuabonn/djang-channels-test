from django.db import models

# Create your models here.
class Article(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.TextField()
    body = models.TextField()
    status = models.TextField()

