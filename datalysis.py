# This finds the minimum and maximum life expectancy values in the life-expectancy in the file.


# Impors python built in library
import csv

def life_expectancy(file_path):
  """
  Author: Mazi Bright Chidozie Onyekachi
  
  This application Reads File and outputs various data therein.
  
  calculates Life expectancy per year etc.
  
  Identifies the year and country that has the largest drop from one year to the next.

  """

  # Opens the file.
  with open(file_path, "r") as datum:
    reader = csv.reader(datum)
    
    
    # Skips the header row.
    next(reader)

    # ITERATION: This Iterates over the lines of the file.
    country = ""
    year = 0
    life_expectancy = 0
    previous_life_expectancy = 0
    largest_drop = 0
    largest_drop_country = ""
    largest_drop_year = 0
    for row in reader:
      # Gets current country, year, and life expectancy.
      country = row[0]
      year = int(row[2])
      life_expectancy = float(row[3])

      # Calculate the change in life expectancy from the previous year.
      life_expectancy_change = life_expectancy - previous_life_expectancy

      # Update the largest drop if necessary.
      if life_expectancy_change < largest_drop:
        largest_drop = life_expectancy_change
        largest_drop_country = country
        largest_drop_year = year

      # Update the previous life expectancy.
      previous_life_expectancy = life_expectancy

    return largest_drop_country, largest_drop_year

# Identify the country and year with the largest negative change in life expectancy.
largest_drop_country, largest_drop_year = life_expectancy("life-expectancy.csv")

# Print the country and year to the user.
print("The country and year with the largest drop in life expectancy are:", largest_drop_country, largest_drop_year)
print("The country and year with the largest drop in life expectancy are:", largest_drop_country, largest_drop_year)

minimum = 9999
minimum_country = ''
minimum_year = 0
maximum = 0
maximum_country = ''
maximum_year = 0

age_list = []
spec_min_age = 9999
spec_min_country = ''
spec_max_age = 0
spec_max_country = ''

selected_year = int(input('Input the year of interest: ').strip())

# Open the life-expectancy.csv file in read mode.
with open('life-expectancy.csv') as expectancy_data:
    
    # Iterate over the lines of the file.
    for i, line in enumerate(expectancy_data):
        if i == 0:
            continue
# Splits the line into a list of values, separated by commas
        line = line.strip()
        data = line.split(',')
        country = data[0]
        year = int(data[2])
        age = float(data[3])

        # Maximum life expectancy
        if age > maximum:
            maximum = age
            maximum_country = country
            maximum_year = year

        # Minimum life expectancy
        if age < minimum:
            minimum = age
            minimum_country = country
            minimum_year = year

        # Life expectancy for the year selected
        if year == selected_year:
            if not age_list:
                age_list.append(age)
            else:
                age_list.append(age)

            # Min life expectancy for the selected year
            if age < spec_min_age:
                spec_min_age = age
                spec_min_country = country

            # Max life expectancy for the selected year
            if age > spec_max_age:
                spec_max_age = age
                spec_max_country = country

spec_avg = sum(age_list) / len(age_list)

print(f'\n Overall maximum life expectancy is: {maximum} from {maximum_country} in {maximum_year}.')
print(f'\n Overall minimum life expectancy is: {minimum} from {minimum_country} in {minimum_year}.')

print(f'\nFor the year {selected_year}:')
print(f'The average life expentancy across all countries was {spec_avg:.2f}')

# Print the minimum and maximum life expectancy values to the user.
print(f'Maximum life expentancy was in" {spec_max_country} with {spec_max_age}')
print(f'Minimum life expentancy was in {spec_min_country} with {spec_min_age}')
