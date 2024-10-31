import numpy as np

def requêtes(dim_wq: tuple, F: np.array):
    """Calculate query matrix Q = W_q @ F^T"""
    # Generate random weight matrix W_q
    W_q = np.random.rand(*dim_wq)
    
    # Calculate Q = W_q @ F^T
    Q = W_q @ F.T
    
    return Q
