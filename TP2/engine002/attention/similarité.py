import numpy as np

def similarité(K: np.array, Q: np.array):
    """Calculate similarity matrix K^T @ Q"""
    # Calculate dot product K^T @ Q
    return K.T @ Q