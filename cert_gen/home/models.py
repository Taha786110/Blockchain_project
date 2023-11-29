from django.db import models
from datetime import datetime

# Create your models here.
class details(models.Model):
    verify_id = models.CharField(max_length=12, blank=True)
    name = models.CharField(max_length=122, blank=True)
    yr = models.CharField(max_length= 200, blank=True)
    sem = models.CharField(max_length= 200, blank=True)
    grade = models.CharField(max_length= 200, blank=True)
    Department = models.CharField(max_length= 200, blank=True)
    start_date = models.CharField(max_length= 200, blank=True)
    end_date = models.CharField(max_length= 200, blank=True)
    program = models.CharField(max_length=122, blank=True)
    year = models.CharField(max_length=8, blank=True)
    tx_rc = models.CharField(max_length= 200, blank=True)
    
    
    
    def __str__(self):
        return self.name