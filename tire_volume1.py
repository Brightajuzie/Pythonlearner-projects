import math
from datetime import date

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

# Initialize total volume
total_volume = 0

# Loop to get data for multiple tires (replace 'Y' with your desired stopping condition)
while input("Enter another tire (Y/N)? ").upper() == 'Y':
  # Get user input for tire dimensions
  width_mm = float(input("Enter the tire width in millimeters (e.g., 205): "))
  aspect_ratio = int(input("Enter the aspect ratio of the tire (e.g., 60 for 60%): "))
  diameter_inch = float(input("Enter the diameter of the wheel in inches (e.g., 15): "))

  # Calculate volume for this tire
  volume_liters = calculate_tire_volume(width_mm, aspect_ratio, diameter_inch)

  # Add volume to total
  total_volume += volume_liters

# Print the total volume with rounding
print(f"The total volume of air for all tires is {total_volume:.2f} liters.")

# Get current date
today = date.today().strftime("%Y-%m-%d")

# Open the file for appending
try:
  with open("volumes.txt", "a") as file:
    # Append data to the file
    file.write(f"{today}, {total_volume:.2f}\n")  # Append total volume with rounding
    print("Tire data successfully appended to volumes.txt")
except FileNotFoundError:
  print("volumes.txt not found. Tire data not saved.")

# Gets yours choice for the purchase of tire. (Optional - Can be commented out)
Question1 = input('Will you want to buy the tire of such volume?,Y/N ')
if Question1 == "Y":
  # Display prices (Optional)
  print("Here are the available tire options:")
  price1 = 20  # Price in dollars for Michelin tire
  price2 = 30  # Price in dollars for AbaMade tire
  print(f"  - Michelin tire: ${price1}")
  print(f"  - AbaMade tire: ${price2}")

  # Get user's choice (Optional)
  tire_choice = input("Enter the number (1 or 2) corresponding to your tire choice: ")

  # Print confirmation message based on user's choice (Optional)
  if tire_choice == '1':
    print("Congratulations! You've purchased a Michelin tire.")
  elif tire_choice == '2':
    print("Congratulations! You've purchased an AbaMade tire.")
  else:
    print("Invalid choice. Please enter 1 or 2.")
else:
  print("Happy shopping!")
