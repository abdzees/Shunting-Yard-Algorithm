from expreval import ExpressionEvaluator

expr = "3 + 5 * 2"
expr_eval = ExpressionEvaluator()
rpn = expr_eval.parse(expr)
val = expr_eval.evaluate(rpn)
print(f"expr: {expr}\n  rpn: {rpn}\n  val: {val}")
