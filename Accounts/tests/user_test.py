import os
import django
from django.test.utils import get_runner
from django.conf import settings

# os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'  # Adjust to your settings module
django.setup()

import uuid
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken
from Accounts.models import User  # Adjust 'Accounts' to the actual app name

class TestUserSetup(TestCase):

    def setUp(self):
        self.client = APIClient()
        fake_email = f"{str(uuid.uuid4())}@example.com"
        self.user = User.objects.create(
            email=fake_email,
        )
        refresh = RefreshToken.for_user(self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {str(refresh.access_token)}')

    def test_example(self):
        # Example test
        response = self.client.get('/your-endpoint/')  # Replace with actual endpoint
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    TestRunner = get_runner(settings)
    test_runner = TestRunner()
    failures = test_runner.run_tests(["Accounts.tests.user_test"])
    if failures:
        exit(1)
