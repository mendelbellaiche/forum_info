from django.contrib import admin
from .models import Ticket, Comment


class TicketAdmin(admin.ModelAdmin):
    list_display = ('ticket_title', 'ticket_contenu_overview', 'pub_date')
    list_filter = ('ticket_title', )
    ordering = ('pub_date',)
    search_fields = ('ticket_title', 'ticket_content')

    fieldsets = (
        # Fieldset 1 : meta-info (titre, auteur…)
        ('Général', {
            'classes': ['collapse', ],
            'fields': ('ticket_title', 'pub_date')
        }),
        # Fieldset 2 : contenu de l'article
        ('Content of Ticket', {
            'description': '',
            'fields': ('ticket_content',)
        }),
    )

    def ticket_contenu_overview(self, content):

        text = content.ticket_content[0:40]
        if len(content.ticket_content) > 40:
            return '%s…' % text
        else:
            return text

    ticket_contenu_overview.short_description = 'Overview of Ticket'


class CommentAdmin(admin.ModelAdmin):
    list_display = ('comment_title', 'comment_contenu_overview', 'pub_date')
    list_filter = ('comment_title', )
    ordering = ('pub_date',)
    search_fields = ('comment_title', 'comment_content')

    fieldsets = (
        # Fieldset 1 : meta-info (titre, auteur…)
        ('Général', {
            'classes': ['collapse', ],
            'fields': ('comment_title', 'pub_date')
        }),
        # Fieldset 2 : contenu de l'article
        ('Content of Ticket', {
            'description': '',
            'fields': ('comment_content',)
        }),
    )

    def comment_contenu_overview(self, content):

        text = content.comment_content[0:40]
        if len(content.comment_content) > 40:
            return '%s…' % text
        else:
            return text

    comment_contenu_overview.short_description = 'Overview of comment'


admin.site.register(Ticket, TicketAdmin)
admin.site.register(Comment, CommentAdmin)
