# !/usr/bin/env python
# -*- coding:utf-8 -*-
"""
    @File   : `player`
    @Author : `long`
    @Date   : `2016-01-08`
    @About  : '游戏玩家的类'
"""
import uuid

from django.db import models


class Player(models.Model):

    # 用户昵称
    name = models.CharField(max_length=100)
    # 用户ID
    player_id = models.CharField(max_length=100, unique=True)
    # 用户头像
    head_img_url = models.CharField(max_length=200)
    # 金币
    gold = models.IntegerField(default=0)
    # 钻石
    diamond = models.IntegerField(default=0)

    def __unicode__(self):
        return self.name

    def init_player(self, data):
        """
        创建用户
        :param data:
        :return:
        """
        self.name = data.get('name')
        self.player_id = uuid.uuid4().hex
        self.head_img_url = data.get('head_img')
        self.save()

