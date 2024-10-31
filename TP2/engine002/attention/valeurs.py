import numpy as np

def valeurs(dim_wv: tuple, F: np.array):
    """Calculate value matrix V = W_v @ F^T"""
    # Generate random weight matrix W_v
    W_v = np.random.rand(*dim_wv)
    
    # Calculate V = W_v @ F^T
    V = W_v @ F.T
    
    return V