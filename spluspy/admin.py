from .tl import functions, types

class ChatAdmin:
    def __init__(self, client):
        self.client = client

    async def ban_user(self, chat, user, until_date=None):
        chat = await self.client.get_input_entity(chat)
        user = await self.client.get_input_entity(user)
        return await self.client(functions.channels.EditBannedRequest(
            channel=chat,
            participant=user,
            banned_rights=types.ChatBannedRights(
                until_date=until_date,
                view_messages=True,
                send_messages=True,
                send_media=True,
                send_stickers=True,
                send_gifs=True,
                send_games=True,
                send_inline=True,
                embed_links=True
            )
        ))

    async def mute_user(self, chat, user, until_date=None):
        chat = await self.client.get_input_entity(chat)
        user = await self.client.get_input_entity(user)
        return await self.client(functions.channels.EditBannedRequest(
            channel=chat,
            participant=user,
            banned_rights=types.ChatBannedRights(
                until_date=until_date,
                send_messages=True
            )
        ))

    async def unmute_user(self, chat, user):
        chat = await self.client.get_input_entity(chat)
        user = await self.client.get_input_entity(user)
        return await self.client(functions.channels.EditBannedRequest(
            channel=chat,
            participant=user,
            banned_rights=types.ChatBannedRights(
                until_date=None,
                send_messages=False
            )
        ))

    async def purge_messages(self, chat, limit=100):
        chat = await self.client.get_input_entity(chat)
        messages = await self.client.get_messages(chat, limit=limit)
        ids = [m.id for m in messages]
        if ids:
            return await self.client.delete_messages(chat, ids)
        return None
