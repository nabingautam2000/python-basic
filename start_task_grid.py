# 2. Python program to read an ASCII grid, find the start 'S',
#    and list all task cells 'T'.

def find_special_cells(grid):
  """
  This function finds the coordinates of the 'S' (start) and all 'T' (task)
  cells in a given grid.

  Args:
    grid: A list of strings representing the grid.

  Returns:
    A tuple containing the start coordinates (row, col) and a list of
    task coordinates [(row1, col1), (row2, col2), ...].
    Returns (None, []) if 'S' is not found.
  """
  start_coords = None
  task_coords = []

  # Enumerate through the grid to get both index (row number) and value (row content)
  for r_idx, row in enumerate(grid):
    # Enumerate through the row string to get index (column number) and character
    for c_idx, char in enumerate(row):
      if char == 'S':
        start_coords = (r_idx, c_idx)
      elif char == 'T':
        task_coords.append((r_idx, c_idx))

  return start_coords, task_coords

# --- Main part of the program ---
if __name__ == "__main__":
  # Define an ASCII grid as a list of strings
  ascii_grid = [
      "#.T.#",
      "#..S#",
      "#T..#",
      "#####",
      ".T..."
  ]

  # Find the start and task cells
  start, tasks = find_special_cells(ascii_grid)

  # Print the results
  print("--- Grid Analysis ---")
  print("Grid:")
  for row in ascii_grid:
      print(row)
  print("---------------------")

  if start:
    print(f"Start 'S' found at: {start}")
  else:
    print("Start 'S' not found in the grid.")

  if tasks:
    print(f"Task 'T' cells found at: {tasks}")
  else:
    print("No Task 'T' cells found in the grid.")
