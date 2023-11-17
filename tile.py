from ortools.sat.python import cp_model
from syms import *
from connections import *


class Poly(tuple):
    '''Base polyomino class.'''
    def __new__(cls, seq, syms = two_sided, connections = wazir):
        return super().__new__(cls, tuple(seq))
    def __init__(self, seq, syms = two_sided, connections = wazir):
        self.syms = syms
        self.connections = connections
        super().__init__()

    # def __eq__(self, other):
    #     return tuple.__eq__(self.canonicalize(), other.canonicalize())
    # def __ne__(self, other):
    #     return tuple.__ne__(self.canonicalize(), other.canonicalize())
    # def __gt__(self, other):
    #     return tuple.__gt__(self.canonicalize(), other.canonicalize())
    # def __ge__(self, other):
    #     return tuple.__ge__(self.canonicalize(), other.canonicalize())
    # def __lt__(self, other):
    #     return tuple.__lt__(self.canonicalize(), other.canonicalize())
    # def __le__(self, other):
    #     return tuple.__le__(self.canonicalize(), other.canonicalize())
    # def __hash__(self):
    #     return tuple.__hash__(self.canonicalize())

    # This function, especially the list comprehension, is a hotspot,
    # and has been slightly optimized for speed.
    def canonpos(self):
        '''Determine the canonical position of a polyform in the plane.'''
        poly = list(self)
        poly.sort()
        if poly[0] == (0,0):
            return Poly(poly)
        x_min, y_min = poly[0]
        return Poly([(x - x_min, y - y_min) for x, y in poly])

        
    is_canonical = False
    var = None
    
    # def canonicalize(self):
    #     '''Cache canonicalization.'''
    #     if self.is_canonical:
    #         return self
    #     else:
    #         return self.canonpos()
    
    canon_dict = {}
    def canonicalize(self):
        if self.is_canonical:
            return self
        
        symforms = []
        min_symform = None
        for sym in self.syms:
            curr_symform = self.__class__([sym(*cell) for cell in self]).canonpos()
            t_curr_symform = tuple(curr_symform)
            if t_curr_symform in self.canon_dict:
                return self.canon_dict[t_curr_symform]
            symforms.append(t_curr_symform)
            if not min_symform or curr_symform < min_symform:
                min_symform = curr_symform
        
        out = self.__class__(min_symform, syms = self.syms, connections = self.connections)
        
        for i in symforms:
            self.canon_dict[i] = out
                
        out.is_canonical = True
        return out
    
    def enlargements(self):
        '''A generator yielding all polyforms that can be made by adding a cell adjacent to this polyform.''' 
        used_neighbors = set()
        for cell in self:
            for i in self.connections:
                neighbor = i(*cell)
                if neighbor not in self and neighbor not in used_neighbors:
                    used_neighbors.add(neighbor)
                    out = list(self)
                    out.append(neighbor)
                    out.sort()
                    out = self.__class__(out, syms = self.syms, connections = self.connections)
                    yield (neighbor, out)
    
    def translate(self, coords):
        dim = len(self[0]) #probably make this a class attribute
        if dim != len(coords):
            print("translate: coords have wrong dimension")
            return False #actually, figure out how errors work in Python
        return self.__class__([[cell[a] + coords[a] for a in range(dim)] for cell in self])
    
    @classmethod
    def n_ominoes(cls, n, syms = two_sided, connections = wazir):
        '''Returns a list of n-ominoes, that is, shapes with n connected cells.'''
        n_omino_list = []     
        for i in range(n):
            prev_n_omino_list = n_omino_list
            n_omino_list = []            
            if i == 0:
                n_omino_list.append(cls(((0,0),), syms, connections))
            else:
                for poly in prev_n_omino_list:
                    for enlargement in poly.enlargements():
                        newpoly = enlargement[1].canonicalize()
                        if newpoly not in n_omino_list:
                            n_omino_list.append(newpoly)

        return n_omino_list

if __name__ == "__main__":
    for i in range(1, 11):
        print(len(Poly.n_ominoes(i, syms=one_sided)))