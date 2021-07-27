# Python-Essentials-LAB-3.2.1.12-Adding-Stack

A brand new stack implementation from scratch. This time, we'll use the objective approach.

**What is a stack?**

A stack is a structure developed to store data in a very specific way. Imagine a stack of coins. You aren't able to put a coin anywhere else but on the top of the stack.
Similarly, you can't get a coin off the stack from any place other than the top of the stack. If you want to get the coin that lies on the bottom, you have to remove all the coins from the higher levels.

The alternative name for a stack (but only in IT terminology) is LIFO.

It's an abbreviation for a very clear description of the stack's behavior: Last In - First Out. The coin that came last onto the stack will leave first.
A stack is an object with two elementary operations, conventionally named push (when a new element is put on the top) and pop (when an existing element is taken away from the top).

Stacks are used very often in many classical algorithms, and it's hard to imagine the implementation of many widely used tools without the use of stacks.

**Adding stack**

Now let's go a little further. Let's add a new class for handling stacks. The new class should be able to evaluate the sum of all the elements currently stored on the stack.

**Complete code includes**
```
class Stack:
    # This class is a stack implementation

class AddingStack(Stack):
    # This class is a subclass of the Stack class
    # It implements a new function - summing elements in the stack
```
