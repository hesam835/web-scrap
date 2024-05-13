from fastapi import FastAPI, Depends, HTTPException,Request
from database import SessionLocal,engine
from sqlalchemy.orm import Session
import schemas,models
import requests
from bs4 import BeautifulSoup
from fastapi.templating import Jinja2Templates



#========================================================================== 
#=========================         data            ========================
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

headers2 = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'}
url2 = 'https://cdn.tsetmc.com/api/BestLimits/46348559193224090'
response = requests.get(url2, headers =headers2 )

#==========================================================================
bourse_count = 0
company_count = 0

models.Base.metadata.create_all(bind=engine)
app = FastAPI()
templates = Jinja2Templates(directory="templates")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        

@app.get('/u',response_model=schemas.FirstBoourseMarketSchema)        
def read_company(db: Session= Depends(get_db)):
    global bourse_count
    if bourse_count<1:
        bourse_market = models.FirstBoourseMarket(last_transaction=int(last_transaction), final_price=int(pclosing), first_price=int(first_price), yesterday_price=int(yesterday_price), transactions_number=int(transaction_number), volume_transaction=int(transaction_valume), transaction_value=int(transaction_value), market_value=int(market_value))
        db.add(bourse_market)
        db.commit()
        bourse_count+=1
        
        # for number in response.json()['bestLimits']:
        #     company = models.Company(buy_number=int(number['zOrdMeDem']),sales_number=int(number['zOrdMeOf']),buy_valume=int(number['qTitMeDem']),sales_valume=int(number['qTitMeOf']),sales=int(number['pMeOf']),buy=int(number['pMeDem']))
        #     db.add(company)
        #     db.commit()
    return bourse_market





print(bourse_count)        

        
@app.get('/',response_model=schemas.CompnySchema)        
def read_template(request:Request,db: Session=Depends(get_db)):
    global company_count
    if company_count<1:
        for number in response.json()['bestLimits']:
            company = models.Company(buy_number=int(number['zOrdMeDem']),sales_number=int(number['zOrdMeOf']),buy_valume=int(number['qTitMeDem']),sales_valume=int(number['qTitMeOf']),sales=int(number['pMeOf']),buy=int(number['pMeDem']))
            db.add(company)
            db.commit()
            company_count+=1
    return templates.TemplateResponse('home.html', {'request':request})
    

@app.get('/template_api_bourse',response_model=schemas.FirstBoourseMarketSchema)
def read_template(db: Session=Depends(get_db)):
    db_company=db.query(models.FirstBoourseMarket).filter(models.FirstBoourseMarket.id2==1).first()
    return db_company

@app.get('/template_api_company')
def read_template_company(db: Session=Depends(get_db)):
    db_company=db.query(models.Company).filter(models.FirstBoourseMarket.id2<=1).all()
    return db_company


