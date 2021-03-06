import factory
from .models import User


class UserFactory(factory.django.DjangoModelFactory):

    id = factory.Sequence(lambda n: n)
    email = factory.Faker('email')
    password = factory.Faker('password')

    class Meta:
        model = User
