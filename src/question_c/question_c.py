#write functions here, don't add input('') statements here!
#Q3 - stock report list

import random

class Stock:
    def __init__(self, symbol, company_name):
        self.__symbol = symbol
        self.__company_name = company_name

    def get_symbol(self):
        return self.__symbol

    def get_company_name(self):
        return self.__company_name

def create_stock_list():
    stocks = [('AAPL', 'Apple Inc'), 
              ('CAT', 'Caterpillar'), 
              ('EK', 'Eastman Kodak'), 
              ('GOOG', 'Google'), 
              ('MSFT', 'Microsoft')]
    random.shuffle(stocks)
    stock_list = [Stock(symbol, company) for symbol, company in stocks]
    return stock_list