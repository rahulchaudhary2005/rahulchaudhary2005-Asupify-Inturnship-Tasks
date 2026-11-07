import ast
import math
import operator

class CalculatorError(Exception):
    """Raised when an expression cannot be safely evaluated."""

class CalculatorService:
    _binary_operations = {
        ast.Add: operator.add, ast.Sub: operator.sub,
        ast.Mult: operator.mul, ast.Div: operator.truediv,
        ast.Pow: operator.pow, ast.Mod: operator.mod,
    }
    _unary_operations = {ast.UAdd: operator.pos, ast.USub: operator.neg}

    def calculate(self, expression):
        try:
            parsed = ast.parse(expression, mode="eval")
            result = self._evaluate_node(parsed.body)
        except ZeroDivisionError as exc:
            raise CalculatorError("Error: division by zero") from exc
        except (SyntaxError, ValueError, TypeError, OverflowError) as exc:
            raise CalculatorError("Error: invalid expression") from exc
        if isinstance(result, bool) or not isinstance(result, (int, float)):
            raise CalculatorError("Error: invalid result")
        if not math.isfinite(result):
            raise CalculatorError("Error: result is too large or undefined")
        return result

    def _evaluate_node(self, node):
        if isinstance(node, ast.Constant) and type(node.value) in (int, float):
            return node.value
        if isinstance(node, ast.BinOp) and type(node.op) in self._binary_operations:
            left, right = self._evaluate_node(node.left), self._evaluate_node(node.right)
            if isinstance(node.op, ast.Pow) and abs(right) > 100:
                raise CalculatorError("Error: exponent is too large")
            return self._binary_operations[type(node.op)](left, right)
        if isinstance(node, ast.UnaryOp) and type(node.op) in self._unary_operations:
            return self._unary_operations[type(node.op)](self._evaluate_node(node.operand))
        raise CalculatorError("Error: unsupported input")

    @staticmethod
    def format_result(value):
        if isinstance(value, float) and value.is_integer():
            return str(int(value))
        return f"{value:.10g}"
