

from django.db import models


chc = [
    ('SDE','Software Developer'),
    ('DA', 'Data Analyst'),
    ('ST', 'Software Tester')
    ]

chc1 = [('Employee', 'Employee'), ('Admin', 'Admin')]

class Employee(models.Model):
    id = models.IntegerField(primary_key = True)
    name = models.CharField(max_length =20)
    design = models.CharField(max_length = 20, choices = chc)
    sal = models.IntegerField()
    age = models.IntegerField(null = True)
    pos = models.CharField(max_length = 15, choices = chc1)
    pswd = models.CharField(max_length = 15, default = 'vs')
  

    def __str__(self):
        return str(self.id) + " - " + self.name


    
    
