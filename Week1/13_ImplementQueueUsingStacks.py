# https://leetcode.com/problems/implement-queue-using-stacks/ 232. Implement Queue using Stacks AlgoMonster: Not sure
# yet LeetCode Description: https://leetcode.com/problems/implement-queue-using-stacks/solutions/3205822/implementing
# -a-queue-using-two-stacks-in-python-a-simple-and-efficient-approach/

class MyQueue:

    def __init__(self):  # 43ms
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        self.stack1.append(x)

    def pop(self) -> int:
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())

        return self.stack2.pop()

    def peek(self) -> int:
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())

        return self.stack2[-1]

    def empty(self) -> bool:
        return not self.stack1 and not self.stack2


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

if __name__ == '__main__':
    tests = [
        [["MyQueue", "push", "push", "peek", "pop", "empty"], [[], [1], [2], [], [], []],
         [[None], [None], [None], [1], [1], False]]
    ]

    for test in tests:
        for i in range(len(test[0])):
            if test[0][i] == "MyQueue":
                obj = MyQueue()
            if obj:
                if test[0][i] == "push" and obj:
                    obj.push(test[1][i])
                if test[0][i] == "pop" and obj:
                    result = obj.pop()
                    if result != test[2][i]:
                        print(f"Pop Error: Expected {test[2][i]} but got {result} instead")
                    else:
                        print(f"pop: {result}")
                if test[0][i] == "peek" and obj:
                    result = obj.peek()
                    if result != test[2][i]:
                        print(f"Peek Error: Expected {test[2][i]} but got {result} instead")
                    else:
                        print(f"peek: {result}")
                if test[0][i] == "empty" and obj:
                    result = obj.empty()
                    if result != test[2][i]:
                        print(f"Empty Error: Expected {test[2][i]} but got {result} instead")
                    else:
                        print(f"empty: {result}")
            else:
                print(f"No object captured")
