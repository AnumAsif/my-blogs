import unittest
from app.models import User, Blog, Comment
from app import db

class BlogModelTest(unittest.TestCase):

    def setUp(self):
        self.user_anum = User(username = "anum", password = "anum123", email="anum@yahoo.com")
        self.new_blog = Blog(title="food", body = "I love food", user_id =self.user_anum.id )

    def tearDown(self):
        Blog.query.delete()
        User.query.delete()
   

   
    def test_instance(self):
        self.assertTrue(isinstance(self.new_blog, Blog))

    def test_check_instance_variables(self):
        self.assertEquals(self.new_blog.title, 'food')
        self.assertEquals(self.new_blog.body,"I love food")
        self.assertEquals(self.new_blog.user_id, self.user_anum.id) 

    def test_save_blog(self):
        self.new_blog.save_blog()
        self.assertTrue(len(Blog.query.all())>0)

    def test_get_blogs(self):

        self.new_blog.save_blog()
        blogs = Blog.get_blogs()
        self.assertTrue(len(blogs)==1)

