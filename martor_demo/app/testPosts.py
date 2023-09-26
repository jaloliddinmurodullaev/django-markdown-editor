from django.test import TestCase
from app.models import Post

class TestPostCase(TestCase):
    def testPost(self):
        post = Post(title="My Title", description="Kali", wiki="Post Body")
        self.assertEqual(post.title, "My Title")
        self.assertEqual(post.description, "Kali")
        self.assertEqual(post.wiki, "Post Body")