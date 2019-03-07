import factory
from faker import Faker
from .models import Event
from django.utils import timezone
from user.factories import UserFactory

faker = Faker()


class EventFactory(factory.django.DjangoModelFactory):

    id = factory.Sequence(lambda n: n)
    user = factory.SubFactory(UserFactory)
    date = factory.LazyFunction(timezone.now)
    title = factory.LazyAttribute(lambda n: faker.sentence()[:20])
    description = factory.Faker('text')

    class Meta:
        model = Event
