wazir = [lambda x, y : (x + 1, y),
         lambda x, y : (x, y + 1),
         lambda x, y : (x - 1, y),
         lambda x, y : (x, y - 1),]

ferz = [lambda x, y : (x + 1, y + 1),
        lambda x, y : (x - 1, y + 1),
        lambda x, y : (x + 1, y - 1),
        lambda x, y : (x - 1, y - 1)]

king = wazir + ferz

#TODO Knight, alfil, dababba, hex stuff
