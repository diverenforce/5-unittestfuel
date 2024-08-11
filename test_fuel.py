import pytest
import fuel

def test_convert_single_value():
    assert fuel.convert('3') == None
    assert fuel.convert('4.4') == None
    assert fuel.convert('a') == None