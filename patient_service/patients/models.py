from django.db import models
class Patient(models.Model):
 name = models.CharField(max_length=100)
 # Allow age to be null/blank so creating users or partial forms won't crash the DB
 age = models.IntegerField(null=True, blank=True)
 medical_history = models.TextField()