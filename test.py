import asyncio
from telethon import TelegramClient
from python_socks.async_.asyncio import Proxy
from telethon.errors import SessionPasswordNeededError

import pandas as pd
from openpyxl.reader.excel import load_workbook

api_id = 24187746
api_hash = '566ab80c14c9de12bf8850221d9587fd'
proxy = Proxy.from_url('http://172.67.182.15:80')

id_list = []

client = TelegramClient('test.xlsx', api_id, api_hash)

# phone = input("Enter phone: ")
# client.send_code_request(phone, force_sms=False)
# value = input("Enter login code: ")
# try:
#     me = client.sign_in(phone, code=value)
# except SessionPasswordNeededError:
#     password = input("Enter password: ")
#     me = client.sign_in(password=password)

client.start()

wb = load_workbook('test.xlsx')
ws = wb['welcome']

df = pd.read_excel('test.xlsx', sheet_name='welcome')
a = pd.DataFrame(df)

for i, data in a.iterrows():
    data = int(data[a.columns[0]])
    id_list.append([i, data])

async def main(d):
    await client.send_message(d, 'ghbdtn')
    await asyncio.sleep(0.5)

for i, d in id_list:
    with client:
        client.loop.run_until_complete(main(int(d)))
        # ws.delete_rows(1)
    # print(i, d)

wb.save('test.xlsx')
wb.close()
