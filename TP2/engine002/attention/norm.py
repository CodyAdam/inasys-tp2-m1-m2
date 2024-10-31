import numpy as np

def norm(d_k: int, similarité: np.array):
    """Normalize similarity matrix by sqrt(d_k)"""
    return similarité / np.sqrt(d_k)
