import math

# Bright Chidozie Onyekachi tire_volume project
def calculate_tire_volume(width_mm, aspect_ratio, diameter_inch):
  """
  Calculates the approximate volume of a car tire in liters.

  Args:
      width_mm: Tire width in millimeters.
      aspect_ratio: Aspect ratio of the tire.
      diameter_inch: Diameter of the wheel in inches.

  Returns:
      The approximate volume of the tire in liters.
  """

  # Convert width from millimeters to meters
  width_m = width_mm / 1000

  # Convert diameter from inches to meters
  diameter_m = diameter_inch * 0.0254

  # Calculate the volume
  pi = math.pi
  volume = pi * width_m**2 * aspect_ratio * (aspect_ratio * width_m + 2540 * diameter_m) / 10**10

  return volume

# Get user input for tire dimensions
width_mm = float(input("Enter the tire width in millimeters : "))
aspect_ratio = float(input("Enter the aspect ratio of the tire : "))
diameter_inch = float(input("Enter the diameter of the wheel in inches : "))

# Calculate and print the volume
volume_liters = calculate_tire_volume(width_mm, aspect_ratio, diameter_inch)
print(f"The volume of the tire is {volume_liters:.2f} liters.")
