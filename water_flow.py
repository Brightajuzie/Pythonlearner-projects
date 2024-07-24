from pytest import approx
import pytest

def test_water_column_height():
  """
  Tests the water_column_height function with various inputs.
  """
  # Test data
  tower_heights = [0.0, 0.0, 25.0, 48.3]
  tank_wall_heights = [0.00, 10.0, 0.0, 12.8]
  expected_heights = [0.0, 7.5, 25.0, 57.9]

  for i in range(len(tower_heights)):
    actual_height = water_column_height(tower_heights[i], tank_wall_heights[i])
    assert actual_height == approx(expected_heights[i])

def test_pressure_gain_from_water_height():
  """
  Tests the pressure_gain_from_water_height function with various inputs.
  """
  # Test data
  heights = [0.0, 30.2, 50.0]
  expected_pressures = [0.000, 295.628, 489.450]

  for i in range(len(heights)):
    actual_pressure = pressure_gain_from_water_height(heights[i])
    assert actual_pressure == approx(expected_pressures[i])

def test_pressure_loss_from_pipe():
  """
  Tests the pressure_loss_from_pipe function with various inputs.
  """
  # Test data
  pipe_diameters = [0.048692, 0.048692, 0.048692, 0.048692, 0.048692, 0.286870, 0.286870]
  pipe_lengths = [0.00, 200.00, 200.00, 200.00, 200.00, 1000.00, 1800.75]
  friction_factors = [0.018, 0.00, 0.018, 0.018, 0.018, 0.013, 0.013]
  fluid_velocities = [1.75, 1.75, 0.00, 1.75, 1.65, 1.65, 1.65]  # Added missing closing parenthesis

  for i in range(len(pipe_diameters)):
    actual_pressure_loss = pressure_loss_from_pipe(pipe_diameters[i], pipe_lengths[i], friction_factors[i], fluid_velocities[i])
    # You might want to assert against expected pressure loss here (assuming you have those values)
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