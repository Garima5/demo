from django.db import models

# Create your models here.
class Salary(models.Model):
    empid = models.CharField(max_length=264)
    beltA = models.IntegerField(null=False)
    beltB = models.IntegerField(null=False)
    beltC = models.IntegerField(null=False)
    makingDate = models.DateField(null=False)
    #Salary = models.FloatField((beltA + beltB + beltC)*8)



    def __str__(self):
        return self.empid