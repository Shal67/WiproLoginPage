from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django.db import models
class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    body = models.TextField()
class CustomManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().only('version', 'release_date', 'end_of_life_date', 'latest')

from django.db import models

class Business(models.Model):
    quarter = models.FloatField(blank=True, null=True)
    ser_ref = models.TextField(db_column='SER_REF', blank=True, null=True)  # Field name made lowercase.
    industry_code = models.TextField(blank=True, null=True)
    industry_name = models.TextField(blank=True, null=True)
    filledjobs = models.IntegerField(blank=True, null=True)
    filledjobsrevised = models.IntegerField(blank=True, null=True)
    filledjobsdiff = models.IntegerField(blank=True, null=True)
    filledjobs_diff = models.IntegerField(db_column='filledjobs%diff', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    total_earnings = models.IntegerField(blank=True, null=True)
    totalearningsrevised = models.IntegerField(blank=True, null=True)
    earningsdiff = models.IntegerField(blank=True, null=True)
    earnings_diff = models.FloatField(db_column='earnings%diff', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    id = models.IntegerField(blank=True,primary_key=True)

    class Meta:
        managed = False
        db_table = 'Business'