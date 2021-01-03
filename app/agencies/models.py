from flask import url_for
from flask_login import UserMixin
from slugify import slugify
from sqlalchemy.exc import IntegrityError

from app import db
import datetime

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('blog_user.id', ondelete='CASCADE'), nullable=False)
    title = db.Column(db.String(256), nullable=False)
    title_slug = db.Column(db.String(256), unique=True, nullable=False)
    content = db.Column(db.Text)
    created = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    image_name = db.Column(db.String(256))
    comments = db.relationship('Comment', backref='post', lazy=True, cascade='all, delete-orphan', order_by='asc(Comment.created)')

    def __repr__(self):
        return f'<Post {self.title}>'

    def save(self):
        if not self.id:
            db.session.add(self)
        if not self.title_slug:
            self.title_slug = slugify(self.title)
        saved = False
        count = 0
        while not saved:
            try:
                db.session.commit()
                saved = True
            except IntegrityError:
                db.session.rollback()  # Añade esta línea
                db.session.add(self)   # y esta
                count += 1
                self.title_slug = f'{slugify(self.title)}-{count}'

# Comentado para mejoras...
#   def public_url(self):
#       return url_for('public.show_post', slug=self.title_slug)

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_by_id(id):
        return Post.query.get(id)

    @staticmethod
    def get_by_slug(slug):
        return Post.query.filter_by(title_slug=slug).first()

    @staticmethod
    def get_all():
        return Post.query.all()

    @staticmethod
    def all_paginated(page=1, per_page=20):
        return Post.query.order_by(Post.created.asc()).\
            paginate(page=page, per_page=per_page, error_out=False)


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('blog_user.id', ondelete='SET NULL'))
    user_name = db.Column(db.String(128))
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)
    content = db.Column(db.Text)
    created = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def __init__(self, content, user_id=None, user_name=user_name, post_id=None):
        self.content = content
        self.user_id = user_id
        self.user_name = user_name
        self.post_id = post_id

    def __repr__(self):
        return f'<Comment {self.content}>'

    def save(self):
        if not self.id:
            db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_by_post_id(post_id):
        return Comment.query.filter_by(post_id=post_id).all()


class Agency_model(db.Model):

    __tablename__ = 'n_nemesis_n_agency_model'

    name = db.Column(db.String(300), nullable=True)
    address = db.Column(db.String(200), nullable=True)
    managerId = db.Column(db.String(20), unique=True, nullable=True)
    vat = db.Column(db.String(16), nullable=True)
    email = db.Column(db.String(256), unique=True, nullable=False)
    phone = db.Column(db.String(45), nullable=True)
    certification = db.Column(db.String(45), unique=True, nullable=False)
    customerid = db.Column(db.String(20), db.ForeignKey('customer.id', ondelete='SET NULL'))
    moreInfo = db.Column(db.String(250), nullable=True)
    id = db.Column(db.String(20), primary_key=False)
    version = db.Column(db.Integer, nullable=True)
    created = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def __repr__(self):
        return f'<Agency_model {self.Id}>'

    def save(self):
        if not self.id:
            db.session.add(self)
        saved = False
        count = 0
        while not saved:
            try:
                db.session.commit()
                saved = True
            except IntegrityError:
                db.session.rollback()  # Añade esta línea
                db.session.add(self)   # y esta
                count += 1

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_by_id(id):
        return Agency_model.query.get(id)

    @staticmethod
    def get_by_name(name):
        return Agency_model.query.filter_by(name=name).first()

    @staticmethod
    def get_all():
        return Agency_model.query.all()

    @staticmethod
    def all_paginated(page=1, per_page=20):
        return Agency_model.query.order_by(Agency_model.created.asc()).\
            paginate(page=page, per_page=per_page, error_out=False)
