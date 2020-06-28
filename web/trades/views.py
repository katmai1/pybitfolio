from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic

from .models import Trades


class IndexView(generic.ListView):
    template_name = 'trades/index.html'
    context_object_name = 'trades_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Trades.objects.all()
    

def detail(request, trade_id):
    return HttpResponse("You're looking at question %s." % trade_id)

def results(request, trade_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % trade_id)

def vote(request, trade_id):
    return HttpResponse("You're voting on question %s." % trade_id)