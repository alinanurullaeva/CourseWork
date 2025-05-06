# решить уравнение a+2b+3c+4d=30 в натуральных числах
import random


class Genetic:
    def __init__(self, n):
        self.n = n
        self.arr = [[random.randrange(1, 22) for j in range(4)] for i in range(n)]

    def result(self, n=0, arr=None):
        if not arr:
            arr = self.arr[n]
        return abs(arr[0] + 2 * arr[1] + 3 * arr[2] + 4 * arr[3] - 30)

    def probability(self):
        for n in range(self.n):
            if self.result(n) == 0:
                return ['Ура!'] + self.arr[n]
        prob = [(1/self.result(n)) / sum([1 / self.result(i) for i in range(self.n)]) for n in range(self.n)]
        prob2 = [sum(prob[0: i + 1]) for i in range(self.n)]
        return prob2

    def average_result(self):
        return sum([self.result(i) for i in range(len(self.arr))]) / len(self.arr)

    def selection(self):
        arr = []
        prob = self.probability()
        if prob[0] == 'Ура!':
            return prob
        for i in range(min(self.n * 4, self.n ** 2 - 1)):
            mother = random.random()
            mother_id = 0
            for j in range(self.n):
                if mother <= prob[j]:
                    mother_id = j
            father = random.random()
            father_id = 0
            for j in range(self.n):
                if father <= prob[j]:
                    father_id = j
                else:
                    break
            n = random.randrange(1, self.n - 1)
            arr.append((mother_id, father_id, n))
        return arr

    def crossover(self):
        arr = []
        selection = self.selection()
        if selection[0] == 'Ура!':
            return selection[1:]
        for i in selection:
            result = self.arr[int(i[0])][:i[2]] + self.arr[int(i[1])][i[2]:]
            result[random.randrange(0, len(result))] = random.randrange(1, 22)
            arr.append((result, self.result(arr=result)))
        arr = sorted(arr, key=lambda el:el[1])[:self.n]
        for i in range(len(arr)): # выбирать лучших
            self.arr[i] = arr[i][0]
        return []

    def get_result(self):
        result = []
        while not result:
            result = self.crossover()
        return result


number = 5
s = Genetic(number)
print(s.get_result())