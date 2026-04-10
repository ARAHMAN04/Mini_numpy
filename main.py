# main.py
from creation.array_creation import array, zeros, ones, eye
from array_stats.stats import mean, var, std
from exceptions.errors import NonNumericDataError

def main():
    print("Welcome to Mini NumPy!\n")

    A = array([[1, 2], [3, 4]])
    B = array([[5, 6], [7, 8]])
    print("A:\n", A)
    print("B:\n", B)

    print("\nZeros (2x3):\n", zeros((2, 3)))
    print("Identity (3x3):\n", eye(3))

    print("\nA + B:\n", A + B)
    print("A * 10:\n", A * 10)
    print("A ** 2:\n", A ** 2)

    print(f"\nMean: {mean(A)}")
    print(f"Variance: {var(A)}")
    print(f"Std Dev: {std(A)}")

    try:
        array([[1, 2], ["three", 4]])
    except NonNumericDataError as e:
        print(f"\nCaught bad data: {e}")

    try:
        print(A + array([1, 2, 3]))
    except Exception as e:
        print(f"Caught shape mismatch: {e}")

if __name__ == "__main__":
    main()