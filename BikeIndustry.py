__author__ = 'Jonathan'

class Bicycle(object):
    def __init__(self, modelname=[], weight=[], cost=[]):
        self.modelname = modelname
        self.weight = weight
        self.cost = cost


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

    def who_buys(self, budget=[], selling_for=[]):
        self.budget = budget
        self.selling_for = selling_for
        sold = []
        for money in self.budget:
            if money > money in self.selling_for:
                sold.append(money)
            else:
                sold.append("not sold")
        return sold

def main():
    bikegroup = Bicycle(["lilbike", "medbike", "bigbike", "orangebike", "yellowbike", "redbike"],
                        [15, 20, 30, 23, 24, 25], [100.0, 600.0, 900.0, 650, 700, 750])
    print(bikegroup.cost)
    gearedup = BikeShop("Geared Up", [6, 6, 6])
    print(gearedup.price(bikegroup.cost))
    crowd = Customers(["Jill", "Jon", "Giant"], [200, 500, 1000])
    print(crowd.who_buys(crowd.money, gearedup.price(bikegroup.cost)))

if __name__ == '__main__':
    main()
