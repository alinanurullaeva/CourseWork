from random import randrange


class MonteKarlo:
    def __init__(self, task_numbers=200, time=200, accuracy=1000):
        # self.window = 0
        self.tasks_number = task_numbers
        self.time = time
        self.accuracy = accuracy

    def get_window(self):
        best_windows = []
        for i in range(self.accuracy):
            tasks = [randrange(100, 501) / 100 for j in range(self.tasks_number)]
            # tasks = [3 for j in range(100)]
            best_window = 0
            best_number = 0
            windows = [randrange(100, 501) / 100 for i in range(100)]
            windows.sort()
            # for window in range(100, 501): # не перебор, а случайные числа
            for window in windows:
                # window = window / 100
                if self.result(tasks, window) > best_number:
                    best_window = window
                    best_number = self.result(tasks, window)
            best_windows.append(best_window)
        # print(best_windows)
        # print(min(best_windows), max(best_windows))
        return sum(best_windows) / len(best_windows)
        # return best_windows



    def result(self, tasks, window):
        number = 0
        for i in range(min(int((self.time / window) // 1), self.tasks_number)):
        # for i in range(int((self.time / window) // 1)):
            if tasks[i] <= window:
                number += 1
        return number


m = MonteKarlo()
print(m.get_window())