# Outline of Grid.py

def main():
  # open file for reading
  in_file = open ("grid.txt", "r")

  # read the dimension of the grid
  dim = in_file.readline()
  dim = dim.strip()
  dim = int (dim)

  # create an empty grid and populate it
  grid = []

  for i in range (dim):
    row = in_file.readline()
    row = row.strip()
    row = row.split()
    for j in range (dim):
      row[j] = int (row[j])
    grid.append (row)

   # print (grid)

  # close the file
  in_file.close()

  # read each row in blocks of four
  for row in grid:
    for i in range (0, len(row) - 3):
      for j in range (i, i + 4):
        print (row[j], end = "  ")
      print (end = "       ")
    print ()

  # read each column in blocks of four
  for j in range (dim):
    for i in range (0, dim - 3):
      for k in range (i, i + 4):
        print (grid[k][j], end = " ")
      print (end = "     ")
    print ()

  # read along major diagonal going L to R in blocks of four
  for i in range (dim - 3):
    for j in range (i, i + 4):
      print (grid[j][j], end = " ")
    print (end = "    ")
  print()

  # read along major diagonal going R to L in blocks of four
  for i in range (dim - 3):
    for j in range (i, i + 4):
      print (grid[j][dim - 1 - j], end = " ")
    print (end = "    ")
  print()

main()