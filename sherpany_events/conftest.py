from user.factories import UserFactory
from django.contrib.auth import login, authenticate
from django.test import Client
import pytest


@pytest.mark.django_db(transaction=True)
@pytest.fixture
def authenticated():
    client = Client()
    client.user = UserFactory.create()
    client.user.set_password('hello')
    client.user.save()
    client.login(username=client.user.email, password='hello')
    return client