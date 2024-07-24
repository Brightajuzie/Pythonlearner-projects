import csv
import os

def download_dataset(file_name, url):
  """Downloads the dataset from the given URL."""
  if not os.path.exists(file_name):
    print("Downloading the dataset from {}...".format(url))
    import requests
    response = requests.get(url)
    with open(file_name, "wb") as f:
      f.write(response.content)
    print("Download complete.")

def load_dataset(file_name):
  """Loads the dataset from the given file."""
  data = []
  with open(file_name, "r") as f:
    reader = csv.reader(f)
    for row in reader:
      data.append(row)
  return data

def iterate_through_dataset(data):
  """Iterates through the dataset line by line and splits each line into parts."""
  for row in data:
    parts = row.split(",")
    yield parts

def main():
  """Downloads the dataset from a file, loads the dataset in the program, iterates through the data line by line, and splits each line into parts."""

  file_name = "life-expectancy.csv"
  url = "https://example.com/dataset.csv"

  # Download the dataset if it doesn't exist.
  download_dataset(file_name, url)

  # Load the dataset into the program.
  data = load_dataset(file_name)

  # Iterate through the data line by line and split each line into parts.
  for parts in iterate_through_dataset(data):
    # Do something with the parts here.
    pass

if __name__ == "__main__":
  main()
