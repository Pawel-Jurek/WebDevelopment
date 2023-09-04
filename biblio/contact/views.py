from django.shortcuts import render
from django.views.generic import DetailView, FormView
from .forms import MessageForm, ContactForm
from .models import Message

'''
class MessageView(DetailView):
    model = Message
'''

class MessageAddView(FormView):
    #form_class = MessageForm
    form_class = ContactForm    #zamiast tego to co jest w komentarzu
    template_name = 'contact/message_form.html'
    success_url = '/'

    
    #def form_valid(self, form):
    #    form.save()
    #    return super(MessageAddView, self).form_valid(form)
    