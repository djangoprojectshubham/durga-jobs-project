from django.db import models

# Create your models here.
class hydjobs(models.Model):
    date=models.DateField();
    company=models.CharField(max_length=100);
    tittle=models.CharField(max_length=100);
    eligibility=models.CharField(max_length=100);
    address=models.CharField(max_length=100);
    email=models.EmailField();

class blorejobs(models.Model):
    date=models.DateField();
    company=models.CharField(max_length=100);
    tittle=models.CharField(max_length=100);
    eligibility=models.CharField(max_length=100);
    address=models.CharField(max_length=100);
    email=models.EmailField();

class chennaijobs(models.Model):
    date=models.DateField();
    company=models.CharField(max_length=100);
    tittle=models.CharField(max_length=100);
    eligibility=models.CharField(max_length=100);
    address=models.CharField(max_length=100);
    email=models.EmailField();


class punejobs(models.Model):
    date=models.DateField();
    company=models.CharField(max_length=100);
    tittle=models.CharField(max_length=100);
    eligibility=models.CharField(max_length=100);
    address=models.CharField(max_length=100);
    email=models.EmailField();
    
