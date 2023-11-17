from itertools import product

class Cell(tuple):
    cache = {}
    def __new__(cls, coords):
        cell = Cell.cache.get(coords)
        if cell:
            return cell
        cell = super(Cell, cls).__new__(cls)
        cell.aspects = []
        cls.cache[coords] = cell

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
