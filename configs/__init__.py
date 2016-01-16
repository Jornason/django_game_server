# !/usr/bin/env python
# -*- coding:utf-8 -*-
"""
    @File   : `$NAME.py`
    @Author : `long`
    @Date   : `2016-01-08`
    @About  : ''
"""
import ConfigParser
import os


# 读取配置文件
config_parser = ConfigParser.ConfigParser()
project_path = os.path.split(os.path.realpath(__file__))[0]
file_path = project_path + '/project.conf'
config_parser.read(file_path)

DB_CONFIG = dict(config_parser.items("db"))
REDIS_CONFIG = dict(config_parser.items("redis"))

