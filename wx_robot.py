from wxpy import *
import requests
import md5sign


# 获取tensentAi 回答
def get_content(plus_item):
    # 聊天的API地址
    url = "https://api.ai.qq.com/fcgi-bin/nlp/nlp_textchat"
    # 获取请求参数
    plus_item = plus_item.encode('utf-8')
    payload = md5sign.get_params(plus_item)
    # r = requests.get(url,params=payload)
    r = requests.post(url, data=payload)
    return r.json()["data"]["answer"]


# 登录bot
bot = Bot(console_qr=2)
# 搜索指定的微信群
two_group = bot.groups().search('恩佐—相信让美好从这里发生')[0]

# 注册好友请求类消息
@bot.register(msg_types=FRIENDS)
def auto_accept_friends(msg):
    # 接受好友请求
    new_friend = msg.card.accept()
    # 向新的好友发送消息
    new_friend.send("哈哈主人不在，智障机器人代替主人添加了您")


# 监听所有*群聊*对象中的*文本*消息
@bot.register(Group, TEXT)
def reply_group_msg(msg):
    # 如果是群聊且被@了
    if msg.is_at:
        message = msg.text
        print(message)
        message = message.split('@恩佐Enzo')[1].strip()
        answer = get_content(message)
        if answer != '':
            msg.reply(answer)


# 监听所有*好友*对象中的*文本*消息
@bot.register(Friend, TEXT)
def reply_group_msg(msg):
    message = msg.text
    print('好友聊天：' + message)
    if message.__contains__('加群'):
        # use_invitation为True，发送群邀请，False则拉进群聊
        two_group.add_members(msg.sender, use_invitation=True)
    else:
        answer = get_content(message)
        if answer != '':
            return answer


# 堵塞线程，并进入 Python 命令行
bot.join()
