import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from typing import List
import os

def f(x: np.array, t: np.array):
    """Define the f function
    Args:
        x: np.array - position values
        t: np.array - time value
    Return:
        The heart rate model function: e^(-(x-3t)²) * sin(4π(x-t))
    """
    return np.exp(-(x - 3*t)**2) * np.sin(4*np.pi*(x - t))

def animator(x: List, t: List, path: str, f: f) -> None:
    """
    Creates and saves an animation of the function f(x,t)
    Args:
        x: List containing [x_min, x_max]
        t: List containing [t_min, t_max]
        path: String path where to save the animation
        f: Function to animate
    """
    # Define x_min and x_max from x 
    x_min, x_max = x[0], x[1]

    # Define t_min and t_max from t
    t_min, t_max = t[0], t[1]

    # Generate 100 values between x_min and x_max
    X = np.linspace(x_min, x_max, 100)

    # Generate 100 values between t_min and t_max
    t_values = np.linspace(t_min, t_max, 100)

    fig, axis = plt.subplots()

    axis.set_xlim([x_min, x_max])
    axis.set_ylim([-1, 1])

    # Add title
    axis.set_title("Heart Rate Model Animation")

    # Add y_label
    axis.set_ylabel("f(x,t)")

    # Add x_label
    axis.set_xlabel("x")

    animated_plot, = axis.plot([], [])

    def update_data(frame):
        """Define the update data function
        Args: 
            frame: int - current frame number
        Returns:
            Tuple containing the updated plot
        """
        t = t_values[frame]

        # For each t, calculate the Y with respect to X
        Y = f(X, t)

        animated_plot.set_data(X, Y)
        return animated_plot,

    animation = FuncAnimation(fig=fig, func=update_data, frames=len(t_values), 
                            interval=25, repeat=True)

    # Create directory if it doesn't exist (make data)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    
    # Save the render using the path
    animation.save(path, writer='pillow')

    plt.show()