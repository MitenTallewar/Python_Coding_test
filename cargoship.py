"""
Implement the CargoShip class so that:
• load adds all items from new_cargo to the cargo.
  new_cargo and cargo are lists of tuples where the first element in the tuple is a port name and the second element is the item weight.
• unload removes items from cargo that are in the same port and returns them as a list of tuples.
  If there are no items for that port, then an empty list should be returned.
• can depart returns True if the sum of all weights in cargo is less than or equal to the capacity, and False if not.
  For example, if a new CargoShip is created with capacity 10 and load is called with [("NEW York", 1), ("London", 20)]
  then calling unload("New York") should return [("New York", 1)],
  cargo should have the value of [("London", 20)] and calling con_depart should return False.

"""

class Cargoship:
    def __init__(self,capacity):
        self.cargo = []
        self.capacity = capacity


    def unload(self,port):
        remove_cargo = []
        for c in self.cargo:
            if c[0] == port:
                remove_cargo = c
                self.cargo.remove(c)
        return list(remove_cargo)


    def can_depart(self):
        total_weight = 0
        for c in self.cargo:
            total_weight +=c[1]
        if total_weight <= self.capacity:
            return True
        return False


    def load(self,new_cargo):
        for cargos in new_cargo:
            self.cargo.append(cargos)

if __name__ == '__main__':
    cs = Cargoship(capacity=10)
    cs.load([("New York",1),("London",2),("Dubai",5)])
    print(cs.unload(port='New York'))
    print(cs.can_depart())
