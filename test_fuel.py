import pytest
import fuel

def test_convert_single_value():
    assert fuel.convert('3') == ''
    assert fuel.convert('4.4') == ''
    assert fuel.convert('a') == ''

def test_convert_zero():
    assert fuel.convert('4/0') == ''
    assert fuel.convert('1/0') == ''
    assert fuel.convert('0/0') == ''

def test_convert_value():
    assert fuel.convert('yes/no') == ''
    assert fuel.convert('please') == ''
    assert fuel.convert('1.5/3') == ''

def test_convert_over():
    assert fuel.convert('5/4') == ''

def test_convert_valid():
    assert fuel.convert('1/2') == 50
    assert fuel.convert('3/4') == 75
 
def test_gauge_full():
    assert fuel.gauge(99) == 'F'
    assert fuel.gauge(100) == 'F'

def test_gauge_empty():
    assert fuel.gauge(1) == 'E'
    assert fuel.gauge(0) == 'E'

def test_gauge():
    assert fuel.gauge(23) == '23%'
    assert fuel.gauge(54) == '54%'