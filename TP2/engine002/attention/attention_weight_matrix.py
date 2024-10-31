import numpy as np

def A(a_x1: np.array, a_x2: np.array, a_x3: np.array, a_x4: np.array):
    """Create attention weight matrix by stacking attention vectors"""
    # Stack attention vectors vertically
    return np.vstack((a_x1, a_x2, a_x3, a_x4))