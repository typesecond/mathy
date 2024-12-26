import numpy as np

def find_eigenvalues_2x2(matrix):
    """
    Find eigenvalues of a 2x2 matrix using the characteristic equation method.
    
    Parameters:
    matrix: A 2x2 numpy array or list of lists
    
    Returns:
    tuple: (lambda1, lambda2) containing the two eigenvalues
    """
    # Convert input to numpy array if it isn't already
    A = np.array(matrix)
    
    # Check if matrix is 2x2
    if A.shape != (2, 2):
        raise ValueError("Matrix must be 2x2")
    
    # Extract matrix elements
    a = A[0, 0]
    b = A[0, 1]
    c = A[1, 0]
    d = A[1, 1]
    
    # Calculate coefficients of characteristic equation: λ² - (trace)λ + (determinant) = 0
    trace = a + d
    determinant = a * d - b * c
    
    # Use quadratic formula to solve for eigenvalues
    # λ = [-(-trace) ± √(trace² - 4*determinant)] / 2
    discriminant = trace**2 - 4*determinant
    
    lambda1 = (trace + np.sqrt(complex(discriminant))) / 2
    lambda2 = (trace - np.sqrt(complex(discriminant))) / 2
    
    # Convert to real if eigenvalues are real
    if abs(lambda1.imag) < 1e-10:
        lambda1 = lambda1.real
    if abs(lambda2.imag) < 1e-10:
        lambda2 = lambda2.real
        
    return lambda1, lambda2

# Example usage and testing
def test_eigenvalue_solver():
    # Test case 1: Matrix with real eigenvalues
    matrix1 = [
        [4, 1],
        [1, 4]
    ]
    print("Matrix 1:")
    print(np.array(matrix1))
    eigenvals1 = find_eigenvalues_2x2(matrix1)
    print("Eigenvalues:", eigenvals1)
    
    # Test case 2: Matrix with complex eigenvalues
    matrix2 = [
        [0, -1],
        [1, 0]
    ]
    print("\nMatrix 2:")
    print(np.array(matrix2))
    eigenvals2 = find_eigenvalues_2x2(matrix2)
    print("Eigenvalues:", eigenvals2)

if __name__ == "__main__":
    test_eigenvalue_solver()
