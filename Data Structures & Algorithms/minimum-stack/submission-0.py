class MinStack:

    def __init__(self):
        self.stack = []
        self._minstack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self._minstack) == 0:
            self._minstack.append(val)
        elif self._minstack[-1] >= val:
            self._minstack.append(val)
        else:
            pass

    def pop(self) -> None:
        if self.stack[-1] == self._minstack[-1]:
            self._minstack.pop()

        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self._minstack[-1]
