# needed for forward reference of Sale in Product,
# since Sale is not yet defined.
from __future__ import annotations
from typing import List

# forward reference used for class Sale
class Product:
    __lastSale: Sale = None

    def __init__(self, sale: Sale, inventory: int):
        self.__lastSale = sale
        self.__inventory = inventory

    def setLastSale(self, lastSale: Sale):
        self.__lastSale = lastSale

    @property
    def getLastSale(self) -> Sale:
        return self.__lastSale

    def __getitem__(self, item):
        return self
    
    def updateInventory(self, quantity: int):
        self.__inventory -= quantity
        if self.__inventory < 0:
            print(f"Warning! Inventory is running out!")
            
    @property        
    def getInventory(self) -> int:
        return self.__inventory

# no forward reference needed since Product is defined
class Sale:
    __saleTimes = 0
    __productSold: List[Product] = None
    __saleNumber: int = 0

    def __init__(self, product: List[Product], quantities: List[int]):  #, saleNumber: int = 1):
        Sale.__saleTimes +=1
        self.__product = product
        self.__quantities = quantities
        self.__saleNumber = Sale.__saleTimes
        for index, product in enumerate(product):
            product[index].setLastSale(self)
            product[index].updateInventory(quantities[index])

    def setProductsSold(self, productSold: List[Product]):
        self.__productSold = productSold

    @property
    def getSaleNumber(self) -> int:
        return self.__saleNumber


productOne = Product(sale=None, inventory=25)
productTwo = Product(sale=None, inventory=43)

saleOne = Sale([productOne, productTwo], [7, 4])
saleTwo = Sale([productOne], [10])
saleThree = Sale([productTwo], [20])

print(f"Starting inventory of ProductOne is 25")
print(f"Starting inventory of ProductTwo is 43")
print(f"After all of the sales, we get the following:")
print(f"ProductOne - Last Sale: #{productOne.getLastSale.getSaleNumber}, Inventory Left: {productOne.getInventory}")
print(f"ProductTwo - Last Sale: #{productTwo.getLastSale.getSaleNumber}, Inventory Left: {productTwo.getInventory}")