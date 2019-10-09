from datetime import datetime

from django.db import models


# Create your models here.
class RankList(models.Model):
    creator = models.ForeignKey('users.User', null=False, related_name='creator', on_delete=models.CASCADE)
    entry = models.ForeignKey('entries.Entries', null=False, related_name='entry', on_delete=models.CASCADE)
    opinionname = models.CharField(unique=True, max_length=50, null=False)
    positionindex = models.IntegerField(null=False)
    created_at = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return str(self.entry)

    def get_date(self):
        time = datetime.now()
        if self.created_at.day == time.day:
            return str(time.hour - self.created_at.hour) + " hours ago"
        else:
            if self.created_at.month == time.month:
                return str(time.day - self.created_at.day) + " days ago"
            else:
                if self.created_at.year == time.year:
                    return str(time.month - self.created_at.month) + " months ago"
        return self.created_at
