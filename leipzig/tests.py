# coding=UTF-8

import datetime

from django.test import TestCase
from django.utils import timezone
from django.core.urlresolvers import reverse
from django.contrib.auth.models import AnonymousUser, User

from views import home, updates, programme, articles, article_single, song_wish, feedback, houses, topics, topic_single, team, partners, dictionary, phones, imprint, datenschutzerklaerung
from .models import Update, Programme, FeaturedItem, SongWish, Article, Comment, Link, Feedback, House, Topic, Setting, TeamMember
# Create your tests here.

# Under me you will find the functions which can easily create demo content.

# Article
demo_article_title = "Hello World"
demo_article_author = "Tom Wolfskämpf"
demo_article_author_country = "Germany"
demo_article_published_on = timezone.now()
demo_article_introduction = "Lorem ipsum dolor sit ameti."
demo_article_text = "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
demo_article_external_link = "http://leipzig2015is.eu"
demo_article_image_link = "http://i.imgur.com/xBHM6Ps.jpg"
demo_article_video_embed_src = 'src="https://www.youtube.com/embed/oHg5SJYRHA0"'

def create_article(title = demo_article_title, author = demo_article_author, author_country = demo_article_author_country, published_on = demo_article_published_on, introduction = demo_article_introduction, text = demo_article_text, external_link = demo_article_external_link, image_link = demo_article_image_link, video_embed_src = demo_article_video_embed_src):
    """
    This will create an article.
    """
    return Article.objects.create(title = title, author = author, author_country = author_country, published_on = published_on, introduction = introduction, text = text, external_link = external_link, image_link = image_link, video_embed_src = video_embed_src)


