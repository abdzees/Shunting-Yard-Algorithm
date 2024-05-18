from stack import Stack

class ExpressionEvaluator:
    
    def __init__(self, invert_precedence=False):
        self.invert_precedence = invert_precedence

    def parse(self, expression):

        # Initializing the stack and the output lists
        output = [] 
        stack = Stack() 

        # Defining operator precedence
        precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
        if self.invert_precedence:
            precedence = {op: 3 - prec for op, prec in precedence.items()} # Inverting the precedence if invert_precedence is set to true

        # Defining operators and their associativity
        operators = set(precedence.keys())
        left_associative = {'+': True, '-': True, '*': True, '/': True}

        # Helper function to handle the precedence and associativity of operators
        def is_higher_precedence(op1, op2):
            return (precedence[op1] > precedence[op2]) or (precedence[op1] == precedence[op2] and left_associative[op1])

        # Splitting up the characters
        characters = expression.split()

        for character in characters:
            if character.isnumeric(): # If the character is an operand
                output.append(character)

            elif character in operators: # If the character is an operator
                while stack and stack.peek() in operators and is_higher_precedence(stack.peek(), character):
                    output.append(stack.pop()) # Pops the higher prec operator from the stack and adds it to the output 
                stack.push(character)

            elif character == '(':  # Left parenthesis
                stack.push(character)
            elif character == ')':  # Right parenthesis
                while stack and stack.peek() != '(':
                    output.append(stack.pop())
                stack.pop()  # Remove the left parenthesis

        # Append remaining items from the stack to output
        while stack:
            output.append(stack.pop())

        return ' '.join(output) # Returns the output list in the form of a string

    def evaluate(self, expression):
        pass
