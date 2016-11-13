import datetime
from django.test import TestCase
from .models import Post

class MainPageTest(TestCase):
	fixtures = ['core_views_testdata.json']
	def test_main_page(self):
		resp = self.client.get('/')
		self.assertEqual(resp.status_code, 200)
		#self.assertTrue('posts' in resp.context)
		#self.assertEqual([post.pk for post in resp.context['posts']], [1])