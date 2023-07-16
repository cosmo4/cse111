import pytest
from weight_balance_calc import calc_oil_weight, calc_moment, calc_fuel_weight, calc_center_of_gravity, calc_totals

def test_calc_oil_weight():
    assert round(calc_oil_weight(6), 1) == 10.8
    assert calc_oil_weight(0) == 0

def test_calc_fuel_weight():
    assert calc_fuel_weight(50) == 300
    assert calc_fuel_weight(0) == 0

def test_calc_moment():
    assert calc_moment(300, 95) == 28500
    assert calc_moment(0, 0) == 0

def test_calc_totals():
    assert calc_totals(1285.1, 11, 365, 300, 10, 50) == 2021.1
    assert calc_totals(0, 0, 0, 0, 0, 0) == 0

def test_calc_center_of_gravity():
    assert round(calc_center_of_gravity(2021.1, 176520.5), 1) == 87.3
    assert round(calc_center_of_gravity(2000, 170000), 1) == 85

pytest.main(["-v", "--tb=line", "-rN", __file__])
