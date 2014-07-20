from django.core.urlresolvers import reverse
from django.test import TestCase


class HomePageViewTest(TestCase):
    url_name = "home"

    def test_home_page_loads_correct_template(self):
        response = self.client.get(reverse(self.url_name))
        self.assertTemplateUsed(response, 'home.html')

    def test_home_page_returns_200(self):
        response = self.client.get(reverse(self.url_name))
        self.assertEquals(200, response.status_code)


class RegisterViewTest(TestCase):
    url_name = "register"

    def test_register_page_loads_correct_template(self):
        response = self.client.get(reverse(self.url_name))
        self.assertTemplateUsed(response, 'register.html')

    def test_register_page_returns_200(self):
        response = self.client.get(reverse(self.url_name))
        self.assertEquals(200, response.status_code)