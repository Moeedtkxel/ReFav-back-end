from django.db import models

# Create your models here.
class SubCategories(models.Model):
    name =  models.CharField(unique=True, max_length=50, null=False)
    parent_category = models.ForeignKey('categories.Categories', null=False, related_name='parent_category', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)