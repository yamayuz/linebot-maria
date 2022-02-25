from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import urllib.request
import json
import environ

env = environ.Env()
env.read_env('.env')

REPLY_ENDPOINT_URL = "https://api.line.me/v2/bot/message/reply"
HEADER = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ' + env('ACCESSTOKEN')
}

class LineMessage():
    def __init__(self, messages):
        self.messages = messages

    def reply(self, reply_token):
        body = {
            'replyToken': reply_token,
            'messages': self.messages
        }
        req = urllib.request.Request(REPLY_ENDPOINT_URL, json.dumps(body).encode(), HEADER)
        print(req)
        try:
            with urllib.request.urlopen(req) as res:
                body = res.read()
        except urllib.error.HTTPError as err:
            print(err)
        except urllib.error.URLError as err:
            print(err.reason)