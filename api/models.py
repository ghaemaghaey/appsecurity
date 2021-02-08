from django.db import models

# Create your models here.
class data(models.Model):
    status = models.CharField(max_length=5)
    def __str__(self):
        return self.status