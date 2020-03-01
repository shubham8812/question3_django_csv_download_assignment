from django.db import models

# Create your models here.
class Titanic(models.Model):
    passid = models.IntegerField()
    survived = models.IntegerField()
    pclass = models.IntegerField()
    name = models.CharField(max_length = 250)
    age = models.FloatField()
    sibsp = models.IntegerField()
    parch = models.IntegerField()
    ticket = models.CharField(max_length = 250)
    fare = models.FloatField()
    embarked =  models.CharField(max_length = 250)


    def __str__(self):
        return "%s,%s"%(self.name,self.survived)
