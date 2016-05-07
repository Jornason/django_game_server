#  基于Django的游戏服务端框架
Author | Email
------------ | -------------
shutong9527 | st9527.cs229@gmail.com
说明：此后端框架适合中小型，H5游戏。

## 环境配置

服务器框架Nginx + Superviosr + uWsgi + gevent + docker
![框架](http://o6p181fdf.bkt.clouddn.com/16-5-7/805876.jpg)

- 为什么选择[uwsgi＋gevent](http://blog.kgriffs.com/2012/12/18/uwsgi-vs-gunicorn-vs-node-benchmarks.html)
- git hook 实现代码更新自动部署
- 代码变化自动[热重启](http://projects.unbit.it/uwsgi/wiki/TipsAndTricks#uWSGIdjangoautoreloadmode)（[相关链接](http://uwsgi-docs.readthedocs.org/en/latest/PythonModule.html)）

``` python
import uwsgi
from uwsgidecorators import timer
from django.utils import autoreload

@timer(3)
def change_code_gracefully_reload(sig):
    if autoreload.code_changed()
        uwsgi.reload()
        
```

- master分支代表正式环境，dev分支代表测试环境


## 框架模型

逻辑模型
![逻辑模型](http://o6p181fdf.bkt.clouddn.com/16-5-7/98436669.jpg)

- 通过在APP目录下新建`models`文件夹，在`__init__.py`里面导入，实现models的解耦。
- 游戏指令前两个字段表示指令所在模块，到了具体模块之后再通过具体的指令解析出具体的操作函数
- 日志系统(settings.py)

``` python
# about logging refer to : https://docs.djangoproject.com/en/1.9/topics/logging/
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': "[%(levelname)s] [%(asctime)s] [%(name)s:%(lineno)s] %(message)s",
            'datefmt': "%d/%b/%Y %H:%M:%S"
        },
        'simple': {
            'format': "[%(levelname)s] [%(asctime)s] %(message)s",
            'datefmt': "%d/%b/%Y %H:%M:%S"
        },
    },
    'handlers': {
        'debug': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'log/django/debug.log',
            'formatter': 'verbose'
        },
        'info': {
            'level': 'INFO',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': 'log/game/info.log',
            'formatter': 'simple',
            # 每天备份一次，备份20天内的日志
            'when': "D",
            'interval': 1,
            "backupCount": 20,
            "encoding": "utf8"
        },
        'error': {
            'level': 'ERROR',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': 'log/game/error.log',
            'formatter': 'verbose',
            'when': "D",
            'interval': 1,
            "backupCount": 20,
            "encoding": "utf8"
        },
    },
    'loggers': {
        'django': {
            'handlers': ['debug'],
            'propagate': True,
            'level': 'DEBUG',
        },
        'game': {
            'handlers': ['info', 'error'],
            'level': 'INFO',
        },
    }
}
```


## 补充说明

- 代码做提供思路只用，具体按实际项目进行设计。
- 项目应用步骤：

	1. 删除`.git`文件夹
	2. 修改`configs`文件夹里面的配置文件
	3. 安装依赖 `pip install -r requirements.txt`
	4. 根据具体项目，修改`urls.py` 和新建app（参考`game`）。

- 关于Redis作为Django缓存有两个库，[django-redis](http://niwinz.github.io/django-redis/latest/)和[django-redis-cache](http://django-redis-cache.readthedocs.org/en/latest/)，关于两者的区别笔者没有找到很好的文章，只搜到[StackOverFlow的一篇文章](http://stackoverflow.com/questions/21932097/difference-between-django-redis-cache-and-django-redis-for-redis-caching-with-dj)。笔者看了两个库的文档，决定用的是[django-redis](http://niwinz.github.io/django-redis/latest/)（功能越多越好原则 :) ）