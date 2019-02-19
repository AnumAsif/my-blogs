from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import Required, Email

class CreateBlog(FlaskForm):
    title = StringField('Blog Title', validators=[Required()])
    subtitle=StringField('Subtitle',validators=[Required()])
    body = TextAreaField('Blog',validators=[Required()])
    submit= SubmitField('Add Blog')

class AddComment(FlaskForm):
    comment = StringField('Comment', validators=[Required()])
    submit = SubmitField('Add Comment') 

class EditBlog(FlaskForm):
    body = TextAreaField('Blog',validators=[Required()])
    submit= SubmitField('Edit Blog')    

class SubscribeForm(FlaskForm):
    email = StringField('Your Email Address',validators=[Required(),Email()])
    submit= SubmitField('Subscribe')  