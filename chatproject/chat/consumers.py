from channels.generic.websocket import AsyncWebsocketConsumer
import json

class ChatConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        user = self.scope["user"]

        if user.is_anonymous:
            await self.close()
        else:
            await self.accept()
            print("Connected:", user.username)

    async def receive(self, text_data):
        user = self.scope["user"]

        await self.send(text_data=json.dumps({
            "message": f"Hello {user.username}"
        }))