#coding=utf-8
#!/usr/bin/python
#
#Time:2016-07-11
#Author:William
#Exercixe:6.16
#The maxtrix a X matrix b and matrix(a)+matrix(b);
def matrix_input(string, m, n):
    matrix = []
    a = string.split(',')
    for i in range(m * n):
        matrix.append(a[i])
    return matrix

def matrix_display(matrix, m, n):
    for i in range(m):
        for j in range(n):
            print matrix[i * n + j],
        print '\r'


M_row = int(raw_input('The number of rows: ... '))
C_column = int(raw_input('The number of cloumns: ... '))
matrix_M_string = raw_input('Please input the M matrix (in list, row by row): ... ')
matrix_M = matrix_input(matrix_M_string, M_row, C_column)

matrix_N_string = raw_input('Please input the N matrix (in list, row by row): ... ')
matrix_N = matrix_input(matrix_N_string, M_row, C_column)
# From cnblogs.com/balian/
matrix_C = []

for i in range(M_row * C_column):
    matrix_C.append(int(matrix_M[i]) + int(matrix_N[i]))

print 'Matrix M:'
matrix_display(matrix_M, M_row, C_column)

print 'Matrix N:'
matrix_display(matrix_N, M_row, C_column)

print 'M + N:'
matrix_display(matrix_C, M_row, C_column)
