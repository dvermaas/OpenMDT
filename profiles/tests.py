import profile

from django.test import TestCase
from django.utils import timezone
from profiles.models import Profile


# Create your tests here.
class ProfileTestCase(TestCase):
    def setUp(self):
        Profile.objects.create(
            name="john",
            surname="doe",
            birthday=timezone.now(),
            created_at=timezone.now(),
        )

    def test_profile_formats_full_name_as_string(self):
        """Animals that can speak are correctly identified"""
        profile = Profile.objects.first()
        self.assertEqual(str(profile), f"{profile.name} {profile.surname}")
