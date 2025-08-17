# 1. Python program to print a simple grid using lists.

def print_grid(grid):
  """
  This function prints a grid represented by a list of lists.
  Each inner list represents a row.
  """
  print("--- Simple Grid ---")
  for row in grid:
    # Join each element in the row with a space for neat printing
    print(" ".join(row))
  print("-------------------")

# --- Main part of the program ---
if __name__ == "__main__":
  # Define a 3x4 grid using a list of lists
  # You can change the characters to create different patterns
  sample_grid = [
      ['.', '#', '.', '.'],
      ['.', '.', '#', '.'],
      ['#', '#', '.', '.']
  ]

  # Call the function to print the grid
  print_grid(sample_grid)

  # Another example of a grid
  another_grid = [
      ['A', 'B', 'C'],
      ['D', 'E', 'F'],
      ['G', 'H', 'I']
  ]
  print_grid(another_grid)