from selenium import webdriver
from bs4 import BeautifulSoup
import random
import time



kisiler = set()


browser = webdriver.Firefox()

ytLiveUrl="https://www.youtube.com/live_chat?v=eQdA8dvsgQs"
browser.get(ytLiveUrl)
html = browser.page_source
time.sleep(2)


soup = BeautifulSoup(html,'html.parser')
messages = soup.find_all("yt-live-chat-text-message-renderer")

for message in messages:
    content = message.find("div",{"id":"content"})
    author = content.find("span",{"id":"author-name"}).text
    umessage = content.find("span",{"id":"message"}).text
    if "lol" in umessage.lower():
        kisiler.add(author)

print("hak kazanan kişi sayısı! {totalUserCount}".format(totalUserCount=len(kisiler)))
time.sleep(5)
print("the draw begins!")
time.sleep(3)
kisilerList= list(kisiler)
print(# HACK: "Congurglations: ",random.choice(kisilerList))

browser.close()
