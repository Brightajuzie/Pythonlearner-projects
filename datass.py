def read_file(filename):
  """Reads the contents of a file.

  Args:
    filename: The name of the file to read.

  Returns:
    A string containing the contents of the file.
  """

  with open(filename, "r") as f:
    file_data = f.read()
  return file_data

def print_file_data(file_data):
  """Prints the contents of a file to the console.

  Args:
    file_data: A string containing the contents of the file.
  """

  print(file_data)

def split_data(file_data):
  """Splits the contents of a file into a list of strings.

  Args:
    file_data: A string containing the contents of the file.

  Returns:
    A list of strings containing the split data.
  """

  split_data = file_data.split()
  return split_data

def print_max_and_min_numbers(split_data):
  """Prints the item with the maximum and minimum number in a list of strings.

  Args:
    split_data: A list of strings containing the split data.
  """

  max_number = max(split_data)
  min_number = min(split_data)

  print("The item with the maximum number is:", max_number)
  print("The item with the minimum number is:", min_number)

if __name__ == "__main__":
  filename = "life-expectancy.csv"

  file_data = read_file(filename)
  print_file_data(file_data)

  split_data = split_data(file_data)
  print_max_and_min_numbers(split_data)
