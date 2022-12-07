from django.contrib.auth import get_user_model
from django.test import TestCase
from app_news.models import News, Commentary, Profile, BlogPost


class NewsTestCase(TestCase):
    def setUp(self):
        News.objects.create(title="lion", description="roar")

    def test_news(self):
        lion = News.objects.get(title="lion")
        self.assertEqual(lion.description, 'roar')


class CommentaryTestCase(TestCase):
    def setUp(self):
        News.objects.create(title="lion", description="roar")
        Commentary.objects.create(user_name="lion", news_at=News.objects.get(id=1), comment="roar2")

    def test_news(self):
        lion = Commentary.objects.get(user_name="lion")
        self.assertEqual(lion.comment, 'roar2')


class ProfileTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        get_user_model().objects.create(username='John')

    def test_profile(self):
        profile = get_user_model().objects.last()
        self.assertEqual(profile.username, 'John')


class BlogPostTestCase(TestCase):
    def setUp(self):
        get_user_model().objects.create(username='John')
        BlogPost.objects.create(description="roar", user=get_user_model().objects.last())

    def test_news(self):
        lion = BlogPost.objects.get(description="roar")
        self.assertEqual(lion.description, 'roar')
