from django.test import TestCase
from django.shortcuts import reverse


class ResponseTest(TestCase):
    def test_root(self):
        response = self.client.get(reverse("landing_page"))
        self.assertEqual(response.status_code, 200)

    # def test_leads(self):
    #     response = self.client.get(reverse("landing"))
    #     self.assertEqual(response.status_code, 200)
