import random


class Ant:
    def __init__(self, n, a, r, s):
        self.number = n # количество городов
        self.ant = a # количество муравьев
        self.cities = [] # координаты городов в декартовой системе координат
        self.dist = [] # длины дорог между городами (если дороги нет, то длина равна 0)
        self.fer = [[1 for i in range(self.number)] for j in range(self.number)]  # количество феромонов на дорогах
        self.pos = [random.randrange(self.number) for i in range(self.ant)]
        self.way = [[self.pos[i]] for i in range(self.ant)]
        self.stop_ind = s # максимальное количество городов, между которыми может не быть дорог
        self.stop = [] # между какими городами нет дорог
        self.a = 1  # коэффициент, влияющий на учёт феромонов
        self.b = 1  # коэффициент, влияющий на учёт расстояния
        self.q = 10  # коэффициент, необходимый для расчета увеличения феромона
        self.p = 0.7  # коэффициент испарения феромонов
        for i in range(self.number):
            city = (random.randrange(0, r), random.randrange(0, r))
            while city in self.cities:
                city = (random.randrange(0, r), random.randrange(0, r))
            self.cities.append(city)
        for i in range(self.number):
            arr = []
            for j in range(self.number):
                arr.append(((self.cities[i][0] - self.cities[j][0]) ** 2 +
                          (self.cities[i][1] - self.cities[j][1]) ** 2) ** 0.5)
            self.dist.append(arr)
        for x in range(self.stop_ind):
            i = random.randrange(0, self.number)
            j = random.randrange(0, self.number)
            self.dist[i][j] = 0
            self.dist[j][i] = 0
            self.stop.append((min(i, j), max(i, j)))
        self.prob = self.probability() # вероятность выбора дорог

    def probability(self):
        prob = []
        for i in range(self.number):
            arr = []
            for j in range(self.number):
                if self.dist[i][j] != 0:
                    arr.append(self.fer[i][j] ** self.a * (1 /self.dist[i][j]) ** self.b)
                else:
                    arr.append(0)
            prob.append(arr)
        prob = [[el/sum(arr) for el in arr] for arr in prob]
        for i in range(len(prob)):
            s = sum(prob[i])
            for j in range(len(prob[i])):
                prob[i][j] = prob[i][j] / s
        prob2 = []
        for i in range(self.number):
            arr = []
            for j in range(self.number):
                arr.append(sum(prob[i][:j + 1]))
            prob2.append(arr)
        return prob2

    def refresh(self):
        fer = [[0 for i in range(self.number)] for j in range(self.number)]
        for i in range(self.ant):
            n = random.random()
            ind = 0
            for j in range(self.number - 1, -1, -1):
                if n < self.prob[self.pos[i]][j] and j != i:
                    ind = j
            self.pos[i] = ind
            self.way[i].append(ind)
            if self.dist[self.pos[i]][ind] != 0:
                fer[self.pos[i]][ind] = fer[self.pos[i]][ind] + self.q / self.dist[self.pos[i]][ind]
                fer[ind][self.pos[i]] = fer[self.pos[i]][ind]
        for i in range(self.number):
            for j in range(self.number):
                self.fer[self.pos[i]][j] = self.fer[self.pos[i]][j] * self.p + fer[self.pos[i]][j]
        self.prob = self.probability()

    def result(self):
        for i in range(self.number):
            self.refresh()
        good = []
        for el in self.way:
            if el[0] == el[-1] and sorted(el[1:]) == [i for i in range(self.number)]:
                el2 = el[1:]
                el2 = el2[el2.index(0):] + el2[:el2.index(0)]
                good.append(el2)
        if not good:
            return 'Нет ответа'
        arr = []
        for el in good:
            arr.append(good.count(el))
        return good[arr.index(max(arr))]


ant = Ant(10, 50000, 10, 5)
print(ant.cities)
print(ant.stop)
print(ant.result())