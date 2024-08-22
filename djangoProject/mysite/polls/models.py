from django.db import models

# class name
class subject(models.Model):
    # class field
    subject = models.CharField(max_length=50)
    frequency_s = models.IntegerField()

class sched(models.Model):
    day=models.CharField(max_length=20)
    timings=models.TimeField()
    n_classes=models.IntegerField()

class teacher(models.Model):
    t_name=models.CharField(max_length=20)
    subject=models.CharField(max_length=20)


class classs(models.Model):
    grade=models.CharField(max_length=20)
    section=models.CharField(max_length=5)







   