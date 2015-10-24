__author__ = 'Jonathan'
import random

class Bicycle(object):
    def __init__(self, modelname, weight, cost):
        self.modelname = modelname
        self.weight = weight
        self.cost = cost

    def __repr__(self):
        return self.modelname

class LilBicycle(Bicycle):
    def __init__(self):
        super(LilBicycle, self).__init__("lilbike", 15, 100.0)

class MedBicycle(Bicycle):
    def __init__(self):
        super(MedBicycle, self).__init__("medbike", 20, 600.0)

class BigBicycle(Bicycle):
    def __init__(self):
        super(BigBicycle, self).__init__("bigbike", 30, 900.0)

class BikeShop(object):
    def __init__(self, name, inventory):
        self.name = name
        self.inventory = inventory

    def catalog(self, budget=None):
        if budget is None:
            for bike in self.inventory:
              print(bike.modelname, self.price(bike))
        else:
            candidates = []
            for bike in self.inventory:
                if self.price(bike) < budget:
                    candidates.append(bike)
            return candidates

    def price(self, bike):
        price = (bike.cost * 1.2)
        return price

class Customers(object):
    def __init__(self, name, budget):
        self.name = name
        self.budget = budget

    def choose(self, bikeshop):
        choice = random.choice(bikeshop.catalog(self.budget))
        return choice and bikeshop.catalog

def main():
    bikegroup = [LilBicycle(), LilBicycle(), MedBicycle(), BigBicycle(), BigBicycle(), BigBicycle(), Bicycle("orangebike", 23, 650.0),
                 Bicycle("yellowbike", 24, 700.0), Bicycle("redbike", 24, 700.0)]

    gearedup = BikeShop("Geared Up", bikegroup)

    crowd = [Customers("Jill", 200), Customers("Jon", 500), Customers("Giant", 1000)]
    choice1 = (crowd[0].choose(gearedup))
    print(choice1)
    bikegroup.remove(choice1)
    print(bikegroup)
    choice2 = (crowd[1].choose(gearedup))
    bikegroup.remove(choice2)
    print(choice2)
    print(bikegroup)
    choice3 = (crowd[2].choose(gearedup))
    print(choice3)
    print(bikegroup)

if __name__ == '__main__':
    main()
