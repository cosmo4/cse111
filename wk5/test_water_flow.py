from water_flow import water_column_height, pressure_gain_from_water_height, pressure_loss_from_pipe, pressure_loss_from_fittings, reynolds_number, pressure_loss_from_pipe_reduction
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

def test_pressure_lost_from_fittings():
    loss = pressure_loss_from_fittings(0, 3)
    assert loss == 0
    loss = pressure_loss_from_fittings(1.65, 0)
    assert loss == 0
    loss = pressure_loss_from_fittings(1.65, 2)
    assert loss == approx(-0.109, abs=0.001)
    loss = pressure_loss_from_fittings(1.75, 2)
    assert loss == approx(-0.122, abs=0.001)
    loss = pressure_loss_from_fittings(1.75, 5)
    assert loss == approx(-0.306, abs=0.001)

def test_reynolds_number():
    num = reynolds_number(0.048692, 0)
    assert num == 0
    num = reynolds_number(0.048692, 1.65)
    assert num == approx(80069, abs=1)
    num = reynolds_number(0.048692, 1.75)
    assert num == approx(84922, abs=1)
    num = reynolds_number(0.28687, 1.65)
    assert num ==approx(471729, abs=1)
    num = reynolds_number(0.28687, 1.75)
    assert num ==approx(500318, abs=1)

def test_pressure_loss_from_pipe_reduction():
    loss = pressure_loss_from_pipe_reduction(0.28687, 0, 1, 0.048692)
    assert loss == 0
    loss = pressure_loss_from_pipe_reduction(0.28687, 1.65, 471729, 0.048692)
    assert loss == approx(-163.744, abs=0.001)
    loss = pressure_loss_from_pipe_reduction(0.28687, 1.75, 500318, 0.048692)
    assert loss == approx(-184.182, abs=0.001)


pytest.main(["-v", "--tb=line", "-rN", __file__])