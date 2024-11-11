import numpy as np

def execute_operation(operation, matrix_a, matrix_b=None):
    """
    Wykonuje operację na macierzach (dodawanie, mnożenie lub transpozycja) i zwraca wynik.
    Args:
        operation (str): Typ operacji ('add', 'multiply', 'transpose')
        matrix_a (np.ndarray): Pierwsza macierz
        matrix_b (np.ndarray, opcjonalnie): Druga macierz dla operacji dodawania i mnożenia
    Returns:
        np.ndarray: Wynik operacji lub komunikat o błędzie
    """
    if operation == 'add' and matrix_b is not None:
        if matrix_a.shape == matrix_b.shape:
            return matrix_a + matrix_b
        else:
            return "Błąd: Wymiary macierzy muszą być takie same do dodawania."
    
    elif operation == 'multiply' and matrix_b is not None:
        if matrix_a.shape[1] == matrix_b.shape[0]:
            return np.dot(matrix_a, matrix_b)
        else:
            return "Błąd: Liczba kolumn pierwszej macierzy musi być równa liczbie wierszy drugiej macierzy."
    
    elif operation == 'transpose':
        return matrix_a.T
    
    else:
        return "Błąd: Nieprawidłowa operacja lub brak drugiej macierzy do dodawania/mnożenia."


matrix_a = np.array([[1, 2, 3], [4, 5, 6]])
matrix_b = np.array([[7, 8, 9], [10, 11, 12]])

print("Dodawanie:")
print(execute_operation("add", matrix_a, matrix_b))

print("\nMnożenie:")
matrix_c = np.array([[1, 2], [3, 4], [5, 6]])
print(execute_operation("multiply", matrix_a, matrix_c))

print("\nTranspozycja:")
print(execute_operation("transpose", matrix_a))
