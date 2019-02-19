import unittest
from app.models import Comment, User, Blog
from app import db

class TestCommentModel(unittest.TestCase):

    def setUp(self):
        self.user_anum = User(username = "anum", password = "anum123", email="anum@yahoo.com")
        self.new_blog = Blog(title="food", body = "I love food", user_id =self.user_anum.id )
        self.new_comment=Comment(feedback="good post", user_id=self.user_anum.id,blog_id=self.new_blog.id)

    def tearDown(self):
        Blog.query.delete()
        User.query.delete()
        Comment.query.delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_comment, Comment))    

    def test_check_instance_variables(self):
        
        self.assertEquals(self.new_comment.feedback, 'good post')
        self.assertEquals(self.new_comment.user_id,self.user_anum.id)
        self.assertEquals(self.new_comment.blog_id, self.new_blog.id) 
    
    def test_save_blog(self):
        self.new_comment.save_comment()
        self.assertTrue(len(Comment.query.all())>0)

    def test_get_blogs(self):

        self.new_comment.save_comment()
        comments = Comment.get_comments()
        self.assertTrue(len(comments)==1)