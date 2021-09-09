from pulp import *

rnge = range(0,9)
Rows = list(rnge)
Cols = list(rnge)	

possible_vals = LpVariable.dicts("PossibleVals",(Rows,Cols,),1,9,LpInteger)

binaries = LpVariable.dicts("PossibleVals",(Rows,Cols,range(36),range(3)),0,1,LpInteger)

C = 9 # C = X_max -1 + X_min

# Define the problem
prob = LpProblem("SudokuProblem",LpMinimize)
# Add objective function
prob += 0

# Get index of box entries
Boxes =[]
for i in range(3):
    for j in range(3):
        Boxes += [[(Rows[3*i+k],Cols[3*j+l]) for k in range(3) for l in range(3)]]

# Absolute value constraints or not natively linear, so to establish a "not equal"
# Relation between two puzzle entries we need to do a work around
# Using:
# -(x_i - x_j) + C * Binary_ij >= 1
# x_i - x_j + C* (1-Binary_ij) >= 1
# We need to create n(n-1)/2 pair-wise comparisons for each system (i.e. each row/col/box)
# Hence, we need 3*(9*36) constraints.
# This method is less efficient than the boolean way of solving the sudoku puzzle but
# I believe it is more intuitive when you are coming from a Mathematical background rather than natively 
# a programming background.

# This adds all the constraints for each Row, Col, Box
for r in Rows:
    counter = 0
    for c in Cols[:-1]:
        i = c
        while i < Cols[-1]:
            prob += lpSum([-possible_vals[r][c],possible_vals[r][i+1]]) + C*binaries[r][i+1][counter][0] >=1
            prob += lpSum([possible_vals[r][c],-possible_vals[r][i+1]]) + C*(1-binaries[r][i+1][counter][0]) >=1
            i+=1
            counter+=1
for c in Cols:
    counter = 0
    for r in Rows[:-1]:
        i = r
        while i < Rows[-1]:
            prob += lpSum([-possible_vals[r][c],possible_vals[i+1][c]]) + C*binaries[i+1][c][counter][1] >=1
            prob += lpSum([possible_vals[r][c],-possible_vals[i+1][c]]) + C*(1-binaries[i+1][c][counter][1]) >=1
            i+=1
            counter+=1
for j in range(len(Boxes)):
    counter=0
    for i in range(0,len(Boxes[j])):
        b1 = Boxes[j][i]
        jj = i+1
        while jj < len(Boxes[j]):
            b2 = Boxes[j][jj]
            prob += lpSum([-possible_vals[b1[0]][b1[1]],possible_vals[b2[0]][b2[1]]]) + C*binaries[b1[0]][b1[1]][counter][2] >=1
            prob += lpSum([possible_vals[b1[0]][b1[1]],-possible_vals[b2[0]][b2[1]]]) + C*(1-binaries[b1[0]][b1[1]][counter][2]) >=1
            counter+=1
            jj+=1


def output_solution():
    with open('sudokuout.txt', 'w') as sudokuout:
        for r in Rows:
            if r == 0 or r == 3 or r == 6:
                sudokuout.write("+-------+-------+-------+\n")
            for c in Cols:
                if c == 0 or c == 3 or c == 6:
                    sudokuout.write("| ")
                sudokuout.write(str(value(possible_vals[r][c])) + " ")
                if c == 8:
                    sudokuout.write("|\n")
        sudokuout.write("+-------+-------+-------+")
        sudokuout.close()
