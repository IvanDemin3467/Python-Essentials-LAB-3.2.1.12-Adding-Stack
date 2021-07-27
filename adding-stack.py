#This is the Python Essentials 2 LAB 3.2.1.12 Adding Stack

class Stack:
    # This class is a stack implementation
    def __init__(self):
        self.__stack_list = []  # This list contains stack values. This is private property

    def push(self, val):        # This method is for pushing the next value onto the stack
        self.__stack_list.append(val)

    def pop(self):              # This method is for popping the topmost value from the stack
        val = self.__stack_list[-1]
        del self.__stack_list[-1]
        return val


class AddingStack(Stack):
    # This class is a subclass of the Stack class
    # It implements a new function - summing elements in the stack
    def __init__(self):         # This method overrides the constructor of the Stack class
        Stack.__init__(self)
        self.__sum = 0          # It adds a new property to store the sum of the stack items

    def get_sum(self):          # This method is for the return of private property "__sum"
        return self.__sum

    def push(self, val):        # This method overrides Stack.push() to implement summation
        self.__sum += val
        Stack.push(self, val)

    def pop(self):              # This method overrides Stack.pop() to implement summation
        val = Stack.pop(self)
        self.__sum -= val
        return val


# Main
if __name__ == "__main__":
    stack_object = AddingStack()

    for i in range(5):
        stack_object.push(i)
    print(stack_object.get_sum())

    for i in range(5):
        print(stack_object.pop())





