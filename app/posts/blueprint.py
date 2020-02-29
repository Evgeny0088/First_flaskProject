from flask import Blueprint
from flask import render_template
from models import Post, Tag, Block
from block import *
from flask import request
from flask import redirect
from flask import url_for
from flask import abort
from app import db
from flask_paginate import Pagination, get_page_parameter
from flask_security import login_required, logout_user
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
import re

posts = Blueprint('posts',__name__,template_folder='templates')

class PostForm(Form):
    title = TextField('Name')
    body = TextAreaField('Content')

#http://localhost/blog/create
@posts.route('/create', methods=["POST","GET"])
@login_required
def create_post():
    if request.method=="POST":
        title = request.form['title']
        body = request.form['body']
        if title and body:
            try:
                post=Post(title=title,body=body)
                db.session.add(post)
                db.session.commit()
            except:
                print('Something is wrong')
            return redirect(url_for('posts.index'))
    form = PostForm()
    return render_template('posts/create_post.html', form = form)

@posts.route('/<slug>/edit/',methods=['POST','GET'])
@login_required
def edit_post(slug):
    post=Post.query.filter(Post.slug==slug).first_or_404()
    if request.method=='POST':
        form=PostForm(formdata=request.form,obj=post)
        form.populate_obj(post)
        db.session.commit()
        return redirect(url_for('posts.post_detail',slug=post.slug))
    form=PostForm(obj=post)
    return render_template('posts/edit_post.html',post=post,form=form)

#http://localhost/blog/
@posts.route('/')
def index():
    q=request.args.get('q')
    page=request.args.get('page')
    if page and page.isdigit():
        page=int(page)
    else:
        page=1
    if q:
        posts=Post.query.filter(Post.title.contains(q)|Post.body.contains(q)) #basequery object!
    else:
        posts = Post.query.order_by(Post.created.desc())
    pages=posts.paginate(page=page,per_page=5)
    return render_template('posts/index.html',pages=pages)

@posts.route('/blockchain/')
def blockchain():
    q=request.args.get('q')
    page = request.args.get('page',type = int, default = 1)
    if q:
        blocks = Block.query.filter(Block.name.containts(q)|Block.to_whom.contains(q))
    else:
        blocks = Block.query.order_by(Block.id.desc())
    pages = blocks.paginate(page = page, per_page = 5)
    return render_template('posts/blockchain.html',pages=pages)

@posts.route('/blockchain/create/', methods=['POST','GET'])
@login_required
def block_create():
    list = get_files()
    if not list:
        create_genesice()
        block = Block(name='Evgeny', amount=5, to_whom='Next user')
        db.session.add(block)
        db.session.commit()
        return redirect(url_for('posts.blockchain'))
    if request.method=='POST':
        lender=request.form['Lender']
        amount=request.form['Amount']
        borrower=request.form['Borrower']
        if lender and amount and borrower:
            try:
                write_block(name=lender,amount=amount,to_whom=borrower)
                block = Block(name = lender,amount = amount,to_whom = borrower)
                db.session.add(block)
                db.session.commit()
            except:
                print('something is wrong')
        return redirect(url_for('posts.blockchain'))
    return render_template('posts/block_create.html')

@posts.route('blockchain/<block>')
def block_detail(block):
    pattern='%20'
    block = re.sub(pattern,' ',block)
    flag = find_block(block=block)
    if flag==False:
         return abort(404)
    else:
        content=read_block(block)
        return render_template('posts/block_detail.html',block=block,content=content)

@posts.route('/blockchain/check_integrity')
@login_required
def check_blockchain():
    results = check_integrity()
    return render_template('posts/check_integrity.html',results = results)

#http://localhost/blog/post-slug
@posts.route('/<slug>')
def post_detail(slug):
    post=Post.query.filter(Post.slug==slug).first_or_404()
    tags=post.tags
    return render_template('posts/post_detail.html',post=post,tags=tags)

#http://localhost/blog/tag/tag_detail
@posts.route('/tag/<slug>')
def tag_detail(slug):
    tag=Tag.query.filter(Tag.slug==slug).first_or_404()
    posts=tag.posts.all()
    return render_template('posts/tag_detail.html',tag=tag,posts=posts)

@posts.route('/logout')
def user_logout():
    logout_user()
    return redirect(url_for('posts.index',next=request.url))