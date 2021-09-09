
if __name__ == '__main__':
	from pulp import*
	import pandas as pd
	import numpy as np
	from SudokuBase import *

	filename = input('Please enter the file name of the puzzle you want to solve (Comma Delimited/Txt):  ')
	puzzle = np.array(pd.read_csv(filename,header=None))
	ii = 0
	for i in puzzle:
		jj = 0
		for j in i:
			if j !=0:
				prob += possible_vals[ii][jj] == j,""
			jj+=1
		ii+=1
	prob.solve()
	output_solution()
	print('Your solution can be found under the filename "sudokuout.txt"')