class HomeViewTests(TestCase):
    """
    This TestCase contains all tests of the above mentioned View
    """

    # def setUp(self):
    #     return 0

    def test_home_view__with_empty_database(self):
        """
        If the database is empty, the home page should still load properly and show appropriate messages
        """
        response = self.client.get(reverse("leipzig:home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "There is no programme available for today.")
        self.assertContains(response, "There are currently no updates.")
        self.assertContains(response, "There is no featured photo.")


class ArticleListViewTests(TestCase):
    """
    This TestCase contains all tests of the above mentioned View
    """
    # def setUp(self):
    #     return 0

    def test_article_view_with_no_articles(self):
        """
        If there are no articles the page should still load and an error message should be shown
        """
        response = self.client.get(reverse("leipzig:articles"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "There are no articles to be shown.")

    def test_article_view_with_one_article(self):
        """
        If there is an article it should be shown and the error message should not
        """
        article = create_article()
        response = self.client.get(reverse("leipzig:articles"))
        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, "There are no articles to be shown.")
        self.assertContains(response, demo_article_introduction)
        self.assertContains(response, demo_article_title)
        self.assertContains(response, demo_article_author)

    def test_article_view_with_two_articles(self):
        """
        If there are two articles they should be shown and the error message should not
        """
        article = create_article()
        article2 = create_article(title = "Say Cheese World", author = "Max Mustermann", author_country = "Switzerland", published_on = demo_article_published_on, introduction = "That's all, folks", text = demo_article_text, external_link = "", image_link = "http://i.imgur.com/i2MolXA.jpg", video_embed_src = demo_article_video_embed_src)
        response = self.client.get(reverse("leipzig:articles"))
        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, "There are no articles to be shown.")
        self.assertContains(response, demo_article_title)
        self.assertContains(response, demo_article_author)
        self.assertContains(response, demo_article_introduction)
        self.assertContains(response, demo_article_external_link)
        self.assertContains(response, "Say Cheese World")
        self.assertContains(response, "Max Mustermann")
        self.assertContains(response, "That's all, folks")
        self.assertContains(response, "Read")



class ArticleSingleViewTests(TestCase):
    """
    This TestCase contains all tests of the above mentioned View
    """
    def setUp(self):
        """
        This function creates an article in the database before each test runs.
        """
        self.article = create_article()

    def test_article_single_view_with_one_article(self):
        """
        The article should be shown including all relevant information.
        """
        response = self.client.get(reverse("leipzig:article_single", args = [self.article.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, demo_article_title)
        self.assertContains(response, demo_article_author)
        self.assertContains(response, demo_article_author_country)
        self.assertContains(response, demo_article_introduction)
        self.assertContains(response, demo_article_text)
        self.assertContains(response, demo_article_image_link)
        self.assertContains(response, demo_article_video_embed_src)

    def test_article_single_view_with_two_articles(self):
        """
        The article should be shown including all relevant information even if there are multiple articles in the database.
        """
        article2 = create_article(title = "Say Cheese World", author = "Max Mustermann", author_country = "Switzerland", published_on = demo_article_published_on, introduction = "That's all, folks", text = demo_article_text, external_link = "", image_link = "http://i.imgur.com/i2MolXA.jpg", video_embed_src = demo_article_video_embed_src)
        response = self.client.get(reverse("leipzig:article_single", args = [self.article.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, demo_article_title)
        self.assertContains(response, demo_article_author)
        self.assertContains(response, demo_article_author_country)
        self.assertContains(response, demo_article_introduction)
        self.assertContains(response, demo_article_text)
        self.assertContains(response, demo_article_image_link)
        self.assertContains(response, demo_article_video_embed_src)


class TopicViewTests(TestCase):
    """
    This TestCase contains all tests of the above mentioned View
    """
    # def setUp(self):
    #     return 0

    def test_topic_view_with_no_topics(self):
        """
        If there are no topics the page should still load and an error message should be shown
        """
        response = self.client.get(reverse("leipzig:topics"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "There are no topics to be shown.")


class ProgrammeTestView(TestCase):
    """
    This TestCase contains all tests of the above mentioned View
    """

    def test_programme_view_with_no_programme(self):
        """
        If there are no programmes the page should still load and an error message should be shown
        """
        response = self.client.get(reverse("leipzig:programme"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "There is no programme to be shown.")


class UpdatesTestView(TestCase):
    """
    This TestCase contains all tests of the above mentioned View
    """

    def test_updates_view_with_no_updates(self):
        """
        If there are no updates the page should still load and an error message should be shown
        """
        response = self.client.get(reverse("leipzig:updates"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "There are no updates to be shown.")



class HouseTestView(TestCase):
    """
    This TestCase contains all tests of the above mentioned View
    """

    def test_house_view_with_no_houses(self):
        """
        If there are no houses the page should still load and an error message should be shown
        """
        response = self.client.get(reverse("leipzig:houses"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "There are no houses to be shown.")


class SongWishTestView(TestCase):
    """
    This TestCase contains all tests of the above mentioned View
    """

    def test_song_wish_view_loading(self):
        """
        When a user loads the song wish page the form should be shown
        """
        response = self.client.get(reverse("leipzig:song_wish"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Submit")

class FeedbackTestView(TestCase):
    """
    This TestCase contains all tests of the above mentioned View
    """

    def test_feedback_view_loading(self):
        """
        When a user loads the feedback page the form should be shown
        """
        response = self.client.get(reverse("leipzig:feedback"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Submit")


class TeamTestView(TestCase):
    """
    This TestCase contains all tests of the above mentioned View
    """

    def test_team_view_with_no_team(self):
        """
        When a user loads the team page with no team members in the database,
        the page should still load and show the appropriate message.
        """
        response = self.client.get(reverse("leipzig:team"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "There are no team members in the database.")



class StaticViewTests(TestCase):
    """
    This TestCase contains all tests of the above mentioned View
    """

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

    def test_imprint_view(self):
        """
        Should display the imprint.html file
        """
        response = self.client.get(reverse("leipzig:imprint"))
        self.assertEqual(response.status_code, 200)

    def test_datenschutzerklaerung_view(self):
        """
        Should display the datenschutzerklaerung.html file
        """
        response = self.client.get(reverse("leipzig:datenschutzerklaerung"))
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
