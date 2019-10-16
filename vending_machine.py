#!/usr/bin/env python

class VendingMachine(object):

    def __init__(self):
        self.inserted_money = 0

    def insert(self, money):
        if money in [10, 50, 100, 500, 1000]:
            self.inserted_money += money
            return 0
        return money


if __name__ == '__main__':

    vending_machine = VendingMachine()
    print(vending_machine.insert(10))
