# !/usr/bin/env python
# -*- coding:utf-8 -*-
"""
    @File   : `mall_handler`
    @Author : `long`
    @Date   : `2016-01-08`
    @About  : ''
"""
from game.logic.basic_handler import BasicHandler
import logging

log = logging.getLogger(__name__)


class MallHandler(BasicHandler):
    """
    商城相关的处理类
    """

    def cmd_handler(self, cmd):
        """
        指令解析器
        :param cmd:
        :return:
        """
        cmd_map = {
            '1101': self.buy_item,
            # .....
        }
        if cmd not in cmd_map:
            log.error("Unknown cmd")
            return {
                "ret": -1,
                "msg": "非法指令"
            }
        else:
            result = cmd_map[cmd]()
            if result['ret'] == 0:
                result['cmd'] = cmd + 1
            return result

    def buy_item(self, data):
        """
        相关逻辑处理函数
        :param data:
        :return:
        """
        pass

