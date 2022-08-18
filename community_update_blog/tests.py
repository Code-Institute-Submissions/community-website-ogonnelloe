from unittest import TestCase
from django.test import Client
from .forms import CommentForm
from django.contrib.auth.models import User
from .models import CommunityUpdate
from .views import CommunityUpdatesMostRecent

class TestCommentForm(TestCase):

    def test_empty_comment(self):
        form = CommentForm({'body': ''})
        self.assertFalse(form.is_valid())

    def test_comment(self):
        form = CommentForm({'body': 'hello I\'m a comment!'})
        self.assertTrue(form.is_valid())


class TestIndexMostRecent(TestCase):

    def setUp(self):
        self.client = Client()

    def test_most_recent(self):
        response = self.client.get('')
        self.assertIsNotNone(response)
        self.assertEqual(response.status_code, 200)
        self.assertIn('Ogonnelloe', str(response.content))
        self.assertIn('recent_posts', response.context)

class TestDetailedView(TestCase):

    def setUp(self):
        self.client = Client()

    def test_detailed_view(self):
        test_community_update = CommunityUpdate(title="hello world",
                                                slug="hello-world",
                                                content="The is the test content",
                                                author= User.objects.create_user(username='me',
                                    email='me@email.com',
                                    password='imagine me and you'),
                                                status=1)
        response = self.client.get('community_updates/hello-world')
        assert test_community_update.content == response.content


class TestCommunityUpdateLike(TestCase):

    def setUp(self):
        self.client = Client()

    def test_like(self):
        response = self.client.post('like/one-more-for-luck')
        self.assertIsNotNone(response)
        self.assertEqual(response.status_code, 200)