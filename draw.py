from selenium import webdriver
import time
from bs4 import BeautifulSoup
import random

#steamdb.info/sales
#camelcamelcamel.com
ytLiveChatURL = "https://www.youtube.com/live_chat?v=yXMbjaPIfs8"  
keyword = "as"
eligibleUsers = set()


op = webdriver.ChromeOptions()
op.add_argument('headless')
browser = webdriver.Chrome(options=op)

# start web browser
#browser = webdriver.Chrome()

def getHTML(url):
    # get source code
    browser.get(url)
    time.sleep(1)
    html = browser.page_source
    return html

def parseHTML(html_source):
    return BeautifulSoup(html_source, 'html.parser')
    
def getMessages(soup):    
    return soup.find_all("yt-live-chat-text-message-renderer")
    
def updateEligibleUsers(messages): 
    for message in messages:
        content = message.find("div", {"id": "content"}) 
        author = content.find("span", {"id": "author-name"}).text
        message_content = content.find("span", {"id": "message"}).text
        if keyword in message_content.lower():
            eligibleUsers.add(author)

def startDrawing(eligibleUsersList):
    print("Cekilis basliyor! {totalUserCount} kisi katilmaya hak kazandi".format(
        totalUserCount = len(eligibleUsers)))

    for i in range(1,5):
        noktalar = i * "."
        print("Rasgele bir sayi cekiliyor" + noktalar)
        time.sleep(1)

    print("Son kontroller yapiliyor!")
    print("{totalUserCount} kisi arasindan kazanan:".format(
        totalUserCount=len(eligibleUsersList)), random.choice(eligibleUsersList))

def main():
    for i in range(0,7):
        html_source = getHTML(ytLiveChatURL)
        soup = parseHTML(html_source)
        messages = getMessages(soup)
        updateEligibleUsers(messages)
        print("{count} kisi cekilise katilmis durumda.".format(
            count = len(eligibleUsers)))
        time.sleep(10)
        
    eligibleUsersList = list(eligibleUsers)
    startDrawing(eligibleUsersList)

    # close web browser
    #browser.close()

main()
