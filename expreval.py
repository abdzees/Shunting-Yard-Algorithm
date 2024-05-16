from stack import Stack

class ExpressionEvaluator:
    
    def __init__(self, invert_precedence=False):
        self.output = []  # Storing the output (list)
        self.operators = {'+', '*'}  # Defining operators set

    def parse(self, expression):
        stack = Stack()
        for char in expression:
            if char.isdigit():  # Checks if the character is a digit
                self.output.append(int(char))
            elif char in self.operators:  # Checks if the character is an operator and then orders them in the stack using PEMDAS
                lastOperator = stack.peek()
                if lastOperator == "*" and char == "+":
                    self.output.append(stack.pop())
                    stack.push(char)
                else:
                    stack.push(char)

        # Append remaining items from the stack to output
        while stack:
            self.output.append(stack.pop())

        return self.output

    def evaluate(self, expression):
        pass
