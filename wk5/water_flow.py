from pytest import approx
import pytest

def water_column_height(tower_height, tank_height):
    """
    Returns the height of the water column based on tower and tank height as a float

    Parameters:
        tower_height: (float) the height of the water tower
        tank_height: (float) the height of the tank of water
    """
    return tower_height + (3 * tank_height) / 4

def pressure_gain_from_water_height(height):
    """
    Returns the calculated pressure caused by gravity

    Parameter:
        height: (float) height of water column in meters
    """
    return (998.2 * 9.80665 * height) / 1000

def pressure_loss_from_pipe(pipe_diameter, pipe_length, friction_factor, fluid_velocity):
    """
    Returns calculated pressure loss from friction within a pipe

    Parameters:
        pipe_diameter: (float) diameter of a pipe in meters
        pipe_length: (float) length of pipe in meters
        friction_factor: (float) pipe's friction factor
        fluid_velocity: (float) velocity of fluid flowing through the pipe in meters/second
    """
    return (-1 * friction_factor * pipe_length * 998.2 * (fluid_velocity ** 2)) / (2000 * pipe_diameter)