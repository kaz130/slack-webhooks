# coding: utf-8

import requests
import json
import config

class Webhook:
    def __init__(self):
        self.webhook_url = config.WEBHOOK_URL

    def post(self, message, color=None):
        requests.post(self.webhook_url, data = json.dumps(message))

class MessageBuilder:
    def __init__(self):
        self.message = {}
        self.message['attachments'] = []

    def setText(self, text):
        self.message['text'] = text

    def addAttachments(self, title=None, color=None, text=None, failback=None):
        self.message['attachments'].append({
            'faileback' : failback,
            'color' : color,
            'title' : title,
            'text' : text
            })

    def getMessage(self):
        return self.message


