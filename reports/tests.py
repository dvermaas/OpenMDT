from django.test import TestCase
from django.contrib.auth.models import User

from reports.models import Report


# Create your tests here.
class ReportTestCase(TestCase):
    def setUp(self):
        user = User.objects.create_user("testuser", "<EMAIL>", "<PASSWORD>")
        Report.objects.create(title="Test Report", created_by=user)

    def TestIfReportExists(self):
        """Animals that can speak are correctly identified"""
        report = Report.objects.first()
        self.assertEqual(report.title, "Test Report")
