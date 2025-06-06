from random import randrange


class MonteCarlo:
    def __init__(self, task_numbers=700, time=300, accuracy=1000): # переименовать accuracy в число решений
        self.tasks_number = task_numbers
        self.time = time
        self.accuracy = accuracy

    def get_window(self):
        best_windows = []
        for i in range(self.accuracy):
            tasks = [randrange(100, 501) / 100 for j in range(self.tasks_number)]
            # tasks = [3 for j in range(self.tasks_number)]
            best_window = 0
            best_number = 0
            windows = [randrange(100, 501) / 100 for i in range(100)]
            windows.sort()
            for window in windows:
                if self.result(tasks, window) > best_number:
                    best_window = window
                    best_number = self.result(tasks, window)
            best_windows.append(best_window)
        return sum(best_windows) / len(best_windows)

    def result(self, tasks, window):
        number = 0
        for i in range(min(int((self.time / window) // 1), self.tasks_number)):
            if tasks[i] <= window:
                number += 1
        return number


arr = []
for i in range(5):
    m = MonteCarlo()
    s = m.get_window()
    s = str(s)
    print(s[0] + ',' + s[2:], end='\t')

