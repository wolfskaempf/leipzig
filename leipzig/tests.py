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


class TopicViewTests(TestCase):
    def serUp(self):
        return 0

    def test_topic_view_with_no_topics(self):
        """
        If there are no topics the page should still load and an error message should be shown
        """
        response = self.client.get(reverse("leipzig:topics"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "There are no topics to be shown.")


class ProgrammeTestView(TestCase):

    def test_programme_view_with_no_programme(self):
        """
        If there are no programmes the page should still load and an error message should be shown
        """
        response = self.client.get(reverse("leipzig:programme"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "There is no programme to be shown.")


class HouseTestView(TestCase):

    def test_house_view_with_no_houses(self):
        """
        If there are no houses the page should still load and an error message should be shown
        """
        response = self.client.get(reverse("leipzig:houses"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "There are no houses to be shown.")


class SongWishTestView(TestCase):

    def test_song_wish_view_loading(self):
        """
        When a user loads the song wish page the form should be shown
        """
        response = self.client.get(reverse("leipzig:song_wish"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Submit")

class FeedbackTestView(TestCase):

    def test_feedback_view_loading(self):
        """
        When a user loads the feedback page the form should be shown
        """
        response = self.client.get(reverse("leipzig:feedback"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Submit")



class StaticViewTests(TestCase):

    def test_dictionary_view(self):
        """
        Should display the dictionary.html file
        """
        response = self.client.get(reverse("leipzig:dictionary"))
        self.assertEqual(response.status_code, 200)

    def test_partners_view(self):
        """
        Should display the partners.html file
        """
        response = self.client.get(reverse("leipzig:partners"))
        self.assertEqual(response.status_code, 200)

    def test_phones_view(self):
        """
        Should display the phones.html file
        """
        response = self.client.get(reverse("leipzig:phones"))
        self.assertEqual(response.status_code, 200)


    # def test_home_view_with_one_session_created(self):
    #     """
    #     This test will create a session with all the standard values and see whether it shows up properly
    #     """
    #     create_session()
    #     response = self.client.get(reverse("statistics:home"))
    #     self.assertEqual(response.status_code, 200)
    #     self.assertContains(response, "Leipzig 2015")
    #     self.assertContains(response, "80th International Session of the European Youth Parliament")
    #     self.assertContains(response, "Account")
    #     self.assertContains(response, "Login")
    #     self.assertQuerysetEqual(response.context['latest_sessions_list'], ["<Session: Leipzig 2015>"])
    #
    # def test_home_view_with_two_sessions_created(self):
    #     """
    #     This test will create two sessions with all the standard values and see whether they shows up properly
    #     """
    #     create_session() #Creating Session 1
    #     create_session(name="Hiber 2015", description="4th International Forum of EYP Spain") #Creating Session 2
    #     response = self.client.get(reverse("statistics:home"))
    #     self.assertEqual(response.status_code, 200)
    #     self.assertContains(response, "Leipzig 2015")
    #     self.assertContains(response, "80th International Session of the European Youth Parliament")
    #     self.assertContains(response, "Hiber 2015")
    #     self.assertContains(response, "4th International Forum of EYP Spain")
    #     self.assertContains(response, "Account")
    #     self.assertContains(response, "Login")
    #     self.assertQuerysetEqual(response.context['latest_sessions_list'], ["<Session: Hiber 2015>", "<Session: Leipzig 2015>"])
    #
    # def test_home_view_with_one_non_public_session_created(self):
    #     """
    #     This test will create one non public session and test whether it does not show up and shows the proper message instead.
    #     """
    #     create_session(is_visible=False) #Creating Session 1
    #     response = self.client.get(reverse("statistics:home"))
    #     self.assertEqual(response.status_code, 200)
    #     self.assertContains(response, "What's going on in GA?")
    #     self.assertContains(response, "No sessions are available.")
    #     self.assertContains(response, "Account")
    #     self.assertContains(response, "Login")
    #     self.assertQuerysetEqual(response.context['latest_sessions_list'], [])
    #
    # def test_home_view_with_one_public_and_one_non_public_session_created(self):
    #     """
    #     This test will create one public and one non public session and test whether they show up and do not show up as expected.
    #     """
    #     create_session(is_visible=False) #Creating non public Session 1
    #     create_session() # Creating public Session 1
    #     response = self.client.get(reverse("statistics:home"))
    #     self.assertEqual(response.status_code, 200)
    #     self.assertContains(response, "What's going on in GA?")
    #     self.assertContains(response, "Leipzig 2015")
    #     self.assertContains(response, "80th International Session of the European Youth Parliament")
    #     self.assertContains(response, "Account")
    #     self.assertContains(response, "Login")
    #     self.assertQuerysetEqual(response.context['latest_sessions_list'], [ "<Session: Leipzig 2015>"])
