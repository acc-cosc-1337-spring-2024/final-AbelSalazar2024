#write functions here, don't add input('') statements here!
#Q2 - A report of stock purchase history

class stock():
    def __init__(self, symbol, company_name):
        self.__symbol = symbol
        self.__company_name = company_name
    
    def get_symbol(self):
        return self.__symbol
    
    def get_company_name(self):
        return self.__company_name

def stock_purchase_history():
    stock1 = stock('AAPL','Apple Inc' )
    stock2 = stock('CAT','Caterpillar' )
    stock3 = stock('EK','Eastman Kodak' )
    stock4 = stock('GOOG','Google' )
    stock5 = stock('MSFT','Microsoft' )

    dictionary = {stock1.get_symbol():stock1.get_company_name(), 
                  stock2.get_symbol():stock2.get_company_name(), 
                  stock3.get_symbol():stock3.get_company_name(), 
                  stock4.get_symbol():stock4.get_company_name(), 
                  stock5.get_symbol():stock5.get_company_name(),}

    print("Symbol  Company name")
    for symbol, company_name in dictionary.items(): 
        print(symbol.ljust(7), company_name)
    
