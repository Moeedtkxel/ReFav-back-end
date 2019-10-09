from django.db import models


# Create your models here.
class BuddyList(models.Model):
    buddy1 = models.ForeignKey('users.User', null=False, related_name='buddy1', on_delete=models.CASCADE)
    buddy2 = models.ForeignKey('users.User', null=False, related_name='buddy2', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)
