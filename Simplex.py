import numpy as np

def Simplex(A,B,Z,Min=True):
    """
    Objective:
    This function uses the Simplex algorithm to optimize a linear program.

    Parameters:
        A: np.array
            A size m x n array containing the constraint coefficients of the linear program
        B: np.array
            A size m x 2 array containing the RHS of constraints and what inequality they use
        Z: np.array
            A size 1 x n array containing the Objective function coefficients
        Max: Boolean
            Boolean saying whether we are maximizing or minimizing. True for Max, False for Min.
    
    Outputs: 
        Solved: np.array
            A size 1 x n array with the number of each variable requirerd for optimum solution.
        Obj: double
            The Objective value of the optimal solution.
    
    Notes:
    B should have the inequality signs (-1 for <=, 0 for =, 1 for >=) in the first column and RHS in the second.
    Solved will come in the same order as A is set out in.

    Author: Bruce Zhang

    """
    # Make the objective a minimization problem.
    if Min == False:
        Z = -1 * Z
    
    
    Obj = Z
    if Min == False:
        Obj = -1 * Obj





