# !/usr/bin/env python
# -*- coding:utf-8 -*-
"""
    @File   : `basic_handler`
    @Author : `long`
    @Date   : `2016-01-09`
    @About  : ''
"""


class BasicHandler(object):
    """
    逻辑处理类父类,用户定义公用方法和成员
    """
    def __init__(self, player, data):
        """
        初始化
        :param player:
        :param data:
        :return:
        """
        self.player = player
        self.player_data = player.player_data
        self.player_statistic = player.player_statistic
        self.data = data



