This is Send message to Wechat application package. You can use
[Github](https://github.com/freeddser/scpmanWechat)

### pip install scpmanWechat
### demo
    from scpmanWechat import QYWeChatBot

    CORPID = 'XXX'
    CORPSECRET = 'XXXX'
    AGENTID = '1000002'
    Tag = "1"
    msg = "hello world"
    wx_bot = QYWeChatBot(CORPID, CORPSECRET, AGENTID, Tag)
    wx_bot.send_msg_to_tag_group("xxx")
