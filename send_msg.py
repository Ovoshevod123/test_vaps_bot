from telethon import TelegramClient
import time
api_id = 24187746
api_hash = '566ab80c14c9de12bf8850221d9587fd'

client = TelegramClient('test_tg', api_id, api_hash)
client.start()

async def main():
    await client.send_message(1696788497, 'ghbdtn')
    time.sleep(0.5)

with client:
    client.loop.run_until_complete(main())