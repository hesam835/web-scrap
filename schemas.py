from pydantic import BaseModel

class CompnySchema(BaseModel):
    id1 : int
    sales_number : int
    buy_number : int
    sales_valume : int
    buy_valume : int
    sales : int
    buy : int    
    
    class Config:
        from_attributes=True


    
    
class FirstBoourseMarketSchema(BaseModel):
    id2 : int
    last_transaction : int
    final_price : int
    first_price : int
    yesterday_price : int
    transactions_number : int
    volume_transaction : int
    transaction_value : int
    market_value : int
    class Config:
        from_attributes=True
    
