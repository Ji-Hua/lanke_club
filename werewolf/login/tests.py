from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest

from login.views import index

class HomePageTest(TestCase):
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, index)
    
    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = index(request)
        content = response.content.decode('utf-8').strip()
        self.assertTrue(content.startswith('<html>'))
        self.assertIn('<title>烂柯游艺社</title>', content)
        self.assertTrue(content.endswith('</html>'))