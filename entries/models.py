from datetime import datetime

from django.db import models


# Create your models here.
class Entries(models.Model):
    subcategory = models.ForeignKey('subcategories.SubCategories', null=False, related_name='subcategory',
                                    on_delete=models.CASCADE)
    name = models.CharField(unique=True, max_length=50, null=False)
    owner = models.ForeignKey('users.User', null=False, related_name='owner', on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return str(self.name)
