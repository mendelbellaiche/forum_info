
from django.forms import ModelForm
from .models import Ticket, Comment


class TicketForm(ModelForm):
    class Meta:
        model = Ticket
        fields = ['ticket_title', 'ticket_content']


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['comment_title', 'comment_content']
