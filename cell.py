class Cell(tuple):
    cache = {}
    def __new__(cls, coords):
        cell = Cell.cache.get(coords)
        if cell:
            return cell
        cell = super(Cell, cls).__new__(cls)
        cell.aspect_vars = []
        cls.cache[coords] = cell