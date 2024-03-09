import json
from channels.generic.websocket import AsyncWebsocketConsumer

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_group_name = "group_chat_gfg"
        if self.channel_layer:
            await self.channel_layer.group_add(
                self.room_group_name,
                self.channel_name
            )
        await self.accept()
    async def disconnect(self , close_code):
        if self.channel_layer:
            await self.channel_layer.group_discard(
                self.room_group_name, 
                self.channel_name
            )
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json.get("message")
        username = text_data_json.get("username")
        if message and username and self.channel_layer:
            await self.channel_layer.group_send(
                self.room_group_name,{
                    "type": "sendMessage",
                    "message": message,
                    "username": username,
            })
    async def sendMessage(self , event) : 
        message = event["message"]
        username = event["username"]
        await self.send(text_data = json.dumps({"message":message ,"username":username}))
