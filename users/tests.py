from .views import users
from django.test import TestCase
from rest_framework.test import APIRequestFactory

class UsersTest(TestCase):
    def testRequestFromAPI(self):
        STATUS_CODE_APPROVED = int(200)

        factory = APIRequestFactory()
        request = factory.get('/users/')
        response = users(request)

        self.assertEqual(response.status_code, STATUS_CODE_APPROVED)