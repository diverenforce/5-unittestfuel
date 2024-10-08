import pytest
import fuel

def test_convert_single_value():
    assert fuel.convert('3') == None
    assert fuel.convert('4.4') == None
    assert fuel.convert('a') == None

def test_convert_zero():
    assert fuel.convert('4/0') == None
    assert fuel.convert('1/0') == None
    assert fuel.convert('0/0') == None

def test_convert_value():
    assert fuel.convert('yes/no') == None
    assert fuel.convert('please') == None
    assert fuel.convert('1.5/3') == None

def test_convert_over():
    assert fuel.convert('5/4') == None

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