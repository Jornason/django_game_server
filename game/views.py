# coding=utf-8
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from game.models.player import Player
import logging
from django.http import JsonResponse
import ujson
from game.logic.activity_handler import ActivityHandler
from game.logic.mall_handler import MallHandler
from game.logic.player_handler import PlayerHandler

# Create your views here.
log = logging.getLogger(__name__)
# 模块表
module_maps = {
    '10': ActivityHandler,
    '11': MallHandler,
    '12': PlayerHandler
    # ......
}


def login_handler(request):
    """
    处理用户注册登录
    设置session的值
    :param request:
    :return:
    """
    pass


def logic_handler(request):
    """
    游戏逻辑处理入口,指令处理器
    游戏指令由四个数字组成, mmcc
    前两位表示指令所属的模块
    :param request:
    :return: json 格式,ret 为 0 表示成功,否则失败
    """
    try:
        if request.method == "POST":
            player_id = request.session['player_id']
            player = get_object_or_404(Player, player_id=player_id)
            game_data = ujson.loads(request.body)
            cmd = game_data.get('cmd')
            if cmd[:2] in module_maps:
                log.info("接收到指令: [%s]" % cmd)
                module = module_maps['cmd'](player, game_data)
                result = module.cmd_handler(cmd)
                return JsonResponse(result)
        else:
            return render(status=403)
    except:
        log.exception()
        return render(status=500)


def pay_handler(request):
    """
    处理支付相关的逻辑
    :param request:
    :return:
    """
    pass
