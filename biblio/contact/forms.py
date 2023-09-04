from django import forms
from .models import Message

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ('name', 'email', 'message')


class ContactForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea())

    def clean_name(self):
        data = self.cleaned_data['name']
        if 'pawel' not in data.lower():
            raise forms.ValidationError("You must have 'pawel' in your name!")
        return data