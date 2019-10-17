import sys
from unittest import TestCase
from vending_machine import VendingMachine
from io import StringIO
import pytest

class TestVendingMachine(object):

    def setup_method(self, method):
        print('method{}'.format(method.__name__))
        self.vm = VendingMachine()
        self.captor = StringIO()
        sys.stdout = self.captor

    def teardown_method(self, method):
        sys.stdout = sys.__stdout__
        print('method{}:'.format(method.__name__))
        del self.vm

    @pytest.mark.parametrize('money', [10, 50, 100, 500, 1000])
    def test_insert_available_money(self, capsys, money):
        self.vm.insert(money)
        assert capsys.readouterr().out == 'changes: 0\n'

    @pytest.mark.parametrize('money', [-1, 3, 11])
    def test_insert_unavailable_money(self, capsys, money):
        self.vm.insert(money)
        assert capsys.readouterr().out == 'changes: {}\n'.format(money)
