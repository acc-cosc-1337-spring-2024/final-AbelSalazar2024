#add import

import random
from question_c import create_stock_list

def main():
   
    stock_list = create_stock_list()
    random_stock = random.choice(stock_list)

    print("Stock Report")
    print("Symbol:", random_stock.get_symbol())
    print("Company Name:", random_stock.get_company_name())

main()



