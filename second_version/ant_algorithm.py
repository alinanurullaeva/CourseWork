import random


class Ant:
    def __init__(self, n, r):
        self.n = n # кол-во городов
        self.ant = n # кол-во муравьёв
        self.cities = [] # координаты городов
        self.a = 1 # коэффициент, влияющий на учёт феромонов
        self.b = 1 # коэффициент, влияющий на учёт расстояния
        self.q = 5 # коэффициент, необходимый для расчета увеличения феромона
        self.p = 0.7 # коэффициент испарения феромонов
        for i in range(n):
            arr = (random.randrange(0, r), random.randrange(0, r))
            while arr in self.cities:
                arr = (random.randrange(0, r), random.randrange(0, r))
            self.cities.append(arr)
        # self.pos = self.cities # координаты муравьёв, обновляются
        self.pos = [i for i in range(n)] # города, в которых находятся муравьи, обновляются
        self.fer = [[1 for j in range(n)] for i in range(n)] # количество феромона между вершинами, обновляется
        for i in range(n):
            self.fer[i][i] = 0
        self.dist = [] # расстояние между городами
        for i in range(n):
            s = []
            for j in range(n):
                s.append(((self.cities[i][0] - self.cities[j][0]) ** 2 +
                          (self.cities[i][1] - self.cities[j][1]) ** 2) ** 0.5)
            self.dist.append(s)
        self.prob = self.probability() # вероятность перехода из одного города в другой, обновляется

    def probability(self):
        prob = []
        s = 0
        n = self.n
        for i in range(n):
            arr = []
            for j in range(n):
                # arr.append(self.fer[i][j] ** self.a * (1 /self.dist[i][j]) ** self.b)
                if j != i:
                    arr.append(self.fer[i][j] ** self.a * (1 /self.dist[i][j]) ** self.b)
                    # arr.append(self.fer[i][j] / self.dist[i][j])
                else:
                    arr.append(0)
            s = s + sum(arr)
            prob.append(arr)
        prob = [[el1 / sum(el2) for el1 in el2] for el2 in prob]
        return prob

    def refresh(self):
        fer = [[0 for i in range(self.n)] for j in range(self.n)]
        for i in range(len(self.pos)):
            n = random.random()
            s = 0
            arr = []
            for j in range(len(self.prob[i])):
                s = s + self.prob[i][j]
                arr.append(s)
            ind = 0
            # print('1', arr)
            for j in range(len(arr) - 1, -1, -1):
                if n < arr[j] and j != i:
                    ind = j
            # print('ind', ind, n)
            self.pos[i] = ind
            fer[i][ind] = fer[i][ind] + self.q/self.dist[i][ind]
            fer[ind][i] = fer[i][ind]
        for i in range(self.n):
            for j in range(self.n):
                self.fer[i][j] = self.fer[i][j] * self.p + fer[i][j]
        self.prob = self.probability()
        print()
        for el in self.prob:
            print(el)


a = Ant(5, 10)
for el in a.probability():
    print(el)
for el in range(5):
    a.refresh()