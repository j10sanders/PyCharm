__author__ = 'Jonathan'

class Bicycle(object):
    def __init__(self, modelname=[], weight=[], cost=[]):
        self.modelname = modelname
        self.weight = weight
        self.cost = cost
        return cost

class BikeShop(object):
    def __init__(self, name, inventory=[]):
        self.name = name
        self.inventory = inventory

    def price(self, prod_cost=[]):
        self.prod_cost = prod_cost
        salecost = []
        for price in prod_cost:
            price = (price* .2) + price
            salecost.append(price)
        return salecost

class Customers(object):
    def __init__(self, name=[], money=[]):
        self.name = name
        self.money = money

def main():
    bikegroup = Bicycle(["lilbike", "medbike" "bigbike"], [15, 20, 30], [100.0, 300.0, 900])
    print(bikegroup)
    print(bikegroup.weight)
    #print(bikegroup.price())
    gearedup = BikeShop("Geared Up", bikegroup.modelname)
    crowd = Customers(["Tom", "Jill"], [200, 500, 1000])



    #fullinventory = {}
    #for bikes in bikegroup.modelname:
        #fullinventory.append(bikes:[bikegroup.weight, bikegroup.price])
        #return fullinventory


    #medbike = Bicycle("medbike", 30, 150)
    #bigbike = Bicycle("bigbike", 60, 250)
    #oarngebike = Bicycle("orangebike", 35, 550)
    #yellobike = Bicycle("yellowbike", 36, 700)
    #redbike = Bicycle("redbike", 37, 1100)
    #print(redbike.sale_price())

if __name__ == '__main__':
    main()
