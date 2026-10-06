def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Деление на ноль невозможно")
    return a / b


def power(a, b):
    return a ** b


OPERATIONS = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    "**": power,
}


def calculate(a, operator, b):
    """Выполняет операцию над двумя числами."""
    print(operator)
    if operator not in OPERATIONS:
        raise ValueError(f"Неизвестная операция: {operator}")
    return OPERATIONS[operator](a, b)
