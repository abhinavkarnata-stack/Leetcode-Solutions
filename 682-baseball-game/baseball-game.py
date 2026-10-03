class Solution:
    def calPoints(self, operations: list[str]) -> int:
        stack = []
        for ch in operations:
            if stack and ch == 'C':
                stack.pop()
            elif ch == '+':
                stack.append(stack[-1] + stack[-2])
            elif ch == 'D':
                stack.append(stack[-1] * 2)
            else:
                stack.append(int(ch))
            
        return sum(stack)