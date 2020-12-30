from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import uuid

db = SQLAlchemy()


class User(db.Model):
    """
    User,代表用户
    """
    __tablename__ = "user"
    __table_args__ = {'useexisting': True}
    id = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.String(128), default=uuid.uuid1())
    userName = db.Column(db.String(128))  # 用户名
    userAvatar = db.Column(db.String(255), unique=True)  # 头像
    userSex = db.Column(db.Integer)  # 性别 1：男 ，2；女 ， 0：其他
    userPhone = db.Column(db.String(11))  # 电话
    userTrueName = db.Column(db.String(128))  # 真实姓名
    userPassword = db.Column(db.String(128))  # 密码
    userCreateTime = db.Column(db.DateTime, index=True, default=datetime.now)

    def __repr__(self):
        return '<User %r>' % self.uid

    def check_password(self, user_password):
        """
        校验密码
        :param user_password:用户密码
        :return:返回布尔值 True or False
        """
        from werkzeug.security import check_password_hash
        return check_password_hash(self, user_password)


class Admin(db.Model):
    __tablename__ = "admin"
    __table_args__ = {'useexisting': True}
    id = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.String(128), default=uuid.uuid1())
    adminName = db.Column(db.String(128))
    adminSex = db.Column(db.Integer)  # 性别 1：男 ，2；女 ， 0：其他
    adminAvatar = db.Column(db.String(255), unique=True)
    adminTrueName = db.Column(db.String(128))
    adminPhone = db.Column(db.String(11))
    adminEmail = db.Column(db.String(32))
    adminCreateTime = db.Column(db.DateTime, index=True, default=datetime.now)

    def __repr__(self):
        return "<Admin %r>" % self.uid
