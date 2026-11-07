ALLOWED_CHARACTERS = set("0123456789+-*/().% ")

def validate_expression(expression):
    if not expression:
        return "Enter an expression first."
    if len(expression) > 120:
        return "Error: expression is too long."
    if any(char not in ALLOWED_CHARACTERS for char in expression):
        return "Error: unsupported character."
    return None
