from datetime import datetime

from django.db import models, connection


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

    def are_friends(self):
        friends = 0
        query = """
            SELECT CASE WHEN EXISTS (
            SELECT * FROM ranklist_ranklist, buddylist_buddylist
            WHERE (ranklist_ranklist.creator_id = buddylist_buddylist.buddy1_id AND buddylist_buddylist.buddy2_id = 11 /*user_id*/)
            OR (ranklist_ranklist.creator_id = buddylist_buddylist.buddy2_id AND buddylist_buddylist.buddy1_id = 11 /*user_id*/)        
            OR (ranklist_ranklist.creator_id = 11 /*user_id*/)
            )
            THEN CAST(1 AS BIT)
            ELSE CAST(0 AS BIT) 
            END"""
        with connection.cursor() as cursor:
            cursor.execute(query)
            if cursor.rowcount != 0:
                result = cursor.fetchone()

                if result is not None:
                    friends = result[0]

        return friends
