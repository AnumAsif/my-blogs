from . import db, login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

class User(UserMixin, db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary = True)
    username = db.Column(db.String(255), index = True)
    email = db.Column(db.String(255), unique = True, index = True)
    password_hash = db.Column(db.String(255))
    Blogs = db.relationship('Blog', backref = 'user', lazy = 'dynamic')
    @property
    def password(self):
        raise AttributeError("You cannot read the password attribute")

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'User {self.username}'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class Blog(db.Model):
    __tablename__ =  "blogs"
    
    id = db.Column(db.Integer, primary = True)
    title = db.Column(db.String(255), index = True)
    body = db.Column(db.String)
    posted_on = db.Column(db.DateTime, default = datetime.datetime.utcnow().strftime('%B %d %Y - %H:%M:%S'))
    Comments = db.relationship('Comment', backref = 'comment', lazy = 'dynamic')
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    def __repr__(self):
        return f'User {self.title}'

    def save_blog(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_blogs(cls):
        blogs = Blog.query.all()    
        return blogs

class Comment(db.Model):

    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary = True)
    feedback = db.Column(db.String, index = True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    blog_id = db.Column(db.Integer,db.ForeignKey('blogs.id'))

    def __repr__(self):
        return f'User{self.feedback}'

        

