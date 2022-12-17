from django.test import TestCase
from django.urls import reverse


class MainPageTest(TestCase):
    def test_main_page(self):
        url = reverse('main')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)


class LoginPageTest(TestCase):
    def test_main_page(self):
        url = reverse('login')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)


class LogoutPageTest(TestCase):
    def test_main_page(self):
        url = reverse('logout')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)


class AnotherLoginPageTest(TestCase):
    def test_main_page(self):
        url = reverse('another_login')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)


class RegisterPageTest(TestCase):
    def test_main_page(self):
        url = reverse('register')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)


class AccountPageTest(TestCase):
    def test_main_page(self):
        url = reverse('account')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)


class NewBlogPostPageTest(TestCase):
    def test_main_page(self):
        url = reverse('new_blog_post')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)


class UpdateBlogPageTest(TestCase):
    def test_main_page(self):
        url = reverse('update_blog')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)


class LoyaltyPageTest(TestCase):
    def test_main_page(self):
        url = reverse('loyalty_cabinet')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 403)




