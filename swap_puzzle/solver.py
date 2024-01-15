from grid import Grid

class Solver(): 
    """
    A solver class, to be implemented.
    """
    def find_path(cell1, cell2):
        a1, b1 = cell1
        a2, b2 = cell2
        liste = []
        if a2 > a1:
            for k in range(a2 - a1 + 1):
                liste.append((a2 - k, b2))
        if a1 > a2:
            for k in range(a1 - a2 + 1):
                liste.append((a2 + k, b2))
        if b2 > b1:
            for k in range(b2 - b1 + 1):
                liste.append((a1, b2 - k))
        if b1 > b2:
            for k in range(b1 - b2 + 1):
                liste.append((a1, b2 + k))



    def get_solution(self):
        """
        Solves the grid and returns the sequence of swaps at the format 
        [((i1, j1), (i2, j2)), ((i1', j1'), (i2', j2')), ...]. 
        """
        n = self.n
        m = self.m
        i = 0
        j = 0
        while not (Grid.is_sorted(self.state)):
            if j < m:
                if 


