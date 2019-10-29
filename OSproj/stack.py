
class stack:
    def __init__(self):
        self.nums = []

    def isEmpty(self):
        return self.nums == []

    def push(self, num):
        self.nums.append(num)

    def pop(self):
        return self.nums.pop()

    def peek(self):
        return self.nums[len(self.nums) - 1]

    def size(self):
        return len(self.nums)