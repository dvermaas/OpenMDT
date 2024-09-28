import factory

from legislations.models import Legislation


class LegislationFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Legislation

    title = factory.Faker("sentence")
    description = factory.Faker("paragraph")
    time = factory.Faker("random_int")
    fine = factory.Faker("random_int")
    type = factory.Iterator(
        [choice[0] for choice in Legislation._meta.get_field("type").choices]
    )
