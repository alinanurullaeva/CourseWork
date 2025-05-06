class Solution:
    def __init__(self, task_numbers=200, time=200):
        self.tasks_number = task_numbers
        self.time = time


    def result(self, tasks, window):
        number = 0
        for i in range(min(int((self.time / window) // 1), self.tasks_number)):
            if tasks[i] <= window:
                number += 1
        return number