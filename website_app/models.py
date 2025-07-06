from django.db import models

class Member(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  phone = models.IntegerField(null=True)
  joined_date = models.DateField(null=True)

  def __str__(self):
    return f"{self.firstname} {self.lastname}"

class User(models.Model):
  email = models.CharField(max_length=255)
  password = models.CharField(max_length=255)

  def __str__(self):
    return f"{self.email}"

class MovieData(models.Model):
  movieid = models.IntegerField(primary_key=True)
  title = models.CharField(max_length=255)
  tags = models.TextField()

  def __str__(self):
    return self.title