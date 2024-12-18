from django.db import models

# Create your models here.
class Defis(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    pts = models.IntegerField()
    def __str__(self):
        return f"{self.name} ({self.pts} pts)"
    
