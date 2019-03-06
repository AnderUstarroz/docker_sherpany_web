from .models import Event
from django import forms
from django.core.exceptions import ValidationError


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['date', 'title', 'description']


class EditEventForm(EventForm):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        self.id = kwargs.pop('id', None)
        super().__init__(*args, **kwargs)

    def clean(self):
        if self.user.pk != self.id:
            raise ValidationError('Only the owner can edit events')

        return self.cleaned_data