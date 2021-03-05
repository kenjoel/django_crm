from django.test import TestCase
from django.shortcuts import reverse


class TemplateTest(TestCase):
    def test_root(self):
        response = self.client.get(reverse("landing_page"))
        self.assertTemplateUsed(response, "landing.html")

    # def test_leads(self):
    #     response = self.client.get(reverse("details"))
    #     self.assertTemplateUsed(response, "details.html")
