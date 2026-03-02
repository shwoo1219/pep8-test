"""Well-formatted Python module following PEP8."""

import os
import sys


def greet(name):
    """Return a greeting string for the given name."""
    return f"Hello, {name}!"


def add(a, b):
    """Return the sum of two numbers."""
    return a + b


def main():
    """Entry point."""
    user = os.environ.get("USER", "world")
    print(greet(user))
    print(add(1, 2))
    sys.exit(0)


if __name__ == "__main__":
    main()
