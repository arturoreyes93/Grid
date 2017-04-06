#  File: Grid.py

#  Description: reads a text file with a nxn matrix and prints the greatest product of 4 consecutive numbers horizontally,vertically and diagonally

#  Student Name: Arturo Reyes Munoz

#  Student UT EID: ar48836

#  Course Name: CS 303E

#  Unique Number: 50865

#  Date Created: 04/14

#  Date Last Modified: 04/14

def main():

	file = open('grid.txt','r')

	n = file.readline()
	n = n.strip()
	n = int(n)

	grid = []

	for i in range(n):

		row = file.readline()
		row = row.strip()
		row = row.split()

		for j in range(n):

			row[j] = int(row[j])

		grid.append(row)

	file.close()

	maxprod = 0

	for i in grid:

		for j in range(n-3):

			prod = i[j]*i[j+1]*i[j+2]*i[j+3]

			if prod > maxprod:

				maxprod = prod

	for row in range(n-3):

		for col in range(n):

			prod = grid[row][col]*grid[row+1][col]*grid[row+2][col]*grid[row+3][col]

			if prod > maxprod :

				maxprod = prod

	for i in range(n-3):

		prod = grid[i][i]*grid[i+1][i+1]*grid[i+2][i+2]*grid[i+3][i+3]

		if prod > maxprod:

			maxprod = prod

	for i in range(n-1,2,-1):

		prod = grid[i][i]*grid[i-1][i-1]*grid[i-2][i-2]*grid[i-3][i-3]

		if prod > maxprod:

			maxprod = prod

	for row in range(n-1,2,-1):

		for col in range(n-3):

			prod = grid[row][col]*grid[row-1][col+1]*grid[row-2][col+2]*grid[row-3][col+3]

			if prod > maxprod:

				maxprod = prod

	for row in range(n-3):

		for col in range(n-1,2,-1):

			prod = grid[row][col]*grid[row+1][col-1]*grid[row+2][col-2]*grid[row+3][col-3]

			if prod > maxprod:

				maxprod = prod
		

	print('The greatest product is '+str(maxprod)+'.')



main()

# wrong from piazza : grid3, 