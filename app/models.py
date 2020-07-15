from django.db import models

class CourseModel(models.Model):
    idno = models.AutoField(primary_key=True)
    cname = models.CharField(max_length=50)
    fname = models.CharField(max_length=50)
    date = models.DateField()
    time = models.CharField(max_length=20)
    fees = models.FloatField()
    duration = models.IntegerField()

class StudentModel(models.Model):
    idno = models.AutoField(primary_key=True)
    sname = models.CharField(max_length=50)
    gender = models.CharField(max_length=20)
    contact = models.IntegerField(unique=True)
    email = models.CharField(max_length=100,unique=True)
    password = models.CharField(max_length=20)

class EnrollCourse(models.Model):
    idno = models.AutoField(primary_key=True)
    cname = models.CharField(max_length=50)
    fname = models.CharField(max_length=50)
    time = models.CharField(max_length=20)
    fees = models.FloatField()
    duration = models.IntegerField()
    sid = models.IntegerField()