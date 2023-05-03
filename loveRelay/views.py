from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic import ListView, DetailView
from .models import Gift, Message, Bottle

# Create your views here.

def index(request):
    return HttpResponse("love relay")

class GiftListView(ListView):
    model = Gift
    template_name = 'gift_list.html'
    context_object_name = 'gifts'

class GiftDetailView(DetailView):
    model = Gift
    template_name = 'gift_detail.html'
    context_object_name = 'gift'

class MessageListView(ListView):
    model = Message
    template_name = 'message_list.html'
    context_object_name = 'messages'

class MessageDetailView(DetailView):
    model = Message
    template_name = 'message_detail.html'
    context_object_name = 'message'

class BottleListView(ListView):
    model = Bottle
    template_name = 'bottle_list.html'
    context_object_name = 'bottles'

class BottleDetailView(DetailView):
    model = Bottle
    template_name = 'bottle_detail.html'
    context_object_name = 'bottle'
