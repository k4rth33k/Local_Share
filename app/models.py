from django.db import models

# Create your models here.

class Links(models.Model):
    id_s = models.AutoField(primary_key=True)
    link = models.TextField()