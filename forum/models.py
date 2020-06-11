from django.db import models
from django.utils import timezone

class Ticket(models.Model):
    ticket_title = models.CharField(max_length=150)
    ticket_content = models.TextField()
    pub_date = models.DateTimeField('date published', default=timezone.now)

    def __str__(self):
        return self.ticket_title


class Comment(models.Model):
    comment_title = models.CharField(max_length=150)
    comment_content = models.TextField()
    pub_date = models.DateTimeField('date published', default=timezone.now)
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment_title



