"""
This script computes the nth Fibonacci number recursively.
It prompts the user to enter a number and prints the result.
"""

def fibonacci(n):
    """Return the nth Fibonacci number."""
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def main():
    """Prompt user for a number and print its Fibonacci value."""
    try:
        n = int(input("Enter a number: "))
        print(f"Fibonacci({n}) = {fibonacci(n)}")
    except ValueError:
        print("Please enter a valid integer.")


if __name__ == "__main__":
    main()
