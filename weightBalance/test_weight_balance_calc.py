from weight_balance_calc import calc_oil_weight, calc_moment, calc_fuel_weight, calc_center_of_gravity, calc_totals
import pytest

def test_calc_oil_weight():
    oil_weight = round(calc_oil_weight(6))
    assert oil_weight == 11

def test_calc_moment():
    moment = calc_moment(300, 95)
    assert moment == 28500

def test_calc_center_of_gravity():
    cg = round(calc_center_of_gravity(2021.1, 176520.5), 1)
    assert cg == 87.3

def test_calc_fuel_weight():
    fuel = calc_fuel_weight(50)
    assert fuel == 300

def test_calc_totals():
    total = calc_totals(1285.1, 11, 365, 300, 10, 50)
    assert total == 2021.1

pytest.main(["-v", "--tb=line", "-rN", __file__])