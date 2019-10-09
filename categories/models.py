from django.db import models

# Create your models here.
class Categories(models.Model):
    name =  models.CharField(unique=True, max_length=50, null=False)

    def __str__(self):
        return str(self.name)