import json

from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncJsonWebsocketConsumer
import time

class ArticleConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        await self.accept()  # ソケットを accept する
        self.groupName = 'article'
        await self.channel_layer.group_add(  # グループにチャンネルを追加
            self.groupName,
            self.channel_name,
        )

    async def disconnect(self, _close_code):
        await self.channel_layer.group_discard(  # グループからチャンネルを削除
            self.groupName,
            self.channel_name,
        )
        await self.close()  # ソケットを close する

    async def comminucateStatus(self, content):
        print(content)
        await self.send(text_data=json.dumps(content['message']))
        

