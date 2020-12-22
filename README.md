## 用Flask创建一个博客

本次开发IDE使用的是PyCharm 2020.3，Python版本3.7.4，Flask版本1.1.2

### 1. 蓝图

​		蓝图（blueprint）是Flask中的一个存储操作方法的容器，这些操作在这个Blueprint 被注册到一个应用之后就可以被调用，Flask 可以通过Blueprint来组织URL以及处理请求。

#### 1.1 使用蓝图

在pycharm中，创建一个flask项目后我们还需要自己创建一个项目文件，config.py，manage.py等必要的文件，创建完成后我们能看见一下目录

![image-20201222114009680](https://i.loli.net/2020/12/22/PpjX61BvVyKYL9J.png)

要使用蓝图，就需要配置Python包中的`__init__.py`文件各个包中的`__init__.py`文件配置如下：

`application/__init__.py`:

~~~python
# _*_ Coding:utf-8 _*_

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import config

db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    db.init_app(app)
    # 注册蓝图
    from applications.front import front as front_blueprint
    from applications.admin import admin as admin_blueprint
    app.register_blueprint(front_blueprint)
    app.register_blueprint(admin_blueprint, url_prefix="/admin")

    return app
~~~

而在admin和front两个项目包下则不需要再注册蓝图了，只需要引入views文件配置如下：

`application/admin/__init__.py`和`application/front/__init__.py`：

~~~python
from flask import Blueprint
# 如果是admin目录下的文件就需要admin = ("admin", __name__)
front = Blueprint("front", __name__)
# 需要后导入
import applications.front.views
~~~

这个是git推送流程
![image-20201222150139097](https://i.loli.net/2020/12/22/AY69CjNGXbOlr5E.png)

