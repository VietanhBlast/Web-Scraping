import requests
from bs4 import BeautifulSoup
import smtplib

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'}

# send a request to fetch HTML of the page
# but amazon has blocked this link,so it cant be requested :(
response = requests.get( 'https://www.amazon.co.uk/Anycubic-Kobra-Upgrade-High-Precision-Short-range-2-Neo/dp/B0CDC6TG8C/ref=sr_1_8?keywords=3d+printer&sr=8-8',headers=headers)

page = requests.get(response, headers=headers)

soup = BeautifulSoup(page.content ,'html.parser')

def check_price(): # function to check if the price has dropped 
    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()
    
    converted_price = float(price[:-3]) #converting the string amount to float 
    if(converted_price < 289.08):
        send_mail()
    
    print(converted_price)
    print(title.strip())

def send_mail(): # function that sends an email if the prices fell down
    server = smtplib.SMTP('smtp.gmail.com', 465)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('pythontester126@gmail.com', 'password')
    
    subject = 'Price fell down'
    body = 'https://www.amazon.co.uk/Anycubic-Kobra-Upgrade-High-Precision-Short-range-2-Neo/dp/B0CDC6TG8C/ref=sr_1_8?keywords=3d+printer&sr=8-8'

    msg = f"Subject: {subject}\n\n{body}"
    
    server.sendmail('pythontester126@gmail.com',msg)
    print('email has been sent')
    server.quit()
    
    check_price()
    
    
