import math

# Sample tire data (width, aspect ratio, diameter)
tires = [
    (205, 55, 16),
    (225, 45, 17),
    (235, 60, 18),
]

# Define function to calculate tire volume
def calculate_tire_volume(width_mm, aspect_ratio, diameter_inch):
  """
  Calculates the approximate volume of air inside a car tire in liters.

  Args:
      width_mm: Tire width in millimeters.
      aspect_ratio: Aspect ratio of the tire (e.g., 60 for 60%).
      diameter_inch: Diameter of the wheel in inches.

  Returns:
      The approximate volume of the tire in liters.
  """

  # Convert width from millimeters to meters
  width_m = width_mm / 1000

  # Convert diameter to meters and account for potential overflow
  diameter_m_adjusted = diameter_inch / 100

  # pi value
  pi = math.pi

  # Calculate the volume
  volume = pi * width_m**2 * aspect_ratio * (aspect_ratio * width_m + 2540 * diameter_m_adjusted) / 10**10
  return volume

# Calculate volume for each tire and print results
for width, aspect_ratio, diameter in tires:
  volume_liters = calculate_tire_volume(width, aspect_ratio, diameter)
  print(f"Tire (width: {width}mm, aspect ratio: {aspect_ratio}%, diameter: {diameter}in): {volume_liters:.2f} liters")