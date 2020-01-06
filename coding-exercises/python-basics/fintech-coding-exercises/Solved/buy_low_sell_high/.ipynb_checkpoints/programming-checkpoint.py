# stock_list = ['$1.42', '$1.32', '$1.45', '$1.20', '$1.34', '$1.74', '$1.10', '$1.89', '$1.42', '$1.90', '$1.80', '$1.85']
stock_list = [1.42, 1.32, 1.45, 1.20, 1.34, 1.74, 1.10, 1.89, 1.42, 1.90, 1.80, 1.85]

def stock_purchase_price(stock_list):
    min_stock_price = min(stock_list)
    max_stock_price = max(stock_list)
    number_of_shares = 10000

    if ((max_stock_price - min_stock_price)*(number_of_shares)) > 4300:
        return "A better trade and profit was possible"
    
stock_purchase_price(stock_list)
