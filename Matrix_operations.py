import numpy as np

def input_matrix(name):
    rows = int(input(f"Enter number of rows for {name}: "))
    cols = int(input(f"Enter number of columns for {name}: "))
    print(f"Enter the elements of {name} row-wise:")
    matrix = []
    for i in range(rows):
        row = list(map(float, input().split()))
        matrix.append(row)
    return np.array(matrix)

def show_menu():
    print("\nMatrix Operations:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Transpose")
    print("5. Determinant")
    print("6. Exit")

def main():
    while True:
        show_menu()
        choice = input("Enter your choice: ")
        
        if choice in ['1', '2', '3']:
            A = input_matrix("Matrix A")
            B = input_matrix("Matrix B")

            if choice == '1':
                print("Result:\n", A + B)
            elif choice == '2':
                print("Result:\n", A - B)
            elif choice == '3':
                print("Result:\n", np.matmul(A, B))

        elif choice == '4':
            A = input_matrix("Matrix")
            print("Transpose:\n", A.T)

        elif choice == '5':
            A = input_matrix("Matrix")
            if A.shape[0] == A.shape[1]:
                print("Determinant:", round(np.linalg.det(A), 2))
            else:
                print("Matrix must be square.")

        elif choice == '6':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
