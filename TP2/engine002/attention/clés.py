import numpy as np

def clés(dim_wk: tuple, F: np.array):
    """Calculate key matrix K = W_k @ F^T"""
    # Generate random weight matrix W_k
    W_k = np.random.rand(*dim_wk)
    
    # Calculate K = W_k @ F^T
    K = W_k @ F.T
    
    return K
