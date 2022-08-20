def create_stack():
    stack = []
    return stack

def check_empty(stack):
    return len(stack)== 0

def push(stack, value):
    stack.append(value)
    return stack

def pop(stack):
    if( check_empty(stack)):
        print(" the stack is empty")
    else :
        stack.pop()
    return stack

stack = create_stack()
print(check_empty(stack))
push(stack, 3)
push(stack, 4)
print(stack)
