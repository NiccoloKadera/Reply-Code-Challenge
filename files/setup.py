
import numpy as np
from elements import golden_point, silver_point, tile


def import_table(par, gv, file_path):
    
    with open(file_path, 'r', encoding='utf-8-sig') as f:
        content_row = f.read().splitlines()

        row_one = content_row[0].split(' ')
        par.W = int(row_one[0])
        par.H = int(row_one[1])
        
        par.G_n = int(row_one[2])
        par.S_m = int(row_one[3])
        par.T_l = int(row_one[4])

        for i in range(1, par.G_n):
            row = content_row[i].split(' ')
            g = golden_point()
            g.x = int(row[0])
            g.y = int(row[1])
            gv.golden_points.append(g)

        
        for i in range(1 + par.G_n, 1 + par.G_n + par.S_m):
            row = content_row[i].split(' ')
            s = silver_point()
            s.x = int(row[0])
            s.y = int(row[1])
            s.score = int(row[2])
            gv.silver_points.append(s)


        for i in range(1 + par.G_n + par.S_m, 1 + par.G_n + par.S_m + par.T_l):
            row = content_row[i].split(' ')
            for i in range(0, int(row[2])):
                t = tile()
                t.id = row[0]
                t.cost = int(row[1])
                gv.tiles.append(t)

def build_matrix(par, gv):
    

    gv.matrix = np.empty((par.W, par.H), dtype=object)
    
    
def setup_matrix(par, gv, file_path):
    with open(file_path, 'r', encoding='utf-8-sig') as f:
        content_row = f.read().splitlines()
    
def matrix_add_golden_points(gv):
    
    for g in gv.golden_points:
        gv.matrix[g.x, g.y] = g
        

def matrix_add_silver_points(gv):
    for s in gv.silver_points:
        gv.matrix[s.x, s.y] = s