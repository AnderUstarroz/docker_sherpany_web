import pytest
from django.conf import settings
from .factories import EventFactory
from .models import Event
import re


@pytest.mark.django_db(transaction=True)
def test_adding_event(authenticated):
    sample = EventFactory.build()
    assert Event.objects.count() == 0
    result = authenticated.post('/events/add/', {
        'date': sample.date.strftime('%Y-%m-%d %H:%M:%S'),
        'title': sample.title,
        'description': sample.description,
    })

    assert Event.objects.count() == 1
    assert result.status_code == 302


@pytest.mark.django_db(transaction=True)
def test_user_cannot_edit_other_people_events(authenticated):
    # Create event by Random user
    event = EventFactory.create()

    authenticated.post('/events/%s/' % event.pk, {
        'date': event.date.strftime('%Y-%m-%d %H:%M:%S'),
        'title': 'some other text',
        'description': 'some text',
    })
    assert event.title == Event.objects.get(pk=event.pk).title


@pytest.mark.django_db(transaction=True)
def test_user_can_edit_his_events(authenticated):
    # Create event by Random user
    event = EventFactory.create(user=authenticated.user)
    authenticated.post('/events/%s/' % event.pk, {
        'date': event.date.strftime('%Y-%m-%d %H:%M:%S'),
        'title': 'title has been updated',
        'description': 'some text',
    })
    assert 'title has been updated' == Event.objects.get(pk=event.pk).title


@pytest.mark.django_db(transaction=True)
def test_pagination(authenticated):
    # Create 6 but only 5 are displayed
    EventFactory.create_batch(38)
    result = authenticated.get('/events/')
    assert len(re.findall("/events/\d+/", str(result.content))) == settings.PAGINATION