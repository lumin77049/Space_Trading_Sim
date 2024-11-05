# This is a prototype of the ecomony system that is going into my C game :)


#  TODO: write stock object validation function
class StockObject:
    def __init__(self, value, amount, id):
        self.value = value      # should be positive
        self.amount = amount    # should be positive
        self.id = id            # should be 3 characters

# example object initialisation:
# stock_name = StockObject(1, 2, "abc")
#   value = 1
#   amount = 2
#   id = "abc"

def stock_validation(stock):
    if  stock.value < 0:
        print("ERR: STOCK VALUE LESS THAN 0")
    if stock.amount < 0:
        print("ERR: STOCK AMOUNT LESS THAN 0")
    if len(stock.id) < 3:
        print("ERR: STOCK ID LESS THAN 3 CHARACTERS")
    elif len(stock.id) > 3:
        print("ERR: STOCK ID MORE THAN 3 CHARACTERS")

