import requests
from bs4 import BeautifulSoup 
from main import get_db
from fastapi import FastAPI, Depends, HTTPException
import models,schemas
from sqlalchemy.orm import Session


# https://cdn.tsetmc.com/api/BestLimits/46348559193224090
# https://cdn.tsetmc.com/api/ClosingPrice/GetClosingPriceInfo/46348559193224090

url='https://cdn.tsetmc.com/api/ClosingPrice/GetClosingPriceInfo/46348559193224090'

headers = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'}
r = requests.get(url,headers=headers)
yesterday_price = r.json()['closingPriceInfo']['priceYesterday']
first_price = r.json()['closingPriceInfo']['priceFirst']
pclosing = r.json()['closingPriceInfo']['pClosing']
last_transaction = r.json()['closingPriceInfo']['pClosing']
transaction_number = r.json()['closingPriceInfo']['zTotTran']
transaction_valume = r.json()['closingPriceInfo']['qTotTran5J']
transaction_value = r.json()['closingPriceInfo']['qTotCap']
market_value = r.json()['closingPriceInfo']['qTotCap']
print(first_price)
def read_company(company:schemas.FirstBoourseMarketSchema,db: Session= Depends(get_db)):
    company = models.FirstBoourseMarket(last_transaction = last_transaction, final_price = pclosing, first_price = first_price, yesterday_price = yesterday_price,transactions_number = transaction_number, volume_transaction = transaction_valume, transaction_value = transaction_value )
    db.add(company)
    db.commit()
    db.refresh(company)
    return company
read_company()

