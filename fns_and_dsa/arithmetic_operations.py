#!/usr/bin/env python3

def perform_operation(num1: float, num2: float, operation: str) -> float:
    """
    Perform basic arithmetic operations on two numbers.
    
    Args:
        num1: First number (float)
        num2: Second number (float)
        operation: Operation to perform ('add', 'subtract', 'multiply', 'divide')
    
    Returns:
        Result of the arithmetic operation as float.
        Returns None for division by zero or invalid operation.
    """
    operation = operation.lower()
    
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return None  # main.py will handle this appropriately
        return num1 / num2
    else:
        return None  # invalid operation

