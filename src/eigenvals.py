import numpy as np

def find_eigenvalues_2x2(matrix):
    """
    Find eigenvalues of a 2x2 matrix using the characteristic equation method.
    """
    A = np.array(matrix)
    
    if A.shape != (2, 2):
        raise ValueError("Matrix must be 2x2")
    
    a = A[0, 0]
    b = A[0, 1]
    c = A[1, 0]
    d = A[1, 1]
    
    trace = a + d
    determinant = a * d - b * c
    discriminant = trace**2 - 4*determinant
    
    lambda1 = (trace + np.sqrt(complex(discriminant))) / 2
    lambda2 = (trace - np.sqrt(complex(discriminant))) / 2
    
    if abs(lambda1.imag) < 1e-10:
        lambda1 = lambda1.real
    if abs(lambda2.imag) < 1e-10:
        lambda2 = lambda2.real
        
    return lambda1, lambda2
# returns eigenvalues 
def eigenSolver():
    """
    Interactive function to get matrix input from user and calculate eigenvalues.
    """
    print("Enter the elements of a 2x2 matrix:")
    
    matrix = []
    for i in range(2):
        row = []
        for j in range(2):
            while True:
                try:
                    value = float(input(f"Enter element at position ({i+1},{j+1}): "))
                    row.append(value)
                    break
                except ValueError:
                    print("Please enter a valid number")
        matrix.append(row)
    
    print("\nYour matrix:")
    print(np.array(matrix))
    
    eigenvalues = find_eigenvalues_2x2(matrix)
    print("\nEigenvalues:", eigenvalues)
    
    return eigenvalues

def determinant(): 
    # ad-bc for 2x2
    pass

    

if __name__ == "__main__":
    try:
        eigenSolver()
    except KeyboardInterrupt:
        print("\nProgram terminated by user")
    except Exception as e:
        print(f"An error occurred: {e}")
