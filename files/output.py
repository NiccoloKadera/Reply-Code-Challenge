import numpy as np

def output_terminal():
    pass


def draw_labirint():
    pass

def print_table(gv):
    matrix_pre = gv.matrix
    
    matrix_print = []
    for el in matrix_pre:
        row = []
        for i in el:
            if i == None:
                row.append('0')
            else:
                row.append(str(i))
        print(row)
        matrix_print.append(row)
    return matrix_print