import datetime

from django.test import TestCase
from django.utils import timezone
from django.core.urlresolvers import reverse
from django.contrib.auth.models import AnonymousUser, User

from views import *
from .models import *
# Create your tests here.


class HomeViewTests(TestCase):

    def setUp(self):
        return 0

    def test_home_view__with_empty_database(self):
        """
        If the database is empty, the home page should still load properly and show appropriate messages.
        """
        response = self.client.get(reverse("leipzig:home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "There is no programme available for today.")
        self.assertContains(response, "There are currently no updates.")
        self.assertContains(response, "There is no photo of the day.")


class ArticleViewTests(TestCase):
    def setUp(self):
        return 0

    def test_article_view_with_no_articles(self):
        """
        If there are no articles the page should still load and an error message should be shown.
        """
        response = self.client.get(reverse("leipzig:articles"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "There are no articles to be shown.")
