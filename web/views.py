from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Message

# Create your views here.
class MessageList(ListView):
    model = Message

class MessageDetail(DetailView):
    model = Message

class MessageCreate(CreateView):
    model = Message
    fields = '__all__'
    success_url = reverse_lazy('mag_list')