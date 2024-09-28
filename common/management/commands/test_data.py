from django.core.management.base import BaseCommand

from legislations.factories import LegislationFactory
from profiles.factories import ProfileFactory
from reports.factories import ReportFactory


class Command(BaseCommand):
    help = "Generate test data using factories"

    def add_arguments(self, parser):
        parser.add_argument(
            "--records",
            type=int,
            default=10,
            help="Number of records to create for each model",
        )

    def handle(self, *args, **kwargs):
        num_records = kwargs["records"]

        # Generate test data
        for _ in range(num_records):
            ReportFactory()
            ProfileFactory()
            LegislationFactory()

        self.stdout.write(
            self.style.SUCCESS(
                f"Successfully created {num_records} records for each model."
            )
        )
