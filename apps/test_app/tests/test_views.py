from django.test import TestCase
from django.core.urlresolvers import resolve
from apps.test_app.views import test_app


class TestPageTest(TestCase):

    def test_root_url_resolves_to_test_page(self):
        """
        Check for can resolve main page.
        """
        found = resolve('/test/')
        self.assertEqual(found.func, test_app)

    def test_correct_main_page_template(self):
        """
        See what template used for main page
        """
        response = self.client.get('/test/')
        self.assertTemplateUsed(response, 'test.html')
