def read_file(filename):
  """Reads the contents of a file.

  Args:
    filename: The name of the file to read.

  Returns:
    A list of strings containing the contents of the file.
  """

  with open(filename, "r") as f:
    file_data = f.read()
  file_data = file_data.split("\n")
  return file_data


def analyze_file(file_data):
  """Analyzes the contents of a file and returns a dictionary containing the following information:

  * highest_amount: The highest amount in the file.
  * lowest_amount: The lowest amount in the file.
  * total_cost: The total cost of all items in the file.
  * average_cost: The average cost of all items in the file.
  * item_details: A dictionary containing the details of all items in the file, including the item name and price.

  Args:
    file_data: A list of strings containing the contents of the file.

  Returns:
    A dictionary containing the analysis results.
  """

  highest_amount = float("-inf")
  lowest_amount = float("inf")
  total_cost = 0
  item_details = {}

  for item in file_data:
    item_name, item_price = item.split(",")
    item_price = float(item_price)

    if item_price > highest_amount:
      highest_amount = item_price
    if item_price < lowest_amount:
      lowest_amount = item_price

    total_cost += item_price

    item_details[item_name] = item_price

  average_cost = total_cost / len(item_details)

  analysis_results = {
    "highest_amount": highest_amount,
    "lowest_amount": lowest_amount,
    "total_cost": total_cost,
    "average_cost": average_cost,
    "item_details": item_details,
  }

  return analysis_results


def print_analysis_results(analysis_results):
  """Prints the analysis results to the console.

  Args:
    analysis_results: A dictionary containing the analysis results.
  """

  print("Highest amount:", analysis_results["highest_amount"])
  print("Lowest amount:", analysis_results["lowest_amount"])
  print("Total cost:", analysis_results["total_cost"])
  print("Average cost:", analysis_results["average_cost"])

  print("Item details:")
  for item_name, item_price in analysis_results["item_details"].items():
    print(f"{item_name}: {item_price}")


def main():
  """The main function of the program."""

  filename = "life-expectancy.csv"
  file_data = read_file(filename)

  analysis_results = analyze_file(file_data)

  print_analysis_results(analysis_results)


if __name__ == "__main__":
  main()