
from django.utils.translation import ugettext_lazy as _
from django.forms import ModelForm
from .models import Ticket, Comment


class TicketForm(ModelForm):
    class Meta:
        model = Ticket
        fields = ['ticket_title', 'ticket_content']
        labels = {
            'ticket_title': _('Title'),
            'ticket_content': _('Message'),
        }


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['comment_title', 'comment_content']
        labels = {
            'comment_title': _('Title'),
            'comment_content': _('Content'),
        }
