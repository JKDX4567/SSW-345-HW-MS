# needed for forward reference of Sale in Product,
# since Sale is not yet defined.
from __future__ import annotations
from typing import List

# forward reference used for class Sale
class Product:
    __lastSale: Sale = None
    inventory = 0

    def __init__(self, sale: Sale, inven):
        self.__lastSale = sale
        self.inventory = inven

    def setLastSale(self, lastSale: Sale):
        self.__lastSale = lastSale

    @property
    def getLastSale(self) -> Sale:
        return self.__lastSale

    def __getitem__(self, item):
        return self
    
    def getInventory(self) -> int:
        return self.inventory
    
    def gotInventory(self, count) -> int:
        self.inventory = self.inventory + count

# no forward reference needed since Product is defined
class Sale:
    __saleTimes = 0
    __productSold: List[Product] = None
    __saleNumber: int = 0

    def __init__(self, product: List[Product]):  #, saleNumber: int = 1):
        Sale.__saleTimes +=1
        self.__product = product
        self.__saleNumber = Sale.__saleTimes
        for index, product in enumerate(product):
            product[index].setLastSale(self)
            product.gotInventory(-1)

    def setProductsSold(self, productSold: List[Product]):
        self.__productSold = productSold

    @property
    def getSaleNumber(self) -> int:
        return self.__saleNumber


productOne = Product(sale=None, inven=1)
productTwo = Product(sale=None, inven=25)
print ("Product one has: " + str(productOne.getInventory()) + " units")
print ("Product two has: " + str(productTwo.getInventory()) + " units")

saleOne = Sale([productOne, productTwo])
saleTwo = Sale([productOne])
saleThree = Sale([productTwo])
print ("Product one has 2 sales")
print ("Product two has 2 sales")

print ("Product one has: " + str(productOne.getInventory()) + " units")
print ("Product two has: " + str(productTwo.getInventory()) + " units")
productOne.gotInventory(10)
print ("Product One has added 10 units")
print ("Product one has: " + str(productOne.getInventory()) + " units")
print(f"{productOne.getLastSale.getSaleNumber}, {productTwo.getLastSale.getSaleNumber}")

