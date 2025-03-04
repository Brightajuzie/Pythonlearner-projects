import pytest
from pytest import approx
# Constants
PVC_SCHED80_INNER_DIAMETER = 0.28687  # (meters)  11.294 inches
PVC_SCHED80_FRICTION_FACTOR = 0.013  # (unitless)
SUPPLY_VELOCITY = 1.65               # (meters / second)

HDPE_SDR11_INNER_DIAMETER = 0.048692 # (meters)  1.917 inches
HDPE_SDR11_FRICTION_FACTOR = 0.018   # (unitless)
HOUSEHOLD_VELOCITY = 1.75            # (meters / second)


def density_of_water():
  """Returns the density of water in kg/m^3"""
  return 998.2


def dynamic_viscosity_of_water():
  """Returns the dynamic viscosity of water in Pa*s"""
  return 0.0010016


def reynolds_number(hydraulic_diameter, fluid_velocity):
  """
  Calculates and returns the Reynolds number for a pipe.

  Args:
      hydraulic_diameter: The hydraulic diameter of the pipe in meters.
      fluid_velocity: The velocity of the water flowing through the pipe in m/s.

  Returns:
      The Reynolds number.
  """
  density = density_of_water()
  viscosity = dynamic_viscosity_of_water()
  return density * hydraulic_diameter * fluid_velocity / viscosity


def pressure_loss_from_fittings(fluid_velocity, quantity_fittings):
  """
  Calculates the water pressure lost because of pipe fittings.

  Args:
      fluid_velocity: The velocity of the water flowing through the pipe in m/s.
      quantity_fittings: The number of fittings in the pipeline.

  Returns:
      The pressure loss in kilopascals.
  """
  density = density_of_water()
  pressure_loss = -0.04 * density * fluid_velocity**2 * quantity_fittings / 2000
  return pressure_loss


def pressure_loss_from_pipe_reduction(larger_diameter,
                                       fluid_velocity, reynolds_number, smaller_diameter):
  """
  Calculates the water pressure lost because of a pipe diameter reduction.

  Args:
      larger_diameter: The diameter of the larger pipe in meters.
      fluid_velocity: The velocity of the water flowing through the larger pipe in m/s.
      reynolds_number: The Reynolds number for the flow in the larger pipe.
      smaller_diameter: The diameter of the smaller pipe in meters.

  Returns:
      The pressure loss in kilopascals.
  """
  k = 0.1 + 50 / (reynolds_number * larger_diameter / smaller_diameter)**4 - 1
  density = density_of_water()
  pressure_loss = -k * density * fluid_velocity**2 / 2000
  return pressure_loss



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