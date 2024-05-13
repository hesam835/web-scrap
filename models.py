from database import Base
from sqlalchemy import Column,String,Integer


class Company(Base):
    __tablename__ = "company"
    
    id1 = Column(Integer, primary_key=True)
    sales_number = Column(Integer)
    buy_number = Column(Integer)
    sales_valume = Column(Integer)
    buy_valume = Column(Integer)
    sales = Column(Integer)
    buy = Column(Integer)
    
    
class FirstBoourseMarket(Base):
    __tablename__ = "Bourse"
    
    id2 = Column(Integer, primary_key=True)
    last_transaction = Column(Integer)
    final_price = Column(Integer)
    first_price = Column(Integer)
    yesterday_price = Column(Integer)
    transactions_number = Column(Integer)
    volume_transaction = Column(Integer)
    transaction_value = Column(Integer)
    market_value = Column(Integer)