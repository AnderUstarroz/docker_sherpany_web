import pytest
from django.test import Client
from .factories import EventFactory
from .models import Event

@pytest.mark.django_db(transaction=True)
def test_adding_event():
    c = Client()
    email = 'someemail@google.com'
    sample = EventFactory.build()
    result = c.post('/events/add/', {
        'date': sample.date,
        'title': sample.title,
        'description': sample.description,
    })
    assert result.status_code == 302

