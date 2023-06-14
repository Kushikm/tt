from django.db import models




# Create your models here.
class instructor(models.Model):
      instructorid = models.CharField(primary_key=True,max_length=10)
      name = models.CharField(max_length=100)
      designation = models.CharField(max_length=50)
      email = models.EmailField()
      phone = models.CharField(max_length=15)

      def __str__(self):
        return self.name
         
class classroom(models.Model):
    classnum=models.CharField(max_length=30)

    def __str__(self):
        return self.classnum
    

