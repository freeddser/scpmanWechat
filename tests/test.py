from scpmanWechat import QYWeChatBot

CORPID = 'XXX'
CORPSECRET = 'XXXX'
AGENTID = '1000002'
Tag = "1"
msg = "hello world"
wx_bot = QYWeChatBot(CORPID, CORPSECRET, AGENTID, Tag)
wx_bot.send_msg_to_tag_group("xxx")
