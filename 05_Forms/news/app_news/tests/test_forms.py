from django.test import TestCase
from app_news.forms import NewsForm, CommentaryForm, AuthForm, AuthCommentaryForm, ExtendedRegisterForm, \
    PostFileForm, UploadBlogForm


class TestNewsForm(TestCase):
    def test_empty_form(self):
        form = NewsForm()
        self.assertIn("title", form.fields)
        self.assertIn("description", form.fields)


class TestCommentaryForm(TestCase):
    def test_empty_form(self):
        form = CommentaryForm()
        self.assertIn("user_name", form.fields)
        self.assertIn("news_at", form.fields)
        self.assertIn("comment", form.fields)


class TestAuthCommentaryForm(TestCase):
    def test_empty_form(self):
        form = AuthCommentaryForm()
        self.assertIn("news_at", form.fields)
        self.assertIn("comment", form.fields)


class TestExtendedRegisterForm(TestCase):
    def test_empty_form(self):
        form = ExtendedRegisterForm()
        self.assertIn("username", form.fields)
        self.assertIn("first_name", form.fields)
        self.assertIn("last_name", form.fields)
        self.assertIn("email", form.fields)
        self.assertIn("password1", form.fields)
        self.assertIn("password2", form.fields)

