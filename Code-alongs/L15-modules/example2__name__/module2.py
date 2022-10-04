import numpy as np

def trigometric_identity(angle: float) -> float:
    """Calculates trig identity

    param:
    angle: angle in radius

    return: trigonometric one
    
    """
    print("running trigonometric_identity()")
    return np.cos(angle)**2 + np.sin(angle)**2


if __name__ == "__main__":
    print("Running directly from module2.py")
    print(trigometric_identity(42))
else:
    print("Imported from module2")