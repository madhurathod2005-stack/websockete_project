online_users = set()

async def connect(self):
    self.user = self.scope["user"]
    online_users.add(self.user.username)

    await self.channel_layer.group_send(
        self.room_group_name,
        {
            'type': 'user_list',
            'users': list(online_users)
        }
    )
    async def disconnect(self, close_code):
     online_users.discard(self.user.username)

    await self.channel_layer.group_send(
        self.room_group_name,
        {
            'type': 'user_list',
            'users': list(online_users)
        }
    )
    async def user_list(self, event):
     await self.send(text_data=json.dumps({
        'type': 'user_list',
        'users': event['users']
    }))