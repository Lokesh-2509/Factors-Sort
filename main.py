def count_factors(n):
    count = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            count += 1
            if n // i != i:
                count += 1
    return count
def custom_comparison(a, b):
    a_factors = count_factors(a)
    b_factors = count_factors(b)
    if a_factors == b_factors:
        return a - b
    return a_factors - b_factors
def sort_by_factors(A):
    n = len(A)
    for i in range(n):
        for j in range(i + 1, n):
            if custom_comparison(A[i], A[j]) > 0:
                A[i], A[j] = A[j], A[i]
if __name__ == "__main__":
    A = list(map(int, input("Enter the elements of the array (separated by space): ").split()))
    sort_by_factors(A)
    print("Sorted array:", A)
