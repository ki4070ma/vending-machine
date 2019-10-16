from unittest import TestCase
from vending_machine import VendingMachine

class TestVendingMachine(TestCase):

    def test_insert_available_money(self):
        vm = VendingMachine()
        assert vm.insert(10) == 0
        assert vm.insert(50) == 0
        assert vm.insert(100) == 0
        assert vm.insert(500) == 0
        assert vm.insert(1000) == 0

    def test_insert_unavailable_money(self):
        vm = VendingMachine()
        assert vm.insert(-1) == -1
        assert vm.insert(3) == 3
        assert vm.insert(11) == 11
