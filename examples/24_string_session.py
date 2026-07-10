"""Example 24: String Session

Demonstrates using string sessions for session persistence.
"""

from spluspy import Client
from spluspy.session import StringSession


async def main():
    # Create a new session
    session = StringSession()
    client = Client(session)

    @client.on_message(filters.command("start"))
    async def handler(m):
        await m.reply("Hello!")

    await client.start(phone="+98XXXXXXXXXX")

    # Export the session string
    session_string = session.export()
    print(f"Session string: {session_string}")

    # You can save this string and use it later
    # restored_session = StringSession.import_string(session_string)
    # client2 = Client(restored_session)

    await client.run_until_disconnected()


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
