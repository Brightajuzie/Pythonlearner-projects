import csv
import os

def read_file(file_name):
  """Reads data from a file and returns a list of rows."""
  data = []
  with open("life-expectancy.csv") as f:
    reader = csv.reader(f)
    for row in reader:
      data.append(row)
  return data

def get_lowest_and_highest_life_expectancy(data):
  """Finds the lowest and highest values for life expectancy in the given list of rows."""
  lowest_life_expectancy = float("inf")
  highest_life_expectancy = float("-inf")
  lowest_life_expectancy_year = None
  highest_life_expectancy_year = None
  lowest_life_expectancy_country = None
  highest_life_expectancy_country = None

  for row in data:
    year = int(row[0])
    country = row[1]
    life_expectancy = float(row[2])

    if life_expectancy < lowest_life_expectancy:
      lowest_life_expectancy = life_expectancy
      lowest_life_expectancy_year = year
      lowest_life_expectancy_country = country
    elif life_expectancy > highest_life_expectancy:
      highest_life_expectancy = life_expectancy
      highest_life_expectancy_year = year
      highest_life_expectancy_country = country

  return lowest_life_expectancy, lowest_life_expectancy_year, lowest_life_expectancy_country, highest_life_expectancy, highest_life_expectancy_year, highest_life_expectancy_country

def main():
  """Reads a file and finds the lowest and highest values for life expectancy in the dataset, and displays both values, prints the year and the country for that value."""

 # file_name = "life_expectancy.csv"

  # Download the dataset if it doesn't exist.
 # if not os.path.exists(file_name):
   # print("Downloading the life expectancy dataset...")
   # import requests
   # url = "https://raw.githubusercontent.com/datasets/life-expectancy/master/data/life-expectancy.csv"
    #with open(file_name, "wb") as f:
    #  response = requests.get(url)
     # f.write(response.content)
    #print("Download complete.")

  # Load the dataset into the program.
  data = read_file("life-expectancy.csv")

  # Find the lowest and highest values for life expectancy in the dataset.
  lowest_life_expectancy, lowest_life_expectancy_year, lowest_life_expectancy_country, highest_life_expectancy, highest_life_expectancy_year, highest_life_expectancy_country = get_lowest_and_highest_life_expectancy(data)

  # Display the lowest and highest values for life expectancy, and the year and country for that value.
  print("The lowest life expectancy is {} in {} {}.".format(lowest_life_expectancy, lowest_life_expectancy_year, lowest_life_expectancy_country))
  print("The highest life expectancy is {} in {} {}.".format(highest_life_expectancy, highest_life_expectancy_year, highest_life_expectancy_country))

if __name__ == "__main__":
  main()
