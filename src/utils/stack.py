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
        if self.is_empty():
            return self.stack.pop()
        else:
            print("Stack ran out of objects")
            return None
    def size(self):
        return len(self.stack)