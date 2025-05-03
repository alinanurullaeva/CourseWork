# решить уравнение a+2b+3c+4d=30 в натуральных числах
import random


class Solution:
    def __init__(self, n):
        self.n = n
        self.arr = [[random.randrange(1, 22) for j in range(4)] for i in range(n)]
        """self.arr[0] = [1, 28, 15, 3]
        self.arr[1] = [14, 9, 2, 4]
        self.arr[2] = [13, 5, 7, 3]
        self.arr[3] = [23, 8, 16, 19]
        self.arr[4] = [9, 13, 5, 2]"""

    def result(self, n):
        arr = self.arr[n]
        return abs(arr[0] + 2 * arr[1] + 3 * arr[2] + 4 * arr[3] - 30)

    def probability(self):
        # prob = [sum([1/self.result(i) for i in range(len(self.arr))]) for n in range(self.n)]
        prob = [(1/self.result(n)) / sum([1 / self.result(i) for i in range(self.n)]) for n in range(self.n)]
        print('prob = ', prob, sum(prob))
        # return (1/self.result(n)) / s
        prob2 = [sum(prob[0: i + 1]) for i in range(self.n)]
        return prob2

    def average_result(self):
        return sum([self.result(i) for i in range(len(self.arr))]) / len(self.arr)

    def selection(self):
        arr = []
        prob = self.probability()
        # n = len(self.arr)
        while len(arr) < self.n:
            mother = random.random()
            mother_id = 0
            for j in range(self.n):
                if mother <= prob[j]:
                    mother_id = j
                else:
                    break
            father = random.random()
            father_id = 0
            for j in range(self.n):
                if father <= prob[j]:
                    father_id = j
                else:
                    break
            # father = random.randrange(n)
            if mother_id != father_id: # and (mother_id, father_id) not in arr:
                arr.append((mother_id, father_id))
        return arr # взять не 5 пар, а перебрать несколько

    def crossover(self):
        arr = []
        for i in self.selection():
            n = random.randrange(1, len(self.arr) - 1)
            result = self.arr[i[0]][:n] + self.arr[i[1]][n:]
            n = random.randrange(0, 4)
            result[n] = random.randrange(1, 22)
            arr.append(result)
        self.arr = arr # выбирать лучших



n = 5
s = Solution(n)
print(s.arr)
print(s.probability())
# print('sum', sum(s.probability()))
prob = s.probability()
'''prob2 = [sum(prob[0: i + 1]) for i in range(n)]
print(prob2)
print('prob', prob)
for i in range(n):
    print(i, prob[0:i+1])'''
# print(Solution.probability(s, 2))
# print(Solution.average_result(s))
# print(Solution.selection(s))
s.crossover()
print(s.arr)
for i in range(1):
    if any([s.result(j) for j in range(n)]) == 0:
        for j in range(n):
            if s.result(j) == 0:
                print(s.arr[j])
                break
    s.crossover()