#  基于Django的游戏服务端框架

说明：此后端框架适合中小型，H5游戏。

## 环境配置

服务器框架Nginx + Superviosr + uWsgi + gevent + docker
![框架](https://raw.githubusercontent.com/ST9527/django_game_server/master/docs/框架.png)


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
![逻辑模型](https://raw.githubusercontent.com/ST9527/django_game_server/master/docs/模型.png)

- 通过在APP目录下新建`models`文件夹，在`__init__.py`里面导入，实现models的解耦。
- 游戏指令前两个字段表示指令所在模块，到了具体模块之后再通过具体的指令解析出具体的操作函数

