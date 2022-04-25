
from django.db import models

from datetime import *



# Create your models here.

class Todo(models.Model):
    title= models.CharField(max_length=500)
    startdateplanned = models.DateField(blank=True, null=True, default=None)
    completiondateplanned = models.DateField(blank=True, null=True, default=None)
    completiondateactual = models.DateField(blank=True, null=True, default=None)
    completiondateactualtext = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.title

    def completiondateactual_text(self):
        if self.completiondateactual == None :
            self.completiondateactualtext = "~"
            self.save()   
        else:
            self.completiondateactualtext = self.completiondateactual.strftime("%Y-%m-%d")
            self.save()





 