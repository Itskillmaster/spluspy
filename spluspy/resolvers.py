from .tl import types
from . import utils

class TargetResolver:
    def __init__(self, client):
        self.client = client

    async def resolve(self, target):
        return await self.client.get_input_entity(target)

async def resolve_reply_sender(message):
    reply = await message.get_reply_message()
    if reply:
        return reply.sender_id
    return None
