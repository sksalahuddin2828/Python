def infix_to_postfix(infix):
    operator_stack = []
    postfix = ""

    # Function to get the precedence of an operator
    def precedence(operator):
        if operator == '+' or operator == '-':
            return 1
        elif operator == '*' or operator == '/':
            return 2
        elif operator == '^':
            return 3
        else:
            return 0

    for char in infix:
        if char.isalnum():
            postfix += char
        elif char == '(':
            operator_stack.append(char)
        elif char == ')':
            while operator_stack and operator_stack[-1] != '(':
                postfix += operator_stack.pop()
            operator_stack.pop()  # Remove '(' from the stack
        else:
            while operator_stack and precedence(char) <= precedence(operator_stack[-1]):
                postfix += operator_stack.pop()
            operator_stack.append(char)

    while operator_stack:
        postfix += operator_stack.pop()

    return postfix


infix = input("Enter infix expression: ")
postfix = infix_to_postfix(infix)
print("Postfix expression:", postfix)


#--------------How to use---------------Mathematica-----------------------------------------

# Enter infix expression: 3 + 4 * 2 / ( 1 - 5 ) ^ 2
# Postfix expression: 3 4 2 * 1 5 - 2 ^ / +


# Enter this value: 3 + (4 * 2) / ((1 - 5) ^ 2)


# Answer: Enter infix expression: 3+(4*2)/((1-5)^2)
#         Postfix expression: 342*15-2^/+
