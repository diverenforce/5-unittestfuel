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
    assert fuel.convert('lovethewind') == None