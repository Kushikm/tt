from django.db import models




# Create your models here.
class classroom(models.Model):
    classnum=models.CharField(max_length=30)
     
    def __str__(self):
        return self.classnum

