from pytest import approx
import pytest

EARTH_ACCELERATION_OF_GRAVITY = 9.80665
WATER_DENSITY = 998.2
WATER_DYNAMIC_VISCOSITY = 0.0010016

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
    return (WATER_DENSITY * EARTH_ACCELERATION_OF_GRAVITY * height) / 1000

def pressure_loss_from_pipe(pipe_diameter, pipe_length, friction_factor, fluid_velocity):
    """
    Returns calculated pressure loss from friction within a pipe

    Parameters:
        pipe_diameter: (float) diameter of a pipe in meters
        pipe_length: (float) length of pipe in meters
        friction_factor: (float) pipe's friction factor
        fluid_velocity: (float) velocity of fluid flowing through the pipe in meters/second
    """
    return (-1 * friction_factor * pipe_length * WATER_DENSITY * (fluid_velocity ** 2)) / (2000 * pipe_diameter)

def pressure_loss_from_fittings(fluid_velocity, quantity_fittings):
    """
    Returns the pressure lost from fittings of a pipe

    Parameters:
        fluid_velocity: (float) velocity of the fluid in meters per second
        quantity_fittings: (int) number of pipe fittings
    """
    return (-1 * 0.04 * WATER_DENSITY * (fluid_velocity ** 2) * quantity_fittings) / 2000

def reynolds_number(hydraulic_diameter, fluid_velocity):
    """
    Returns the unitless ratio of the inertial and viscous forces in a fluid

    Parameters:
        hydraulic_diameter: (float) the hydraulic diameter of a pipe in meters
        fluid_velocity: (float) the velocity of the fluid in meters per second
    """
    return (WATER_DENSITY * hydraulic_diameter * fluid_velocity) / WATER_DYNAMIC_VISCOSITY

def pressure_loss_from_pipe_reduction(larger_diameter, fluid_velocity, reynolds_number, smaller_diameter):
    """
    Returns the water pressure lost because of water moving from a pipe with a large diameter into a pipe with a smaller diameter

    Parameters:
        larger_diameter: (float) diameter of larger pipe in meters
        fluid_velocity: (float) the velocity of the fluid in meters per second
        reynolds_numbear: (int) the unitless ratio of the inertial and viscous forces in a fluid
        smaller_diameter: (float) diameter of smaller pipe in meters
    """
    k = (0.1 + (50 / reynolds_number)) * (((larger_diameter / smaller_diameter) ** 4) - 1)
    return (-1 * k * WATER_DENSITY * (fluid_velocity ** 2)) / 2000

PVC_SCHED80_INNER_DIAMETER = 0.28687 # (meters)  11.294 inches
PVC_SCHED80_FRICTION_FACTOR = 0.013  # (unitless)
SUPPLY_VELOCITY = 1.65               # (meters / second)

HDPE_SDR11_INNER_DIAMETER = 0.048692 # (meters)  1.917 inches
HDPE_SDR11_FRICTION_FACTOR = 0.018   # (unitless)
HOUSEHOLD_VELOCITY = 1.75            # (meters / second)


def main():
    tower_height = float(input("Height of water tower (meters): "))
    tank_height = float(input("Height of water tank walls (meters): "))
    length1 = float(input("Length of supply pipe from tank to lot (meters): "))
    quantity_angles = int(input("Number of 90° angles in supply pipe: "))
    length2 = float(input("Length of pipe from supply to house (meters): "))

    water_height = water_column_height(tower_height, tank_height)
    pressure = pressure_gain_from_water_height(water_height)

    diameter = PVC_SCHED80_INNER_DIAMETER
    friction = PVC_SCHED80_FRICTION_FACTOR
    velocity = SUPPLY_VELOCITY
    reynolds = reynolds_number(diameter, velocity)
    loss = pressure_loss_from_pipe(diameter, length1, friction, velocity)
    pressure += loss

    loss = pressure_loss_from_fittings(velocity, quantity_angles)
    pressure += loss

    loss = pressure_loss_from_pipe_reduction(diameter,
            velocity, reynolds, HDPE_SDR11_INNER_DIAMETER)
    pressure += loss

    diameter = HDPE_SDR11_INNER_DIAMETER
    friction = HDPE_SDR11_FRICTION_FACTOR
    velocity = HOUSEHOLD_VELOCITY
    loss = pressure_loss_from_pipe(diameter, length2, friction, velocity)
    pressure += loss

    print(f"Pressure at house: {pressure:.1f} kilopascals")


if __name__ == "__main__":
    main()