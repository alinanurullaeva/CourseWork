from random import randrange
from solution import Solution


class MonteCarlo(Solution):
    def __init__(self, accuracy=1000):
        super().__init__()
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