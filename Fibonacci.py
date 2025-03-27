#   A Fibonacci sequence is a sequence in which each element is the sum of the two elements that precede it.

def fibonacci_iterative(n):
    fib_series = []
    a, b = 0, 1  # First two Fibonacci numbers
    for _ in range(n):
        fib_series.append(a)
        a, b = b, a + b  # Update values
    return fib_series

# Example usage:
n = 50  # Generate first 10 Fibonacci numbers
print(fibonacci_iterative(n))
