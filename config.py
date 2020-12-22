import os


class Config:
    SECRET_KEY = os.urandom(24)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UP_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)), "app/static/uploads/")  # 文件上传路径
    FC_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)), "app/static/uploads/users/")  # 用户头像上传路径

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    # 建立数据库连接
    HOST = "127.0.0.1"
    PORT = "3306"
    DATABASE = "mblog"
    USER = "root"
    PASSWORD = "admin1234"
    CHARSET = "utf8"
    DB_URI = "mysql+mysqlconnector://{}:{}@{}:{}/{}?charset={}".format(USER, PASSWORD, HOST, PORT, DATABASE, CHARSET)
    SQLALCHEMY_DATABASE_URI = DB_URI
    DEBUG = True


config = {
    'default': DevelopmentConfig
}

