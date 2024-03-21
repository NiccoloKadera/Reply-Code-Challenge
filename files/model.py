
from parameters import par
from global_variables import gv
from output import print_table


from setup import import_table, build_matrix, matrix_add_golden_points, matrix_add_silver_points

class model:

    def __init__(self) -> None:
        
        self.par = par()
        self.gv = gv()


    def run(self, path):
        
        import_table(self.par, self.gv, path) #'input_files/00-trailer.txt' 'input_files/01-comedy.txt'
        build_matrix(self.par, self.gv)
        
        

        matrix_add_golden_points(self.gv)
        matrix_add_silver_points(self.gv)
        
        print_table(self.gv)