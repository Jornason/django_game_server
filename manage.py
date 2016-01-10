#!/usr/bin/env python
# coding=utf-8
import os
import sys


def check_log():
    """
    初始化
    :return:
    """
    project_path = os.getcwd()
    log_path = project_path + "/log"
    django_log_path = log_path + '/django'
    game_log_path = log_path + '/game'

    # 检查日志文件夹是否存在
    if not os.path.exists(log_path):
        os.mkdir(log_path)
    if not os.path.exists(django_log_path):
        os.mkdir(django_log_path)
    if not os.path.exists(game_log_path):
        os.mkdir(game_log_path)


if __name__ == "__main__":

    check_log()

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_game_server.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
