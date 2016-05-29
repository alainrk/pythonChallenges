'''
From: 2016 AIPO National Finals

Write a program that prints a chessboard with N rows and M columns with the following rules:
The top left cell must be an asterisk (*)
Any cell touching (left, right, up or down) a cell with an asterisk must be a dot (.)
Any cell touching (left, right, up or down) a cell with a dot must be an asterisk.
A chessboard of 8 rows and 8 columns printed using these rules would be:

*.*.*.*.
.*.*.*.*
*.*.*.*.
.*.*.*.*
*.*.*.*.
.*.*.*.*
*.*.*.*.
.*.*.*.*
Input

A single line with two integers N and M separated by spaces. The number N will represent the number of rows and M the number of columns. N and M will be between 1 and 10.
Output

Print N lines each containing M characters with the chessboard pattern.
'''

def chessboard(s, board = "", p = "*", q = "."):
    nrow, ncol = map(int,s.split(" "))
    for i in range(nrow):
        board += "".join([p if j%2 != 1 else q for j in range(ncol)])+("\n" if i<nrow-1 else "")
        p,q = q,p
    return board

print chessboard("1 1")
print chessboard("2 2")
print chessboard("3 4")
print chessboard("5 2")
print chessboard("7 7")
