from twilio.rest import Client 
from time import sleep
from bs4 import BeautifulSoup
import requests

account_sid = 'sid from twillo' 
auth_token = 'auth token from twillo' 
client = Client(account_sid, auth_token) 
url="https://news.google.com/topics/CAAqKggKIiRDQkFTRlFvSUwyMHZNRGRqTVhZU0JXVnVMVWRDR2dKUVN5Z0FQAQ/sections/CAQiR0NCQVNMd29JTDIwdk1EZGpNWFlTQldWdUxVZENHZ0pRU3lJTkNBUWFDUW9ITDIwdk1HMXJlaW9KRWdjdmJTOHdiV3Q2S0FBKi4IACoqCAoiJENCQVNGUW9JTDIwdk1EZGpNWFlTQldWdUxVZENHZ0pRU3lnQVABUAE?hl=en-PK&gl=PK&ceid=PK:en"
def Get_News():
    html_text=requests.get(url).text
    soup = BeautifulSoup(html_text, 'lxml')
    posts = soup.findAll("article")
    output=[]
    for i,post in enumerate(posts):
        link = post.find("a",class_="RZIKme").get('href').replace("?hl=en-PK&gl=PK&ceid=PK%3Aen","")
        link = "https://news.google.com"+link.replace("./","/")
        heading = post.find("a",class_="RZIKme").decode_contents().strip()
        output.append({"No":i ,"heading": heading,"link": link})
    return output
messages = Get_News()
def send_love_message():
        for message in messages:
            client.messages.create(from_='whatsapp:+141 twillo whatsapp number',body=message['heading']+'\n'+message['link'],to='whatsapp:+92 your whatsapp number')
            sleep(2)