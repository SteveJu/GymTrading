import telegram
import re

"""
# Use below to get chat_id
import requests
TOKEN = "YOUR TELEGRAM BOT TOKEN"
url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"
print(requests.get(url).json())
message = "hello from your telegram bot"
url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
print(requests.get(url).json())
"""


class telegram_connection:
    def __init__(self):
        with open('hidden_files/info.txt', 'r')as f:
            lines = f.readlines()
        f.close()
        self.userID = lines[0]
        names = re.split(' ', lines[1])
        chat_ids = re.split(' ', lines[2])
        self.chatID = {}
        for n in range(len(names)):
            self.chatID[names[n]] = chat_ids[n]
        self.TOKEN = lines[3]
        self.bot = telegram.Bot(token=self.TOKEN)

    def sendTeleMessageToAll(self, message):
        for v in self.chatID.values():
            self.bot.send_message(chat_id=v, text=message)

    def sendTeleMessageToSelected(self, names, message):
        ids = []
        for name in names:
            ids.append(self.chatID[name])
        for i in ids:
            self.bot.sendMessage(chat_id=i, text=message)
