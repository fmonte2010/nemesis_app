from flask import url_for
from flask_login import UserMixin
from slugify import slugify
from sqlalchemy.exc import IntegrityError

from .customer import Customer_model
from app import db
import datetime


class Contact_model(db.Model):

    __tablename__ = 'n_nemesis_n_contact_model'

    name = db.Column(db.String(45), nullable=False)
    surname = db.Column(db.String(45), nullable=False)
    taxCode = db.Column(db.String(16), unique=True, nullable=True)
    address = db.Column(db.String(256), unique=True, nullable=False)
    phone = db.Column(db.String(45), nullable=True)
    certification = db.Column(db.String(45), unique=True, nullable=False)
    user = db.Column(db.String(16), unique=True, nullable=True)
    customerid = db.Column(db.String(20), db.ForeignKey('customer.id', ondelete='SET NULL'))
    id = db.Column(db.String(20), primary_key=False)
    version = db.Column(db.Integer, nullable=True)
    created = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def __repr__(self):
        return f'<Contact_model {self.Id}>'

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
        return Contact_model.query.get(id)

    @staticmethod
    def get_by_name(name):
        return Contact_model.query.filter_by(name=name).first()

    @staticmethod
    def get_all():
        return Contact_model.query.all()

    @staticmethod
    def all_paginated(page=1, per_page=20):
        return Contact_model.query.order_by(Contact_model.created.asc()).\
            paginate(page=page, per_page=per_page, error_out=False)
