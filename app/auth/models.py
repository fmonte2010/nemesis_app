from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app import db

class User(db.Model, UserMixin):

    __tablename__ = 'blog_user'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(256), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __repr__(self):
        return f'<User {self.email}>'

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def save(self):
        if not self.id:
            db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return User.query.all()

    @staticmethod
    def get_by_id(id):
        return User.query.get(id)

    @staticmethod
    def get_by_email(email):
        return User.query.filter_by(email=email).first()

# Definicion de la tabla n_nemesis_acl_apppermission_model

class Acl_apppermission_model(db.Model, UserMixin):

    __tablename__ = 'n_nemesis_acl_apppermission_model'

    appId = db.Column(db.String(20), nullable=True)
    action = db.Column(db.String(200), nullable=True)
    id = db.Column(db.String(20), primary_key=True)
    version = db.Column(db.Integer, nullable=False)

    def __init__(self, appId, action):
        self.appId = appId
        self.action = action

    def __repr__(self):
        return f'<Acl_apppermission_model {self.appId}>'

    def save(self):
        if not self.id:
            db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Acl_apppermission_model.query.all()

    @staticmethod
    def get_by_id(id):
        return Acl_apppermission_model.query.get(id)

    @staticmethod
    def get_by_appId(appId):
        return Acl_apppermission_model.query.filter_by(appId=appId).first()


# Definicion de la tabla n_nemesis_acl_group_model

class Acl_group_model(db.Model, UserMixin):

    __tablename__ = 'n_nemesis_acl_group_model'

    name = db.Column(db.String(200), unique=True, nullable=True)
    parent = db.Column(db.String(20), nullable=True)
    id = db.Column(db.String(20), primary_key=True)
    version = db.Column(db.Integer, nullable=False)

    def __init__(self, name, parent):
        self.name = name
        self.parent = parent

    def __repr__(self):
        return f'<Acl_group_model {self.id}>'

    def save(self):
        if not self.id:
            db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Acl_group_model.query.all()

    @staticmethod
    def get_by_id(id):
        return Acl_group_model.query.get(id)

    @staticmethod
    def get_by_name(name):
        return Acl_group_model.query.filter_by(name=name).first()


# Definicion de la tabla n_nemesis_acl_permission_model

class Acl_permission_model(db.Model, UserMixin):

    __tablename__ = 'n_nemesis_acl_permission_model'

    group = db.Column(db.String(20), nullable=True)
    action = db.Column(db.String(200), nullable=True)
    id = db.Column(db.String(20), primary_key=True)
    version = db.Column(db.Integer, nullable=False)

    def __init__(self, group, action):
        self.group = group
        self.action = action

    def __repr__(self):
        return f'<Acl_permission_model {self.id}>'

    def save(self):
        if not self.id:
            db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Acl_permission_model.query.all()

    @staticmethod
    def get_by_id(id):
        return Acl_permission_model.query.get(id)

    @staticmethod
    def get_by_group(group):
        return Acl_permission_model.query.filter_by(group=group).first()

# Definicion de la tabla n_nemesis_acl_usergroup_model

class Acl_usergroup_model(db.Model, UserMixin):

    __tablename__ = 'n_nemesis_acl_usergroup_model'

    userId = db.Column(db.String(20), nullable=True)
    group = db.Column(db.String(20), nullable=True)
    id = db.Column(db.String(20), primary_key=True)
    version = db.Column(db.Integer, nullable=False)

    def __init__(self, group, userId):
        self.group = group
        self.userId = userId

    def __repr__(self):
        return f'<Acl_usergroup_model {self.id}>'

    def save(self):
        if not self.id:
            db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Acl_usergroup_model.query.all()

    @staticmethod
    def get_by_id(id):
        return Acl_usergroup_model.query.get(id)

    @staticmethod
    def get_by_group(group):
        return Acl_usergroup_model.query.filter_by(group=group).first()


# Definicion de la tabla n_nemesis_apps_app_model

class Apps_app_model(db.Model, UserMixin):

    __tablename__ = 'n_nemesis_apps_app_model'

    apiKey = db.Column(db.String(45), nullable=False)
    apiSecret = db.Column(db.String(45), nullable=False)
    appName = db.Column(db.String(45), unique=True, nullable=False)
    appAuthor = db.Column(db.String(45), nullable=False)
    id = db.Column(db.String(20), primary_key=False)
    version = db.Column(db.Integer, nullable=True)

    def __init__(self, appName, appAuthor):
        self.appName = appName
        self.appAuthor = appAuthor

    def __repr__(self):
        return f'<Apps_app_model {self.id}>'

    def save(self):
        if not self.id:
            db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Apps_app_model.query.all()

    @staticmethod
    def get_by_id(id):
        return Apps_app_model.query.get(id)

    @staticmethod
    def get_by_appName(appName):
        return Apps_app_model.query.filter_by(appName=appName).first()

# Definicion de la tabla n_nemesis_auth_session_model

class Auth_session_model(db.Model, UserMixin):

    __tablename__ = 'n_nemesis_auth_session_model'

    hostAddress = db.Column(db.String(45), nullable=True)
    hostAgent = db.Column(db.String(256), nullable=True)
    apiKey = db.Column(db.String(256), nullable=True)
    enabled = db.Column(db.Integer, nullable=True)
    time = db.Column(db.DateTime, primary_key=False)
    user = db.Column(db.String(20), nullable=True)
    accessToken = db.Column(db.String(120), unique=True, nullable=True)
    id = db.Column(db.String(20), primary_key=False)
    version = db.Column(db.Integer, nullable=True)

    def __init__(self, id, user):
        self.id = id
        self.user = user

    def __repr__(self):
        return f'<Auth_session_model {self.id}>'

    def save(self):
        if not self.id:
            db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Auth_session_model.query.all()

    @staticmethod
    def get_by_id(id):
        return Auth_session_model.query.get(id)

    @staticmethod
    def get_by_user(user):
        return Auth_session_model.query.filter_by(user=user).first()
