from flask import render_template, request, redirect, url_for
from . import main
from app import db
from ..requests import get_quotes
from flask_login import login_required, current_user
from .forms import CreateBlog, AddComment
from ..models import User,Blog,Comment
@main.route('/')
def index():
    new_quote = get_quotes()
    blogs = Blog.query.all()
    users = User.query.all()
    return render_template('index.html', new_quote=new_quote, blogs=blogs, users=users)

@main.route('/blog/<id>',methods=["get","post"])
def blog(id):
    comment_form = AddComment()
    blog = Blog.query.filter_by(id=id).first()
    if comment_form.validate_on_submit():
        feedback = comment_form.comment.data
        comment= Comment(feedback=feedback,user_id=current_user.id,blog_id=id)
        db.session.add(comment)
        db.session.commit()
        comments=Comment.query.filter_by(blog_id=id).all()
        return render_template("blog.html", blog=blog, comments=comments,comment_form=comment_form)
    comments=Comment.query.filter_by(blog_id=id)
    return render_template("blog.html", blog=blog,comment_form=comment_form,comments=comments) 

@main.route('/addblog', methods=["get","post"]) 
def add_blog():
    blogform = CreateBlog() 
    
    if blogform.validate_on_submit():
        # user= User.query.filter_by(username=current_user.username).first()
        # userid=user.id

        title=blogform.title.data
        subtitle=blogform.subtitle.data
        body=blogform.body.data
        new_blog = Blog(title=title,subtitle=subtitle,body=body,user_id=current_user.id)
        db.session.add(new_blog)
        db.session.commit()
        # message="Your blog has been added successfully!!"
        return redirect(url_for('main.index'))
    return render_template('create_blog.html', blog_form=blogform)
    

@main.route('/profile/<uname>')
def profile(uname):
    return render_template('profile/profile.html')    

@main.route('/deleteComment/<int:commentid>/<int:blogid>',methods=["get","post"])
def deleteComment(commentid,blogid):
    comment= Comment.query.filter_by(id=commentid).first()
    db.session.delete(comment)
    db.session.commit()
    return redirect(url_for("main.blog",id=blogid))
