import factory

from profiles.models import Profile


class ProfileFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Profile

    name = factory.Faker("first_name")
    surname = factory.Faker("last_name")
    body = factory.Faker("paragraph")
    birthday = factory.Faker("date_of_birth")
