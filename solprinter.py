from ortools.sat.python import cp_model

class SolPrinter(cp_model.CpSolverSolutionCallback):
    def __init__(self, board):
        self.board = board
        super().__init__()

    def OnSolutionCallback(self):
        for row in self.board:
            for entry in row:
                print(self.Value(entry))