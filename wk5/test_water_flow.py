from water_flow import water_column_height, pressure_gain_from_water_height, pressure_loss_from_pipe
from pytest import approx
import pytest


def test_water_column_height():
    column_height = water_column_height(0, 0)
    assert column_height == 0
    column_height = water_column_height(0, 10)
    assert column_height == 7.5
    column_height = water_column_height(25, 0)
    assert column_height == 25
    column_height = water_column_height(48.3, 12.8)
    assert column_height == approx(57.9, abs=0.1)

def test_pressure_gain_from_water_height():
    pressure = pressure_gain_from_water_height(0)
    assert pressure == approx(0, abs=0.001)
    pressure = pressure_gain_from_water_height(30.2)
    assert pressure == approx(295.628, abs=0.001)
    pressure = pressure_gain_from_water_height(50)
    assert pressure == approx(489.450, abs=0.001)

def test_pressure_loss_from_pipe():
    loss = pressure_loss_from_pipe(0.048692, 0, 0.18, 1.75)
    assert loss == approx(0, abs=0.001)
    loss = pressure_loss_from_pipe(0.048692, 200, 0, 1.75)
    assert loss == approx(0, abs=0.001)
    loss = pressure_loss_from_pipe(0.048692, 200, 0.018, 0)
    assert loss == approx(0, abs=0.001)
    loss = pressure_loss_from_pipe(0.048692, 200, 0.018, 1.75)
    assert loss == approx(-113.008, abs=0.001)
    loss = pressure_loss_from_pipe(0.048692, 200, 0.018, 1.65)
    assert loss == approx(-100.462, abs=0.001)
    loss = pressure_loss_from_pipe(0.28687, 1000, 0.013, 1.65)
    assert loss == approx(-61.576, abs=0.001)
    loss = pressure_loss_from_pipe(0.28687, 1800.75, 0.013, 1.65)
    assert loss == approx(-110.884, abs=0.001)


pytest.main(["-v", "--tb=line", "-rN", __file__])