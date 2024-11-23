import factory
from factory.fuzzy import FuzzyChoice

from DjangoPolls.factories import UserFactory
from legislations.factories import LegislationFactory
from profiles.factories import ProfileFactory
from reports.models import Report, Suspect, Charge


class ReportFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Report

    type = FuzzyChoice([choice[0] for choice in Report.REPORT_TYPES])
    title = factory.Faker("sentence")
    body = factory.Faker("paragraph")
    created_by = factory.SubFactory(UserFactory)


class SuspectFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Suspect

    report = factory.SubFactory(ReportFactory)
    profile = factory.SubFactory(ProfileFactory)
    is_warrant = factory.Faker("boolean")
    is_processed = factory.Faker("boolean")
    is_plead_guilty = factory.Faker("boolean")


class ChargeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Charge

    legislation = factory.SubFactory(LegislationFactory)
    suspect = factory.SubFactory(SuspectFactory)
