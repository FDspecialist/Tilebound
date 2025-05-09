class Stack:
    def __init__(self):
        self.stack = []
    def is_empty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False
    def push(self,obj):
        self.stack.append(obj)
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return None

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            return None
    def size(self):
        return len(self.stack)