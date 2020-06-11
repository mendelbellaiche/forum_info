from django.shortcuts import render

from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Ticket, Comment
from .forms import TicketForm, CommentForm


def index(request):
    latest_ticket_list = Ticket.objects.order_by('-pub_date')[:5]
    context = {'latest_ticket_list': latest_ticket_list}
    return render(request, 'forum/index.html', context)


def ticket(request):
    if request.method == 'POST':
        ticket_form = TicketForm(request.POST)

        if ticket_form.is_valid():
            ticket_form.save()
            return HttpResponseRedirect(request.path)
    else:
        ticket_form = TicketForm()
    context = {'ticketForm': ticket_form}
    return render(request, 'forum/ticket.html', context)


def detail(request, ticket_id):
    try:
        ticket = Ticket.objects.get(pk=ticket_id)
        comments = ticket.comment_set.all()

        if request.method == 'POST':
            comment_form = CommentForm(request.POST)

            if comment_form.is_valid():
                comment_obj = comment_form.save(commit=False)
                comment_obj.ticket_id = ticket_id
                comment_obj.save()
                return HttpResponseRedirect(request.path)
        else:
            comment_form = CommentForm()

    except Ticket.DoesNotExist:
        raise Http404("Question does not exist")
    context = {'ticket': ticket, 'comments': comments, 'commentForm': comment_form}
    return render(request, 'forum/detail.html', context)
