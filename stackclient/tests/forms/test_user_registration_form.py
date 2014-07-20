from django.utils.unittest.case import TestCase

from stackclient.forms import UserRegistrationForm


class UserRegistrationFormTestCase(TestCase):
    def test_that_username_is_required(self):
        form = UserRegistrationForm(data={"password": "si", "username": "", "confirmPassword": "ads"})
        self.assertFalse(form.is_valid())
        self.assertEquals("This field is required.", form.errors["username"][0])

    def test_that_password_is_required(self):
        form = UserRegistrationForm(data={"password": "", "username": "klasdjlkasjkld", "confirmPassword": "ads"})
        self.assertFalse(form.is_valid())
        self.assertEquals("This field is required.", form.errors["password"][0])

    def test_that_confirm_password_is_required(self):
        form = UserRegistrationForm(
            data={"password": "ajskjaklsd", "username": "klasdjlkasjkld", "confirmPassword": ""})
        self.assertFalse(form.is_valid())
        self.assertEquals("This field is required.", form.errors["confirmPassword"][0])

    def test_that_confirm_password_should_match(self):
        form = UserRegistrationForm(
            data={"password": "passed123", "username": "klasdjlkasjkld", "confirmPassword": "passed124"})
        self.assertFalse(form.is_valid())
        self.assertEquals("Passwords do not match.", form.errors["confirmPassword"][0])

    def test_that_if_all_are_correct_validationSucceeds(self):
        form = UserRegistrationForm(
            data={"password": "StrongPass", "username": "klasdjlkasjkld", "confirmPassword": "StrongPass"})
        self.assertTrue(form.is_valid())

    def test_that_password_is_longer_than_6(self):
        form = UserRegistrationForm(data={"password": "pass", "username": "klasdjlkasjkld", "confirmPassword": "pass"})
        self.assertFalse(form.is_valid())
        self.assertEquals("Ensure this value has at least 6 characters (it has 4).", form.errors["password"][0])

    def test_that_confirm_password_is_longer_than_6(self):
        form = UserRegistrationForm(
            data={"password": "past", "username": "klasdjlkasjkld", "confirmPassword": "past"})
        self.assertFalse(form.is_valid())
        self.assertEquals("Ensure this value has at least 6 characters (it has 4).", form.errors["confirmPassword"][0])