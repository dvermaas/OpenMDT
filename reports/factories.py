import factory

from DjangoPolls.factories import UserFactory
from reports.models import Report


class ReportFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Report

    title = factory.Faker("sentence")
    body = factory.Faker("paragraph")
    created_by = factory.SubFactory(UserFactory)
