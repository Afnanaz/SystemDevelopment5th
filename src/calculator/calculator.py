class InvalidInputException(Exception):
    """Exception raised when input values are outside the valid range."""
    pass


class Calculator:
    """Calculator class providing basic arithmetic operations."""

    MAX_VALUE = 1000000
    MIN_VALUE = -1000000

    def _validate_input(self, *values):
        for value in values:
            if value > self.MAX_VALUE or value < self.MIN_VALUE:
                raise InvalidInputException(
                    f"Value {value} is outside the valid range "
                    f"({self.MIN_VALUE} to {self.MAX_VALUE})"
                )

    def add(self, a, b):
        """Add two numbers."""
        self._validate_input(a, b)
        return a + b

    def subtract(self, a, b):
        """Subtract b from a."""
        self._validate_input(a, b)
        return a - b

    def multiply(self, a, b):
        """Multiply two numbers."""
        self._validate_input(a, b)
        return a * b

    def divide(self, a, b):
        """Divide a by b."""
        self._validate_input(a, b)
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
