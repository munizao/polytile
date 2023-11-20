from itertools import product
from cell import Cell

class Board():
    def __init__(self, dims, holes) -> None:
        self.dims = dims
        self.holes = holes
    def __iter__(self):
        for cell in product(range(dim) for dim in self.dims):
            #TODO check for hole
            yield(cell)

    def contains(self, polycell):
        for cell in polycell:
            for i, coord in enumerate(cell):
                if coord < 0 or coord >= self.dims[i]:
                    return False
        return True
        #TODO handle holes
