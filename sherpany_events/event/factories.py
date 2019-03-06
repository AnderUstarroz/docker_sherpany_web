import factory
from .models import Event
from django.utils import timezone


class EventFactory(factory.django.DjangoModelFactory):

    id = factory.Sequence(lambda n: n)
    date = factory.LazyFunction(timezone.now)
    title = factory.Faker('sentence', nb_words=4)
    description = factory.Faker('text')

    class Meta:
        model = Event
