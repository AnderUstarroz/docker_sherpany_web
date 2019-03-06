import pytest
from .factories import UserFactory
from django.test import Client
from .models import User
from .forms import RegisterForm

@pytest.mark.django_db(transaction=True)
def test_user_can_register():
    c = Client()
    email = 'someemail@google.com'
    result = c.post('/register/', {
        'email': email,
        'password1': 'somevalidpassword',
        'password2': 'somevalidpassword',
    })
    assert result.status_code == 302
    assert User.objects.filter(email=email).count() == 1


@pytest.mark.django_db(transaction=True)
def test_user_can_logout_login():
    c = Client()
    email = 'someemail@google.com'
    result = c.post('/register/', {
        'email': email,
        'password1': 'somevalidpassword',
        'password2': 'somevalidpassword'
    })
    assert '_auth_user_id' in result.client.session._session
    result = c.post('/logout/')
    assert not '_auth_user_id' in result.client.session._session
    result = c.post('/login/', {
        'email': email,
        'password1': 'somevalidpassword',
    })
    assert '_auth_user_id' in result.client.session._session


@pytest.mark.django_db(transaction=True)
def test_duplicated_emails_not_allowed():
    c = Client()
    user = UserFactory.create()
    form = RegisterForm({'email':user.email, 'password1': 'asbasd11221', 'password2': 'asbasd11221'})
    assert not form.is_valid()
    assert 'email' in form.errors
    assert 'already exists' in form.errors['email'][0]
