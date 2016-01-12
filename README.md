#  基于Django的游戏服务端框架
Author | Email
------------ | -------------
shutong9527 | st9527.cs229@gmail.com
说明：此后端框架适合中小型，H5游戏。

## 环境配置

服务器框架Nginx + Superviosr + uWsgi + gevent + docker
![框架](https://raw.githubusercontent.com/ST9527/django_game_server/master/docs/%E6%A1%86%E6%9E%B6.png)


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
![逻辑模型](https://raw.githubusercontent.com/ST9527/django_game_server/master/docs/%E6%A8%A1%E5%9E%8B.png)

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


## 说明

代码做提供思路只用，具体按实际项目进行设计。

