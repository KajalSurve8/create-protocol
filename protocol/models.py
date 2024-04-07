from django.db import models

# Create your models here.
class FormulationType(models.Model):
    fid = models.AutoField(auto_created=True, primary_key=True)
    ftype = models.CharField(max_length=30)
    
