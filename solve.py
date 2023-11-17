from ortools.sat.python import cp_model


def solve(tileset, board):
    model = cp_model.CpModel()
    for tile in tileset:
        tile.aspect_vars = []
        for sym in tile.syms:
            symtile = tile.__class__([sym(cell) for cell in tile])
            for x in board.dims[0]:
                for y in board.dims[1]:
                    aspect = symtile.translate(x, y)
                    if board.contains(aspect):
                        # tile.aspects.append(aspect)
                        aspect_var = model.NewBoolVar(repr(aspect))
                        tile.aspect_vars.append(aspect_var)
                        for cell in aspect:  # get the actual corresponding board cell
                            cell.aspect_vars.append(aspect_var)
    for cell in board:
        model.Add(sum(cell.aspect_vars) == 1)
    for tile in tileset:
        model.Add(sum(tile.aspect_vars) == 1)
