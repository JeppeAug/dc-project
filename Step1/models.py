from django.db import models

# Create your models here.

class Beregning1(models.Model):
    image = models.ImageField(upload_to="images/")
