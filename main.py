class Task:
    def __init__(self, title: str, description: str):
        self.title = title
        self.description = description


class TaskManager:
    def __init__(self):
        self.__tasks = []

    def add_task(self, title: str, description: str):
        task = Task(title, description)
        self.__tasks.append(task)

    @property
    def tasks(self):
        tasks_lines = ''
        counter = 1
        for task in self.__tasks:
            tasks_lines += f'{counter}: {task.title} {task.description}\n'
            counter += 1

        return tasks_lines


if __name__ == "__main__":
    test_task = TaskManager()
    for idx in range(10):
        test_task.add_task(f'Задача {idx+1}', f'Описание задачи {idx+1}')

    print(test_task.tasks)

