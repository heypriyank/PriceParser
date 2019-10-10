import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = 'https://www.amazon.in/Test-Exclusive-607/dp/B07HGJKDQB/ref=sr_1_1?keywords=oneplus+7+pro&qid=1570640962&smid' \
      '=A23AODI1X2CEAE&sr=8-1 '
      
#search your headers from google - type "my user agent" and copy
headers = {
    "Headers": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) '
               'Chrome/77.0.3865.90 Safari/537.36'}
    
#prices in AMAZON INDIA is in INR so the string slicing is variable by currency.
#here the desired amount fall down is capped at Rs. 43000/-
def price_parse():
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    price = soup.find(id='priceblock_dealprice').get_text()
    converted_price = int(price[2:4])
    if converted_price < 43:
        send_mail()


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo_or_helo_if_needed()
    server.starttls()
    server.ehlo_or_helo_if_needed()
    server.login('YOUR EMAIL HERE', 'GOOGLE 2-step PASSWORD HERE example-(wpmqaezccknyrkbk)')

    subject = 'Price Fell DOWN'
    body = '''Check the link for your product 
    https://www.amazon.in/Test-Exclusive-607/dp/B07HGJKDQB/ref=sr_1_1?keywords=oneplus+7+pro&qid=1570640962&smid=A23AODI1X2CEAE&sr=8-1'''
    message = f'Subject: {subject}\n\n{body}'

    server.sendmail(
        'SENDER EMAIL',
        'RECIEVER EMAIL',
        message
    )
    server.quit()


while (True):
    price_parse()
    time.sleep(60 * 60 * 24)
    print('Email will be sent now if the price had fallen !')
