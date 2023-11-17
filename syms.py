two_sided = [lambda x, y : ( x,  y),
             lambda x, y : (-x,  y),
             lambda x, y : ( x, -y),
             lambda x, y : (-x, -y),
             lambda x, y : ( y,  x),
             lambda x, y : (-y,  x),
             lambda x, y : ( y, -x),
             lambda x, y : (-y, -x)]

one_sided = [lambda x, y : ( x,  y),
             lambda x, y : ( y, -x),
             lambda x, y : (-x, -y),
             lambda x, y : (-y, x)]

rectangular = [lambda x, y : ( x,  y),
               lambda x, y : ( x,  y),
               lambda x, y : ( x, -y),
               lambda x, y : (-x, -y)]

rhombic = [lambda x, y : ( x,  y),
        lambda x, y : ( y,  x),
        lambda x, y : (-y, -x),
        lambda x, y : (-x, -y)]

fixed = [lambda x, y : ( x,  y)]