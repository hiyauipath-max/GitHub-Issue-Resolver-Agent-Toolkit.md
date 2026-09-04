# calculator.py — demo file with intentional bugs for the AI Issue Resolver

def divide(a, b):
    # BUG 1: No zero-division handling. divide(10, 0) crashes with ZeroDivisionError.
    return a / b


def average(numbers):
    # BUG 2: Crashes on an empty list (division by zero via len()).
    return sum(numbers) / len(numbers)


def factorial(n):
    # BUG 3: No handling for negative input; recurses forever and overflows.
    if n == 0:
        return 1
    return n * factorial(n - 1)


def is_even(n):
    # BUG 4: Wrong operator — uses '=' assignment instead of '==' comparison.
    # (This is a syntax error in real Python; great for showing the agent spot it.)
    return n % 2 = 0


def find_max(items):
    # BUG 5: Off-by-one — range stops one short, so the last item is never checked.
    maximum = items[0]
    for i in range(1, len(items) - 1):
        if items[i] > maximum:
            maximum = items[i]
    return maximum


def to_celsius(fahrenheit):
    # BUG 6: Wrong formula — missing the *5/9 factor.
    return (fahrenheit - 32)
