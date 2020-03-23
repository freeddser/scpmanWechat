# -*- coding: utf-8 -*-
import json
import requests
class QYWeChatBot(object):
    def __init__(self,corp_id,crop_secret,agent_id,group_tag_id,message_body=""):
        self.CORPID = corp_id
        self.CORPSECRET = crop_secret
        self.AGENTID = agent_id
        self.Tag = group_tag_id
        self.Message=message_body

    def _get_access_token(self):
        url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken'
        values = {'corpid': self.CORPID,
                  'corpsecret': self.CORPSECRET,
                  }
        req = requests.post(url, params=values)
        data = json.loads(req.text)
        return data["access_token"]



    def send_msg_to_tag_group(self, message):
        send_url = 'https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=' + self._get_access_token()
        send_values = {
            "totag":self.Tag,
            "msgtype": "text",
            "agentid": self.AGENTID,
            "text": {
                "content": message
                },
            "safe": "0"
            }
        data=json.dumps(send_values,ensure_ascii=False)
        # send_msges=(bytes(json.dumps(send_values), 'utf-8'))
        respone = requests.post(send_url, data)
        respone = respone.json()
        return respone["errmsg"]


